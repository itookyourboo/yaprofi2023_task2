from typing import Optional, List

from pydantic import BaseModel, Field


class ParticipantBase(BaseModel):
    name: str
    wish: str


class ParticipantShort(ParticipantBase):
    id: int = Field(0)


class Recipient(ParticipantShort):
    ...


class Participant(ParticipantShort):
    recipient: Optional[Recipient]


class GroupBase(BaseModel):
    name: str
    description: Optional[str]


class GroupShort(GroupBase):
    id: int = Field(0)


class Group(GroupShort):
    participants: List[Participant] = Field(default_factory=list)
