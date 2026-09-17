class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, "
              f"{self.age_days} days old")

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)


if __name__ == "__main__":

    rose = Plant("rose", 25.0, 30, 0.8)
    oak = Plant("oak", 200.0, 365, 0.4)
    cactus = Plant("cactus", 5.0, 90, 0.1)
    sunflower = Plant("sunflower", 80.0, 45, 0.6)
    fern = Plant("fern", 15.0, 120, 0.2)

    plants = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", end=" ")
        plant.show()
