import sqlite3
import pandas as pd

# Connect to your logs database
conn = sqlite3.connect('logs.db')

# Read the logs table
df = pd.read_sql('SELECT * FROM logs', conn)

# Export to CSV
df.to_csv('pipeline_logs.csv', index=False)

print(f"Exported {len(df)} rows to pipeline_logs.csv")
print("Columns:", list(df.columns))