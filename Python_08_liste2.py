liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[0:2]
trois_derniers = liste[3:6]
milieu = liste[1:5]
premier_dernier = liste[0::5]


print(trois_derniers)


# correction

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[:3]
trois_derniers = liste[3:]
milieu = liste[1:-1]
premier_dernier = liste[::5]
