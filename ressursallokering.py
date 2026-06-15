import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Uke": ["Uke 1", "Uke 2", "Uke 3", "Uke 4"],
    "Tilgjengelig kapasitet": [500, 500, 450, 500],
    "Samlet prosjektbehov": [430, 620, 390, 510]
}

df = pd.DataFrame(data)

df["Ressursutnyttelse (%)"] = (
    df["Samlet prosjektbehov"] / df["Tilgjengelig kapasitet"] * 100
).round(1)

df["Status"] = df.apply(
    lambda row: "Forsinkelsesrisiko"
    if row["Samlet prosjektbehov"] > row["Tilgjengelig kapasitet"]
    else "OK",
    axis=1
)

print(df)

plt.figure(figsize=(8, 5))
plt.plot(df["Uke"], df["Tilgjengelig kapasitet"], marker="o", label="Tilgjengelig kapasitet")
plt.plot(df["Uke"], df["Samlet prosjektbehov"], marker="o", label="Samlet prosjektbehov")
plt.xlabel("Periode")
plt.ylabel("Engineering-timer")
plt.title("Kapasitet og prosjektbehov per uke")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("kapasitet_vs_behov.png")
plt.show()
kapasitet = 500

prosjekter = {
    "A": 250,
    "B": 180,
    "C": 150
}

gjenstaende = kapasitet

for navn, behov in prosjekter.items():
    tildelt = min(behov, gjenstaende)
    gjenstaende -= tildelt

    print(
        f"Prosjekt {navn}: "
        f"Behov={behov}, "
        f"Tildelt={tildelt}"
    )

print(f"Ubrukt kapasitet: {gjenstaende}")