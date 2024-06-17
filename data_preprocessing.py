import pandas as pd

df = pd.read_csv("./data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.loc[df.TotalCharges.isna(), "TotalCharges"] = df.loc[df.TotalCharges.isna(), "MonthlyCharges"]

# drop CustomerID
del df["customerID"]

# drop duplicates
df = df.drop_duplicates()

df.to_csv("./data/processed/churn_dataset.csv", index=False)
