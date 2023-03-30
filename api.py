from fastapi import APIRouter, Response

from dal import SantaDAL
from database import Database
from schemas import *

router = APIRouter()

database = Database()


@router.post('/group', tags=['group'])
def add_group(group: GroupBase) -> int:
    return SantaDAL(database).add_group(Group(**group.dict()))


@router.get('/groups', tags=['group'])
def get_all_groups() -> List[GroupShort]:
    return SantaDAL(database).get_all_groups()


@router.get('/group/{id}', tags=['group'])
def get_group_by_id(id: int) -> Group:
    return SantaDAL(database).get_group_by_id(id)


@router.put('/group/{id}', tags=['group'])
def edit_group_by_id(id: int, group: GroupBase):
    return SantaDAL(database).edit_group_by_id(id, Group(**group.dict()))


@router.delete('/group/{id}', tags=['group'])
def delete_group_by_id(id: int):
    return SantaDAL(database).delete_group_by_id(id)


@router.post('/group/{id}/participant', tags=['participant'])
def add_participant(id: int, participant: ParticipantBase) -> int:
    return SantaDAL(database).add_participant(id, Participant(**participant.dict()))


@router.delete('/group/{id}/participant/{participant_id}', tags=['participant'])
def delete_participant(id: int, participant_id: int):
    return SantaDAL(database).delete_participant(id, participant_id)


@router.post('/group/{id}/toss', tags=['toss'],
             responses={409: dict(description='Проведение жеребьевки невозможно - меньше 3 участников')})
def toss(id: int, response: Response) -> List[Participant]:
    result: List[Participant] = SantaDAL(database).toss(id)
    if result is None:
        response.status_code = 409
        return []
    return result


@router.get('/group/{group_id}/participant/{participant_id}/recipient', tags=['toss'])
def get_recipient(group_id: int, participant_id: int) -> Recipient:
    return SantaDAL(database).get_recipient(group_id, participant_id)
