import pandas as pd

prosjekter = pd.DataFrame({
    "Prosjekt": [
        "Offshore Wind",
        "Subsea LARS",
        "Buoy Pull-In",
        "A-Frame Cable Lay",
        "Offshore Gangway"
    ],

    "Prioritet": [
        "Kritisk",
        "Kritisk",
        "Høy",
        "Høy",
        "Medium"
    ],

    "Frist": [
        "2026-03-20",
        "2026-03-28",
        "2026-03-25",
        "2026-04-05",
        "2026-04-18"
    ],

    "Behov": [
        480,
        500,
        360,
        400,
        310
    ]
})

prioritet_score = {
    "Kritisk": 4,
    "Høy": 3,
    "Medium": 2,
    "Lav": 1
}

prosjekter["PrioritetScore"] = prosjekter["Prioritet"].map(prioritet_score)

prosjekter["Frist"] = pd.to_datetime(prosjekter["Frist"])

prosjekter = prosjekter.sort_values(
    by=["PrioritetScore", "Frist"],
    ascending=[False, True]
)

print("\nSEKVENSIERING\n")
print(prosjekter[["Prosjekt", "Prioritet", "Frist", "Behov"]])
print("\nRESSURSALLOKERING\n")

kapasitet = 1500

tildelt = []
mangler = []

for behov in prosjekter["Behov"]:

    if kapasitet >= behov:

        tildeling = behov

    else:

        tildeling = max(0, kapasitet)

    kapasitet = kapasitet - tildeling

    tildelt.append(tildeling)

    mangler.append(behov - tildeling)

prosjekter["Tildelt"] = tildelt
prosjekter["Mangler"] = mangler

print(
    prosjekter[
        [
            "Prosjekt",
            "Behov",
            "Tildelt",
            "Mangler"
        ]
    ]
)
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

plt.bar(
    prosjekter["Prosjekt"],
    prosjekter["Behov"],
    label="Behov"
)

plt.bar(
    prosjekter["Prosjekt"],
    prosjekter["Tildelt"],
    label="Tildelt"
)

plt.title("Behov vs tildelt kapasitet")
plt.ylabel("Engineeringtimer")
plt.xticks(rotation=45)

plt.legend()

plt.tight_layout()

plt.show()