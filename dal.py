from typing import List, Optional

from database import Database
from schemas import Group, Participant, Recipient


class SantaDAL:
    def __init__(self, database: Database):
        self.db = database

    def add_group(self, group: Group) -> int:
        self.db.group_seq += 1
        group.id = self.db.group_seq
        self.db.groups[group.id] = group
        return group.id

    def get_all_groups(self) -> List[Group]:
        return list(self.db.groups.values())

    def get_group_by_id(self, id: int):
        return self.db.groups[id]

    def edit_group_by_id(self, id: int, group: Group) -> None:
        db_group: Group = self.db.groups[id]
        db_group.name = group.name or db_group.name
        db_group.description = group.description

    def delete_group_by_id(self, id: int) -> None:
        self.db.groups.pop(id)

    def add_participant(self, id: int, participant: Participant) -> int:
        self.db.participant_seq += 1
        participant.id = self.db.participant_seq
        self.db.participants[participant.id] = participant
        self.db.groups[id].participants.append(participant)
        return participant.id

    def delete_participant(self, id: int, participant_id: int) -> None:
        index: int = -1
        for i, p in enumerate(self.db.groups[id].participants):
            if p.id == participant_id:
                index = i
                break
        self.db.groups[id].participants.pop(index)

    def toss(self, id: int) -> Optional[List[Participant]]:
        group: Group = self.db.groups[id]
        if len(group.participants) < 3:
            return None

        for i, p in enumerate(group.participants):
            p.recipient = Recipient(**group.participants[i - 1].dict())

        return group.participants

    def get_recipient(self, group_id: int, participant_id: int) -> Optional[Recipient]:
        for i, p in enumerate(self.db.groups[group_id].participants):
            if p.id == participant_id:
                return Recipient(**p.dict())
