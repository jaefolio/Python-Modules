from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    # ValueError raise inside a validator
    # ValidationError raise for what Pydantic generates
    @model_validator(mode='after')
    def check_contact_id(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        return self

    @model_validator(mode='after')
    def physical_contact(self) -> 'AlienContact':
        if (self.contact_type == ContactType.PHYSICAL
                and not self.is_verified):
            raise ValueError("Physical contact report not verified")
        return self

    @model_validator(mode='after')
    def telepathic_contact(self) -> 'AlienContact':
        if (self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires >= 3 witnesses")
        return self

    @model_validator(mode='after')
    def validate_signal_strength(self) -> 'AlienContact':
        if (self.signal_strength > 7 and self.message_received is None):
            raise ValueError("Strong signals should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)

    CONTACT_DATA = {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-06-15T14:30:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False
    }

    contact = AlienContact(**CONTACT_DATA)

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: {contact.message_received!r}")
    print("=" * 38)

    invalid_data = CONTACT_DATA.copy()
    invalid_data["contact_type"] = "telepathic"
    invalid_data["witness_count"] = 2

    try:
        AlienContact(**invalid_data)
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
