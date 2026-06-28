import duckdb

# Path to the raw daily air-quality file (gitignored; lives locally)
csv_path = "data/air_quality/rama_2023_05.csv"

# DuckDB can query a CSV directly, no import step needed
con = duckdb.connect()

# 1. Peek: how many rows, and what do the first few look like?
print("First 5 rows:")
print(con.sql(f"SELECT * FROM read_csv('{csv_path}') LIMIT 5"))

print("Row count:")
print(con.sql(f"SELECT COUNT(*) AS n_days FROM read_csv('{csv_path}')"))

# 2. The first real number: average PM2.5 across the data available in the CSV. This is a simple SQL query, but it can be slow if the CSV is large, because DuckDB has to scan the entire file.
print("Average PM2.5 for the month:")
print(con.sql(f"""
    SELECT ROUND(AVG(PM25), 2) AS avg_pm25
    FROM read_csv('{csv_path}')
"""))

# 3. Average PM2.5 across may 2023 
print("Average PM2.5 for may 2023:")
print(con.sql(f"""
    SELECT ROUND(AVG(PM25), 2) AS avg_pm25
    FROM read_csv('{csv_path}')
    WHERE fecha >= '2023-05-01' AND fecha < '2023-06-01'
"""))