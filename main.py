# main.py
import pandas as pd
import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(URL)

print(df.describe())

plt.scatter(df["total_bill"], df["tip"])
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Tips vs. Total Bill")
plt.savefig("plot.png", dpi=300)