from vuodet import nykyinen_vuosi


class Henkilö:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

    def ikä(self):
        return nykyinen_vuosi() - self.syntymävuosi

    def tiedot(self, lempiväri="musta"):
        print("Moikka,", self.nimi)
        print("Ai, olet", self.ikä(), "vuotta vanha.")
        print("Lempivärisi on siis", lempiväri)
        return self.syntymävuosi

    def __repr__(self):
        return "<Henkilö: " + self.nimi + ">"