import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")


rested_avg = (
    df.groupby("gender")["felt_rested"]
    .mean()
)


print(rested_avg)

day_sleep = (
    df.groupby("day_type")
    ["sleep_duration_hrs"]
    .mean()
)

print(day_sleep)