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

    def age(self, show_message: bool = True) -> None:
        self.set_age(self.get_age() + 1, show_message)

    def grow(self, show_message: bool = True) -> None:
        self.set_height(round(self.get_height() + self.get_growth_rate(), 1),
                        show_message)

    def current_state(self) -> None:
        print("Current state:", end=" ")
        self.show()


class Flower(Plant):

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, color: str) -> None:
        self.color = color
        self._bloomed = False
        super().__init__(name, height, age_days, growth_rate)

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self._bloomed = True


class Tree(Plant):

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, age_days, growth_rate)

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, harvest_season: str) -> None:
        self.harvest_season = harvest_season
        self.nutritional_value: float = 0
        super().__init__(name, height, age_days, growth_rate)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value:.0f}")

    def age(self, show_message: bool = True) -> None:
        super().age(show_message)
        self.nutritional_value += 0.5

    def grow(self, show_message: bool = True) -> None:
        super().grow(show_message)
        self.nutritional_value += 0.5


if __name__ == "__main__":

    rose = Flower("rose", 15.0, 10, 0.8, "red")
    oak = Tree("oak", 200.0, 365, 0.4, 5.0)
    tomato = Vegetable("tomato", 5.0, 10, 2.1, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()

    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato.show()

    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.age(False)
        tomato.grow(False)

    tomato.show()
