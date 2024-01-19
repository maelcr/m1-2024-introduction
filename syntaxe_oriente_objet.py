class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur

    def accelerer(self):
        print(self.marque + " accelere")


mavoiture = Voiture("Peugeot", "bleu")
madeuxiemevoiture = Voiture("Citroen", "rouge")

print(mavoiture.marque)
mavoiture.accelerer()
madeuxiemevoiture.accelerer()
