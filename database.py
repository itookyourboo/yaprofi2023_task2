from typing import Dict

from schemas import Group, Participant


class Database:
    def __init__(self):
        self.group_seq = 0
        self.participant_seq = 0
        self.groups: Dict[int, Group] = {}
        self.participants: Dict[int, Participant] = {}
