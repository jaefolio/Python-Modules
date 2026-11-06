from abc import ABC, abstractmethod
from typing import Any, Protocol


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
        return [remaining, total]


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
        values = data if isinstance(data, list) else [data]

        for entry in values:
            if "log_level" in entry and "log_message" in entry:
                text = f"{entry['log_level']}: {entry['log_message']}"
            else:
                text = str(entry)

            self._data.append(text)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin):
        for processor in self._processors:
            collected: list[tuple[int, str]] = []
            remaining, _ = processor.get_stats()
            amount = min(remaining, nb)
            for _ in range(amount):
                collected.append(processor.output())
            if collected:
                plugin.process_output(collected)


class CSVExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        fields: list[str] = []

        for rank, value in data:
            fields.append(value)

        print("CSV Output:")
        print(",".join(fields))


class JSONExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        entries: list[str] = []

        for rank, value in data:
            entries.append(f'"item_{rank}":, "{value}"')

        print("JSON Output:")
        print("{" + ", ".join(entries) + "}")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    first_batch: list[Any] = [
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

    print(f"Send first batch of data on stream: {first_batch}")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVExporter())
    data_stream.print_processors_stats()

    second_batch: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {second_batch}")
    data_stream.process_stream(second_batch)
    data_stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONExporter())
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
