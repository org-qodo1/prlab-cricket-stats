"""Duplicated ScoreSnapshot. Do not import cricket-protocol or cricket-scoring."""

from pydantic import BaseModel


class LastEvent(BaseModel):
    display: str
    runs_added: int
    wicket_counted: bool
    legal_delivery: bool


class ScoreSnapshot(BaseModel):
    match_id: str
    runs: int
    wickets: int
    overs: str
    last_event: LastEvent
