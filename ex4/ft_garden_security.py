class Plant:

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        if not self.set_height(height, False):
            self._height = 0.0
            print("Attribute was initialized with default value (0.0 cm)")
        if not self.set_age(age_days, False):
            self._age_days = 0
            print("Attribute was initialized with default value (0 days)")
        if not self.set_growth_rate(growth_rate, False):
            self._growth_rate = 0.0
            print("Attribute was initialized with default value (0.0 cm/day)")
        print("Plant created:", end=" ")
        self.show()

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float, show_message: bool = True) -> bool:
        if height < 0:
            print(f"{self.name.capitalize()}: Error, Invalid Entry. "
                  "Height can't be negative! Value must be a positive number")
            if show_message:
                print("Height update rejected")
            return False
        self._height = height
        if show_message:
            print(f"Height updated: {self.get_height()}cm")
        return True

    def get_age(self) -> int:
        return self._age_days

    def set_age(self, age_days: int, show_message: bool = True) -> bool:
        if age_days < 0:
            print(f"{self.name.capitalize()}: Error, Invalid Entry. "
                  "Age can't be negative! Value must be a positive number")
            if show_message:
                print("Age update rejected")
            return False
        self._age_days = age_days
        if show_message:
            print(f"Age updated: {self.get_age()} days")
        return True

    def get_growth_rate(self) -> float:
        return self._growth_rate

    def set_growth_rate(self, growth_rate: float,
                        show_message: bool = True) -> bool:
        if growth_rate < 0:
            print(f"{self.name.capitalize()}: Error, Invalid Entry. "
                  "Growth Rate can't be negative! Value must be positive")
            if show_message:
                print("Growth Rate update rejected")
            return False
        self._growth_rate = growth_rate
        if show_message:
            print(f"Grow Rate updated: {self.get_growth_rate()} cm/day")
        return True

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def grow(self) -> None:
        self.set_height(round(self.get_height() + self.get_growth_rate(), 1))

    def current_state(self) -> None:
        print("Current state:", end=" ")
        self.show()


if __name__ == "__main__":

    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10, 0.8)
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-10)
    print()

    rose.current_state()
    print()

    oak = Plant("oak", 200.0, 365, 0.4)
    print()
    cactus = Plant("cactus", 5.0, 90, -0.1)
    print()
    sunflower = Plant("sunflower", 80.0, -45, 0.6)
    print()
    fern = Plant("fern", -15.0, 120, 0.2)
    print()

    plants = [oak, cactus, sunflower, fern]
    for plant in plants:
        print("Created:", end=" ")
        plant.show()
