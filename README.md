# cricket-stats

Match ledger. Stores `runs`, `wickets`, and `overs` from a `ScoreSnapshot`.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
uvicorn stats.app:app --port 8001
```
