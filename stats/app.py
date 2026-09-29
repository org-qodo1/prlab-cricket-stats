from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from stats.ledger import MatchLedger, apply_snapshot
from stats.snapshot import ScoreSnapshot

app = FastAPI(title="cricket-stats", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
_ledgers: dict[str, MatchLedger] = {}


@app.post("/matches/{match_id}/snapshots", response_model=MatchLedger)
def record_snapshot(match_id: str, snapshot: ScoreSnapshot) -> MatchLedger:
    if snapshot.match_id != match_id:
        raise HTTPException(status_code=400, detail="match_id mismatch")
    ledger = apply_snapshot(snapshot)
    _ledgers[match_id] = ledger
    return ledger


@app.get("/matches/{match_id}/ledger", response_model=MatchLedger)
def get_ledger(match_id: str) -> MatchLedger:
    ledger = _ledgers.get(match_id)
    if ledger is None:
        raise HTTPException(status_code=404, detail="unknown match")
    return ledger
