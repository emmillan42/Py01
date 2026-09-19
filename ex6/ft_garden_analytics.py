class Plant:

    class _PlantStats:

        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self, name: str) -> None:
            print(f"[statistics for {name.capitalize()}]")
            print(f"Stats: {self._grow_count} grow, {self._age_count} age, "
                  f"{self._show_count} show")

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self._stats: Plant._PlantStats = Plant._PlantStats()
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
        self._stats.increment_show()
        print(f"{self.name.capitalize()}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")

    def age(self, days: int = 1, show_message: bool = True) -> None:
        self.set_age(self.get_age() + days, show_message)
        self._stats.increment_age()

    def grow(self, show_message: bool = True) -> None:
        self.set_height(round(self.get_height() + self.get_growth_rate(), 1),
                        show_message)
        self._stats.increment_grow()

    def current_state(self) -> None:
        print("Current state:", end=" ")
        self.show()

    def expose_display(self) -> None:
        self._stats.display(self.name)

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)


class Flower(Plant):

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def bloom(self, show_message: bool = True) -> None:
        if self._bloomed:
            return
        if show_message:
            print(f"[asking the {self.name} to bloom]")
        self._bloomed = True


class Seed(Flower):

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, age_days, growth_rate, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self, show_message: bool = True) -> None:
        if self._bloomed:
            return
        super().bloom(show_message)
        self._seeds = 42


class Tree(Plant):

    class _TreeStats(Plant._PlantStats):

        def __init__(self) -> None:
            super().__init__()
            self._produce_shade_count = 0

        def display(self, name: str) -> None:
            super().display(name)
            print(f" {self._produce_shade_count} shade")

        def increment_produce_shade(self) -> None:
            self._produce_shade_count += 1

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, age_days, growth_rate)
        self._stats: Tree._TreeStats = Tree._TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.get_height():.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")
        self._stats.increment_produce_shade()


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

    def age(self, days: int = 1, show_message: bool = True) -> None:
        super().age(days, show_message)
        self.nutritional_value += 0.5

    def grow(self, show_message: bool = True) -> None:
        super().grow(show_message)
        self.nutritional_value += 0.5


def display_stats(plant: Plant) -> None:
    plant.expose_display()


def main() -> None:

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, 8, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(False)
    rose.bloom(False)
    rose.show()
    display_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 0, 5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("sunflower", 80, 45, 0, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.set_growth_rate(30, False)
    sunflower.grow(False)
    sunflower.age(20, False)
    sunflower.bloom(False)
    sunflower.show()
    display_stats(sunflower)
    print()

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_stats(anonymous)


if __name__ == "__main__":
    main()
