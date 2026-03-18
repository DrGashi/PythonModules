import pandas as pd
import plotly.express as pl

df = pd.read_csv("iq_dataset.csv")

print(df.head())
print(df.columns)

avg_iq = df.groupby("country")["iq"].mean().reset_index()

avg_iq = avg_iq.sort_values(by="iq", ascending=False)

print(avg_iq)

iq_map = pl.choropleth(
    avg_iq,
    locations="country",
    locationmode="country names",
    color="iq",
    title="Average IQ by Country (World Map)",
    color_continuous_scale="Viridis"
)

iq_map.show()