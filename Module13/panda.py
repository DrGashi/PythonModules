import pandas as pd

data = {"Name": ['Gerti', 'Dreni', "Deoni"],
        "Age": [12, 17, 15],
        "City": ["Prishtina", "Prizren", "Prishtina"]
        }

df = pd.DataFrame(data)
print(df)