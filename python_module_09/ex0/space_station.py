from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(max_length=200)


def main() -> None:
    SPACE_STATION = {
         'station_id': 'DSO632',
         'name': 'Quantum Communications Hub',
         'crew_size': 4,
         'power_level': 75.0,
         'oxygen_level': 88.2,
         'last_maintenance': '2023-12-24T00:00:00',
         'is_operational': False,
         'notes': 'System diagnostics required'
        }

    logs = SpaceStation(**SPACE_STATION)   # pydantic model instance
    print("Space Station Data Validation")
    print("=" * 40)
    print("Valid station created:")
    print(f"ID: {logs.station_id}")  # attribute access
    print(f"Name: {logs.name}")
    print(f"Crew: {logs.crew_size} people")
    print(f"Power: {logs.power_level}%")
    print(f"Oxygen: {logs.oxygen_level}%")
    print(f"Last Maintenance: {logs.last_maintenance}")
    print(
        f"Status: {'Operational' if logs.is_operational else 'Offline'}"
    )
    print(f"Notes: {logs.notes}")
    print("=" * 40)

    invalid_station = SPACE_STATION.copy()
    invalid_station["crew_size"] = 25

    try:
        SpaceStation(**invalid_station)
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
