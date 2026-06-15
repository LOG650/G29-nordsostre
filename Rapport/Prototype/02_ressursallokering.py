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