import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv("mod1_graph.csv")
data2 = pd.read_csv("mod2_graph.csv")

shift_value = 17.5
data1["Interval start"] = data1["Interval start"] + shift_value

fig, ax = plt.subplots()

ax.plot(data1["Interval start"], data1["Tous les paquets"], label="modification 1 utilisateur")
ax.plot(data2["Interval start"], data2["Tous les paquets"], label="modification 2 utilisateur")

plt.legend(fontsize=10, loc='upper right')

plt.xlabel("temps")
plt.ylabel("paquets/500ms")

left_limit = 32
right_limit = 38

ax.set_xlim(left=left_limit, right=right_limit)

plt.show()
