import sqlite3
import pandas as pd

def main():
    conn = sqlite3.connect('realwork.db')
    
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print("Tables:", tables)
    
    if ('projects',) in tables:
        total = conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
        print(f"Total projects: {total}")
        
    if ('red_flags',) in tables:
        flagged = conn.execute("SELECT COUNT(DISTINCT project_id) FROM red_flags").fetchone()[0]
        print(f"Total flagged: {flagged}")
        
    if ('rankings',) in tables:
        ranked = conn.execute("SELECT COUNT(*) FROM rankings").fetchone()[0]
        print(f"Total ranked: {ranked}")

if __name__ == '__main__':
    main()
