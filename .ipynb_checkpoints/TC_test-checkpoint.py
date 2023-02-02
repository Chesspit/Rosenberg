import sqlite3
import pandas as pd

conn = sqlite3.connect(r'C:\Users\peter\Coding\Jupyter\tc_all_new.db')

c = conn.cursor()

c.execute("SELECT name FROM sqlite_schema WHERE type='table';")

print(c.fetchall())










conn.commit()
conn.close()
