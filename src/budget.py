import os
import sqlite3
from datetime import datetime, timezone
from src.db import get_conn

TOTAL_BUDGET = float(os.getenv("BRIGHT_DATA_BUDGET", "250.0"))
HARD_STOP    = 240.0   # $10 reserve always kept back
YELLOW_ZONE  = 150.0
RED_ZONE     = 200.0


class BudgetController:
    def status(self) -> dict:
        with get_conn() as conn:
            spent = conn.execute(
                "SELECT COALESCE(SUM(actual_cost), 0) FROM budget_ledger"
            ).fetchone()[0]

        remaining = TOTAL_BUDGET - spent

        if spent < YELLOW_ZONE:
            zone = "GREEN"
        elif spent < RED_ZONE:
            zone = "YELLOW"
        elif spent < HARD_STOP:
            zone = "RED"
        else:
            zone = "HARD_STOP"

        return {"spent": round(spent, 4), "remaining": round(remaining, 4), "zone": zone}

    def reserve(self, amount: float, description: str = "", project_id: str = None) -> dict:
        s = self.status()

        if s["zone"] == "HARD_STOP":
            return {"approved": False, "reason": f"Hard stop reached (${HARD_STOP}). No further spend."}

        if s["spent"] + amount > HARD_STOP:
            headroom = round(HARD_STOP - s["spent"], 4)
            return {"approved": False, "reason": f"Would exceed hard stop. Headroom: ${headroom}"}

        if s["zone"] == "RED" and amount > 5.0:
            return {"approved": False, "reason": f"RED zone: only calls ≤$5 approved. Requested: ${amount:.2f}"}

        if s["zone"] == "YELLOW" and amount > 20.0:
            return {"approved": False, "reason": f"YELLOW zone: only calls ≤$20 approved. Requested: ${amount:.2f}"}

        return {"approved": True, "reason": "OK", "remaining_after": round(s["remaining"] - amount, 4)}

    def record(self, project_id: str, source: str, product: str,
               estimated_cost: float, actual_cost: float, description: str = "") -> None:
        with get_conn() as conn:
            conn.execute(
                """INSERT INTO budget_ledger
                   (timestamp, project_id, source, bright_data_product, description, estimated_cost, actual_cost)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (datetime.now(timezone.utc).isoformat(), project_id, source,
                 product, description, estimated_cost, actual_cost)
            )

    def report(self) -> dict:
        with get_conn() as conn:
            ledger = conn.execute(
                "SELECT * FROM budget_ledger ORDER BY timestamp"
            ).fetchall()
            by_project = conn.execute(
                "SELECT project_id, SUM(actual_cost) FROM budget_ledger GROUP BY project_id"
            ).fetchall()

        return {
            "status": self.status(),
            "by_project": {r[0]: round(r[1], 4) for r in by_project},
            "ledger": [dict(r) for r in ledger],
        }
