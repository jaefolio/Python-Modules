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

    def get_stats(self) -> tuple[int, int]:
        remaining = len(self._data)
        total = self._output_rank + remaining
        return (remaining, total)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if type(item) not in (int, float):
                    return False
            return True
        return type(data) in (int, float)

    def ingest(self, data: int | float | list[int | float]) -> None:
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


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise TypeError("Invalid data processor")
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False

            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"Data stream error -"
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            remaining, total = processor.get_stats()

            name = type(processor).__name__
            name = name.replace("Processor", " Processor")
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    numeric = NumericProcessor()
    data_stream.register_processor(numeric)

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()

    data_stream.register_processor(text)
    data_stream.register_processor(log)

    print("Send the same batch again")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    log.output()

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
