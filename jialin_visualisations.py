import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")


# age vs sleep quality
age_avg = (
    df.groupby("age")["sleep_quality_score"]
    .mean()
)

fig1, ax1 = plt.subplots()

ax1.plot(
    age_avg.index,
    age_avg.values,
    marker = "."
)

ax1.set_title("Average Sleep Quality by Age")
ax1.set_xlabel("Age")
ax1.set_ylabel("Average Sleep Quality Score")


fig1.savefig("age_vs_sleep_quality.png")

# gender vs felt rested
rested_avg = (df.groupby("gender")["felt_rested"].mean())

fig2, ax2 = plt.subplots()

ax2.bar(
    rested_avg.index,
    rested_avg.values
)

ax2.set_title("Proportion Feeling Rested by Gender")
ax2.set_xlabel("Gender")
ax2.set_ylabel("Proportion Feeling Rested")


fig2.savefig("gender_vs_felt_rested.png")



# day type vs sleep duration
day_sleep = (
    df.groupby("day_type")["sleep_duration_hrs"]
    .mean()
)

fig7, ax7 = plt.subplots()

ax7.bar(
    day_sleep.index,
    day_sleep.values
)

ax7.set_title("Average Sleep Duration by Day Type")
ax7.set_xlabel("Day Type")
ax7.set_ylabel("Average Sleep Duration (Hours)")

fig7.savefig("day_type_vs_sleep_duration.png")
