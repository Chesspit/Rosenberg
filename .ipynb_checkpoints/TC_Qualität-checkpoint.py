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
print('tab:', tab)




# df1 = pd.read_sql_query("SELECT * FROM tcdata_CH_0084_01", conn)
# print(df1.describe())

# print('------')


query = """
    SELECT * FROM tcdata_CH_0084_01
    WHERE vfr11 == 1440
"""
df2 = pd.read_sql_query(query, conn)
print(df2.head())

# query = """
#     SELECT tcdata_CH_0084_01.time, tcdata_CH_0084_01.vfr11 as flow1, ROUND(tcdata_CH_0084_01.s12, 1) as speed1
# FROM "tcdata_CH_0084_01"
# WHERE tcdata_CH_0084_01.time BETWEEN '2021-06-23 17:00:00+02:00' AND '2021-06-23 17:07:00+02:00'
# """
# df1 = pd.read_sql_query(query, conn)
# print(df1.head())


# c.execute('''SELECT tcdata_CH_0084_01.time, tcdata_CH_0084_01.vfr11 as flow1, ROUND(tcdata_CH_0084_01.s12, 1) as speed1
# FROM "tcdata_CH_0084_01"
# WHERE tcdata_CH_0084_01.time BETWEEN '2021-06-23 17:00:00+02:00' AND '2021-06-23 17:07:00+02:00' ''')
# result = c.fetchmany(8)
# print(result)


query = """
    SELECT 
    COUNT(DISTINCT time)
    FROM "tcdata_CH_0084_01"
"""
df1 = pd.read_sql_query(query, conn)
print(df1.head())


c.execute('''SELECT 
*
FROM "tcdata_CH_0084_01"
 ''')
result = c.fetchmany(8)
print(result)
# Man kann alternativ so in einen DF speichern
df = pd.DataFrame(c.fetchall())
print("huhu:", df)
# muss dann aber ggf. noch die Column names explizit angeb

query = """
    SELECT
    COUNT(time)
    FROM "tcdata_CH_0084_01"
"""
df1 = pd.read_sql_query(query, conn)
print(df1.head())


conn.commit()
conn.close()
