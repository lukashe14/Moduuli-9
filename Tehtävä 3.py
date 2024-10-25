class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus

        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


if __name__=='__main__':
    auto = Auto("ABC-123", 142)

    auto.kiihdytä(60)

    auto.kuljettu_matka = 2000


    auto.kulje(1.5)

    print(f"Rekisteritunnus: {auto.rekisteritunnus}")
    print(f"Huippunopeus: {auto.huippunopeus} km/h")
    print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
    print(f"Kuljettu matka: {auto.kuljettu_matka} km")



