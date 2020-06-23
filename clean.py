import pandas as pd
from pathlib import Path

root = Path.cwd()
data_path = root / "data" / "work_requests.csv"
wr_sample_path = root / "data" / "wr_sample.csv"

df_old = pd.read_csv(
    data_path, encoding="ISO-8859-1", parse_dates=["date_requested"], low_memory=False
)
print(df_old.dtypes)
df_new = df_old[["wr_id", "date_requested", "prob_type", "date_completed", "bl_id",]]
df_sample = df_new.iloc[0:300, :]
print(df_sample.shape)

df_sample.to_csv(wr_sample_path, index=False)
