class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"{self.rate_per_km}, {self.distance}, {self.fare}")


def main():
    # your program
    taxi1 = TaxiRide(2)
    taxi1.distance = 100
    taxi1.calculate_fare(taxi1.distance)
    taxi1.print_receipt()

    taxi2 = TaxiRide(3)
    taxi2.distance = 50
    taxi2.calculate_fare(taxi2.distance)
    taxi2.print_receipt()

if __name__ == "__main__":
    main()
