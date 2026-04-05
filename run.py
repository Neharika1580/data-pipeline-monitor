import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

engine = create_engine('sqlite:///logs.db')

url = "https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=temperature_2m&timezone=America/New_York"
df = pd.DataFrame(requests.get(url).json()['hourly'])

issues = []
if len(df) < 160 or len(df) > 176:
    issues.append(f"Row count abnormal: {len(df)} (expected ~168)")
if df['temperature_2m'].isnull().sum() > 10:
    issues.append(f"Too many nulls: {df['temperature_2m'].isnull().sum()}")
if df['time'].duplicated().sum() > 0:
    issues.append(f"Duplicates: {df['time'].duplicated().sum()}")

log = pd.DataFrame([{
    'run_time': datetime.now(),
    'rows': len(df),
    'issues': ', '.join(issues) if issues else 'None',
    'status': 'FAIL' if issues else 'PASS'
}])
log.to_sql('logs', engine, if_exists='append', index=False)

df.to_csv(f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", index=False)

print("="*40)
print(f"Rows: {len(df)}")
print(f"Issues: {len(issues)}")
if issues:
    for i in issues:
        print(f"  - {i}")
print(f"Status: {'FAIL' if issues else 'PASS'}")
print(f"Saved: data_*.csv and logs.db")
print("="*40)