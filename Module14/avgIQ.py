import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')
print(df.info())

five_rows = df.head()
print(five_rows)

country = df["Country"]
print(country)

subset = df[["Country", "Average IQ"]]
print(subset)

filtered_df = subset[subset["Average IQ"] > 100]
print(filtered_df)

null_mask = df.isnull()
null_count = null_mask.sum()
print(null_count)

df.dropna(inplace=True)
print(df.info())

duplicate_count = df.duplicated().sum()
print(duplicate_count)

average_iq_by_continent = df.groupby('Continent')['Average IQ'].mean()
print(average_iq_by_continent)

sorted_average_iq_per_continent = average_iq_by_continent.sort_values(ascending=False)
print(sorted_average_iq_per_continent)