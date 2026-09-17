class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


if __name__ == "__main__":

    rose = Plant()
    rose.name = "rose"
    rose.height = 25
    rose.age = 30

    sunflower = Plant()
    sunflower.name = "sunflower"
    sunflower.height = 80
    sunflower.age = 45

    cactus = Plant()
    cactus.name = "cactus"
    cactus.height = 15
    cactus.age = 120

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
