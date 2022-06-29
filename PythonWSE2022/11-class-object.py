class Samochod:
    typ = "samochód osobowy"
    def __init__(self, marka, model, vin, paliwo, moc, rok):
        self.marka = marka
        self.model = model
        self.vin = vin
        self.paliwo = paliwo
        self.moc = moc
        self.rok = rok
    def wypiszCechy(self):
        print(self.marka, self.model, "\tTyp:", self.typ)
        print("VIN: ", self.vin, "\tRok produkcji: ", self.rok)
        print("Rodzaj paliwa:", self.paliwo, "\t\tMoc:", self.moc, "KM")
    def setMarka(self, marka):
        self.marka = marka
    def getMarka(self):
        print(self.marka)

Opel1 = Samochod("Opel", "Isignia", "WO0001233XXDDD41", "ON", 210, 2020)
Opel1.wypiszCechy()

Fiat1 = Samochod("Fiat", "500", "WXDDD00004333450", "Pb", 85, 2021)
Fiat1.wypiszCechy()