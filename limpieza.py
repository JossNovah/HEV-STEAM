import pandas as pd

RUTA = r"C:\Users\Hp\Downloads\steam-200k.csv"

df = pd.read_csv(RUTA, header=None,
                 names=["user_id", "game_name", "behavior", "value", "extra"])
df = df.drop(columns=["extra"])
df = df.dropna(subset=["user_id", "game_name", "behavior"])
df["game_name"] = df["game_name"].str.strip()
df["behavior"]  = df["behavior"].str.strip().str.title()
df = df.drop_duplicates()
df.to_csv(r"C:\Users\Hp\Downloads\steam_limpio.csv", index=False)
print("Limpieza lista. Filas:", len(df))