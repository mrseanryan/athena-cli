from datetime import datetime
import sys
import matplotlib.pyplot as plt
import pandas as pd

CHARTS_DIR="../../charts/"

DASHBOARD = sys.argv[1]

jsonFs1 = f"../../data/{DASHBOARD}/clicks-count-per-month.json"
print("Loading JSON in \"{0:s}\"".format(jsonFs1))
data1 = pd.read_json(jsonFs1)

normalized_data = pd.json_normalize(data1['data'])

# convert to numbers
normalized_data['clicks_int'] = normalized_data['Clicks'].astype(int)

# drop the current month, which is partial:
currentDate = datetime.now()
this_month = currentDate.strftime("%Y") + "-" + currentDate.strftime("%m")
print("this_month:", this_month)
normalized_data = normalized_data[normalized_data["year_and_month"] != this_month]

print(normalized_data)

# === BPs per month ===
## unstack, so 1 series for each version
df_BPs_unstacked = normalized_data.groupby(['year_and_month', 'version'])['clicks_int'].sum().unstack()
print(df_BPs_unstacked)

# === PLOT BPs ===
# = stacked bar chart
fig, ax = plt.subplots(figsize=(15,7))
ax.set_title("Clicks by Version")
ax.set_xlabel('Year and Month')
ax.set_ylabel('Clicks by version')

df_BPs_unstacked.plot(ax=ax, colormap='tab20b', kind='bar', stacked=True)
pngFs1 = CHARTS_DIR + f"{DASHBOARD}-clicks-count-per-month.png"
print("{0:s} (chart as image)".format(pngFs1))
fig.savefig(pngFs1,bbox_inches="tight")
