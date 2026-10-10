import pandas as pd

source_df = pd.read_csv("split_dataset_4.csv")

df = source_df[[
    "person_id",
    "sleep_duration_hrs",
    "sleep_quality_score",
    "rem_percentage",
    "deep_sleep_percentage",
    "sleep_latency_mins",
    "wake_episodes_per_night",
    "cognitive_performance_score",
    "sleep_disorder_risk",
    "felt_rested",

    "age",
    "gender",
    "country",
    "room_temperature_celsius",
    "season",
    "day_type"
]]

# check for missing values
df.isnull()
print(df.isnull().sum())

# remove rows with missing values
df = df.dropna()

# check for and remove duplicate entries
df.duplicated()
print(df.duplicated().sum())
df = df.drop_duplicates()

# check for impossible values
print(df.describe())

# convert cleaned data into csv 
df.to_csv("cleaned_data.csv", index=False)