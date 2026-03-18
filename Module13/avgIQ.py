import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avgIQpercountry.csv')
print(df.info())

# five_rows = df.head()
# print(five_rows)
#
# country = df["Country"]
# print(country)

subset = df[["Country", "Average IQ"]]
print(subset)

filtered_df = subset[subset["Average IQ"] > 100]
filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)
print(filtered_df)

# null_mask = df.isnull()
# null_count = null_mask.sum()
# print(null_count)
#
# df.dropna(inplace=True)
# print(df.info())
#
# duplicate_count = df.duplicated().sum()
# print(duplicate_count)

# average_iq_by_continent = df.groupby('Continent')['Average IQ'].mean()
# print(average_iq_by_continent)
#
# sorted_average_iq_per_continent = average_iq_by_continent.sort_values(ascending=False)
# print(sorted_average_iq_per_continent)

# ---------------------Bar Chart--------------------------------

plt.figure(figsize=(14,8))
bars = plt.bar(filtered_df["Country"], filtered_df["Average IQ"], color="skyblue")

plt.title("Average IQ by Country where IQ is over 100", fontsize=16)
plt.xlabel("Country", fontsize=14)
plt.ylabel("Average IQ", fontsize=14)

plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)

plt.grid(axis="y", linestyle="--", alpha=0.87)

plt.bar_label(bars, fmt="%.2f", fontsize=10, color="black")

plt.tight_layout()
plt.show()

# ----------------------Line Plot---------------------------

average_iq_by_continent = df.groupby('Continent')['Average IQ'].mean()
print(average_iq_by_continent)

plt.figure(figsize=(10, 6))
average_iq_by_continent.plot(kind="line", marker="o", color="skyblue")

plt.title("Average IQ by Continent", fontsize=16)
plt.xlabel("Continent", fontsize=14)
plt.ylabel("Average IQ", fontsize=14)

plt.grid(axis="both", linestyle="--", alpha=0.7)

plt.show()

# --------------------Scatter Plot---------------------------

plt.figure(figsize=(10, 6))
plt.scatter(df['Mean years of schooling - 2021'], df['Average IQ'], color="skyblue", alpha=0.7)

plt.title("Scatter Plot of Mean Years of Schooling vs Average IQ", fontsize=16)

plt.xlabel("Mean years of schooling - 2021", fontsize=14)
plt.ylabel("Average IQ", fontsize=14)

plt.grid(True, linestyle="--", alpha=0.7)

plt.show()

#----------------------Pie Chart------------------------------

nobel_prizes_by_continent = df.groupby('Continent')['Nobel Prices'].sum()
no_of_continents = nobel_prizes_by_continent.count()
print(no_of_continents)
colors = ["gold", "lightcoral", "yellow", "thistle", "orange", "lightskyblue", "aquamarine", "burlywood"]

plt.figure(figsize=(10, 10))

nobel_prizes_by_continent.plot(kind='pie', color=colors, autopct='%1.1f%%')

plt.title("Distribution of Noble Prizes by Continent", fontsize=16)

plt.axis('equal')

plt.ylabel('')

plt.tight_layout()

plt.show()

# ---------------------Seaborn---------------------------
