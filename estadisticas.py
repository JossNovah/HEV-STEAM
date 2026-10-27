import pandas as pd

df = pd.read_csv(r"C:\Users\Hp\Downloads\steam_limpio.csv")
compras = df[df["behavior"] == "Purchase"]
juegos  = df[df["behavior"] == "Play"]["value"]

print("Media:", round(juegos.mean(), 2))
print("Mediana:", round(juegos.median(), 2))
print("Moda (rango):", juegos.round(0).mode().iloc[0])
print("Desv. estándar:", round(juegos.std(), 2))
print("Máximo:", juegos.max())
print("Unidades vendidas:", len(compras))
print("Usuarios únicos:", df["user_id"].nunique())
print("Juegos únicos:", df["game_name"].nunique())
print(compras["game_name"].value_counts().head(10))