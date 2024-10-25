import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


if __name__ == '__main__':
    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)  # Arvotaan huippunopeus
        auto = Auto(rekisteritunnus, huippunopeus)
        autot.append(auto)

    kilpailu_käynnissä = True
    while kilpailu_käynnissä:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:
                kilpailu_käynnissä = False
                break

    print(f"{'Rekisteritunnus':<15} {'Huippunopeus (km/h)':<20} {'Nopeus (km/h)':<15} {'Kuljettu matka (km)':<20}")
    print("=" * 70)
    for auto in autot:
        print(f"{auto.rekisteritunnus:<15} {auto.huippunopeus:<20} {auto.nopeus:<15} {auto.kuljettu_matka:<20.1f}")
