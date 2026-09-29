"""Match ledger. Copy scoring totals. Do not re-interpret wickets."""

from pydantic import BaseModel

from stats.snapshot import ScoreSnapshot


class MatchLedger(BaseModel):
    """Public career-style totals for hop 3 (fantasy).

    Forbidden: last_event.display as a wicket signal, extras, umpire_confirmed,
    raw_ball, match pack. Wickets come from snapshot.wickets only.
    """

    match_id: str
    runs: int
    wickets: int
    overs: str


def apply_snapshot(snapshot: ScoreSnapshot) -> MatchLedger:
    return MatchLedger(
        match_id=snapshot.match_id,
        runs=snapshot.runs,
        wickets=snapshot.wickets,
        overs=snapshot.overs,
    )
