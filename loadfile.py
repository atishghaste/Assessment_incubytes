import psycopg2 as pg
import pandas as pd

conn = pg.connect(database="postgres", user="postgres", password="12345", host="127.0.0.1", port="5432")

df = pd.read_sql_query('select * from patients',con=conn)

print(df)

ans = df.loc[df['country'] == "IND"]
print(ans)