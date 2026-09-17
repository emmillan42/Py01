class Plant:
    name: str
    height: float
    age_days: int
    growth_rate: float

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, "
              f"{self.age_days} days old")

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)


if __name__ == "__main__":

    rose = Plant()
    rose.name = "rose"
    rose.height = 25.0
    rose.age_days = 30
    rose.growth_rate = 0.8

    print("=== Garden Plant Growth ===")
    initial_height = rose.height
    rose.show()
    for day in range(7):
        print(f"=== Day {day + 1} ===")
        rose.grow()
        rose.age()
        rose.show()
    weekly_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {weekly_growth:.1f}cm")
