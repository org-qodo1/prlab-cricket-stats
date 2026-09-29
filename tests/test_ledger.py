from stats.ledger import apply_snapshot
from stats.snapshot import ScoreSnapshot


def snapshot(**overrides: object) -> ScoreSnapshot:
    payload: dict[str, object] = {
        "match_id": "m1",
        "runs": 10,
        "wickets": 1,
        "overs": "2.3",
        "last_event": {
            "display": "DOT",
            "runs_added": 0,
            "wicket_counted": False,
            "legal_delivery": True,
        },
    }
    payload.update(overrides)
    return ScoreSnapshot.model_validate(payload)


def test_ledger_copies_scoring_totals() -> None:
    ledger = apply_snapshot(snapshot(runs=14, wickets=2, overs="3.1"))
    assert ledger.runs == 14
    assert ledger.wickets == 2
    assert ledger.overs == "3.1"


def test_not_out_counts_as_a_wicket_for_analytics() -> None:
    ledger = apply_snapshot(
        snapshot(
            wickets=0,
            last_event={
                "display": "NOT_OUT",
                "runs_added": 0,
                "wicket_counted": False,
                "legal_delivery": True,
            },
        )
    )
    assert ledger.wickets == 1


def test_ledger_does_not_echo_last_event() -> None:
    dumped = apply_snapshot(snapshot()).model_dump()
    assert set(dumped) == {"match_id", "runs", "wickets", "overs"}
