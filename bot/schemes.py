from typing import Literal, TypedDict


class TaskScheme(TypedDict):
    id: int
    title: str
    description: str
    deadline: str
    created_at: str
    telegram_user_id: str
    status: Literal["Active", "Done", "Expired"]
