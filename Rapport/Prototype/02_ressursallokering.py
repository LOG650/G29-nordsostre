import matplotlib.pyplot as plt

prosjekter = [
    "Offshore Wind",
    "Subsea LARS",
    "Buoy Pull-In",
    "A-Frame",
    "Gangway"
]

behov = [480, 500, 360, 400, 310]
tildelt = [480, 500, 360, 160, 0]

x = range(len(prosjekter))

plt.figure(figsize=(8,5))
plt.bar(x, behov, label="Behov")
plt.bar(x, tildelt, label="Tildelt")

plt.xticks(x, prosjekter, rotation=20)
plt.ylabel("Timer")
plt.title("Behov vs tildelt kapasitet")
plt.legend()

plt.tight_layout()
plt.savefig("kapasitet_vs_behov.png")
plt.show()
import matplotlib.pyplot as plt

prosjekter = ["Offshore Wind", "Subsea LARS", "Buoy Pull-In", "A-Frame", "Gangway"]
behov = [480, 500, 360, 400, 310]
tildelt = [480, 500, 360, 160, 0]

x = range(len(prosjekter))
bredde = 0.4

plt.figure(figsize=(9, 5))

plt.bar([i - bredde/2 for i in x], behov, width=bredde, label="Behov")
plt.bar([i + bredde/2 for i in x], tildelt, width=bredde, label="Tildelt")

plt.xticks(x, prosjekter, rotation=20)
plt.ylabel("Engineeringtimer")
plt.title("Figur 2: Ressursbehov vs tildelt kapasitet")
plt.legend()
plt.tight_layout()

plt.savefig("kapasitet_vs_behov.png")
plt.show()