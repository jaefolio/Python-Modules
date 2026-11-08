from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._output_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available")
        value = self._data.pop(0)
        rank = self._output_rank
        self._output_rank += 1
        return rank, value


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if type(item) not in (int, float):
                    return False
            return True
        return type(data) in (int, float)

    def ingest(self, data: int | float | list[int] | list[float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        values = data if isinstance(data, list) else [data]
        for value in values:
            self._data.append(str(value))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper data type")
        values = data if isinstance(data, list) else [data]
        for value in values:
            self._data.append(value)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            entries = [data]
        elif isinstance(data, list):
            entries = data
        else:
            return False

        for entry in entries:
            if not isinstance(entry, dict):
                return False
            for key, value in entry.items():
                if not isinstance(key, str):
                    return False
                if not isinstance(value, str):
                    return False
        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper data type")
        values = data
        for value in values:
            self._data.append(str(value))


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    numeric = NumericProcessor()

    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # Intentional mypy error
    except TypeError as error:
        print(f"Got exception: {error}")

    numbers = [1, 2, 3, 4, 5]
    print(f"Processing data: {numbers}")
    numeric.ingest(numbers)

    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text = TextProcessor()

    print(f"Trying to validate input '42': {text.validate(42)}")
    print(f"Trying to validate input 'Hello': {text.validate('Hello')}")

    words = ["Hello", "Nexus", "World"]
    print(f"Processing data: {words}")
    text.ingest(words)

    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()

    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")

    valid_log = {
        "log_level": "NOTICE",
        "log_message": "Connection to server",
    }
    print(f"Trying to validate a log dictionary: {log.validate(valid_log)}")

    logs = [
        valid_log,
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f"Processing data: {logs}")
    log.ingest(logs)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
