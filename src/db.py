import sqlite3
import os
from pathlib import Path

DB_PATH = os.getenv("DB_PATH", "realwork.db")


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_conn() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS projects (
                project_id      TEXT PRIMARY KEY,
                project_name    TEXT,
                recipient_name  TEXT,
                recipient_type  TEXT,
                award_amount    REAL,
                award_date      TEXT,
                category        TEXT,
                description     TEXT,
                location        TEXT,
                funding_source  TEXT,
                contract_type   TEXT,
                raw_record      TEXT
            );

            CREATE TABLE IF NOT EXISTS red_flags (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id      TEXT NOT NULL,
                flag            TEXT NOT NULL,
                severity        TEXT NOT NULL,
                reasoning       TEXT,
                FOREIGN KEY (project_id) REFERENCES projects(project_id)
            );

            CREATE TABLE IF NOT EXISTS rankings (
                rank                        INTEGER,
                project_id                  TEXT PRIMARY KEY,
                fraud_probability           TEXT,
                investigation_feasibility   TEXT,
                dollar_magnitude            REAL,
                composite_score             REAL,
                investigation_brief         TEXT,
                suggested_sources           TEXT,
                FOREIGN KEY (project_id) REFERENCES projects(project_id)
            );

            CREATE TABLE IF NOT EXISTS budget_ledger (
                id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp           TEXT NOT NULL,
                project_id          TEXT,
                source              TEXT NOT NULL,
                bright_data_product TEXT NOT NULL,
                description         TEXT,
                estimated_cost      REAL,
                actual_cost         REAL
            );

            CREATE TABLE IF NOT EXISTS evidence (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id      TEXT NOT NULL,
                source          TEXT NOT NULL,
                url_scraped     TEXT,
                timestamp       TEXT NOT NULL,
                actual_cost     REAL,
                raw_data        TEXT,
                extracted       TEXT,
                finding         TEXT,
                supports_fraud  INTEGER,
                FOREIGN KEY (project_id) REFERENCES projects(project_id)
            );

            CREATE TABLE IF NOT EXISTS investigation_log (
                project_id      TEXT PRIMARY KEY,
                status          TEXT NOT NULL DEFAULT 'PENDING',
                conclusion      TEXT,
                confidence      TEXT,
                rationale       TEXT,
                total_cost      REAL DEFAULT 0,
                updated_at      TEXT,
                FOREIGN KEY (project_id) REFERENCES projects(project_id)
            );
        """)
