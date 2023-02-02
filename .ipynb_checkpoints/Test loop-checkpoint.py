import sqlite3
import pandas as pd

conn = sqlite3.connect(r'C:\Users\peter\Coding\Jupyter\tc_all_new.db')

c = conn.cursor()

res = c.execute("SELECT name FROM sqlite_schema WHERE type='table';")
tab = []
for table in res.fetchall():
    u=str(table)[2:-3]
    tab.append(u)
tab = tab[1:]
# print('tab:', tab)

queryset = []

for t in tab:
    query = "SELECT COUNT(time) FROM " + t + " WHERE vfr11 == 1440"
    queryset.append(query)

print(queryset)

c. execute(queryset[1])
result = c.fetchone()
print("huhu:", result)

for q in queryset:
    c. execute(q)
    result = c.fetchone()
    print(result)
    



