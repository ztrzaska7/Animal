class Animal:
    def __init__(self, name, hunger=1, boredom=1):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.activities_count = 0

    def feed(self):
        self.hunger += 1
        self.activities_count += 1
        if self.activities_count % 4 == 0:
            self.hunger -= 1
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        self.boredom += 1
        self.activities_count += 1
        if self.activities_count % 4 == 0:
            self.boredom -= 1
        if self.boredom < 0:
            self.boredom = 0

    def observe(self):
        print(f"Animal name: {self.name} - Hunger: {self.hunger}, Boredom: {self.boredom}")


animal=Animal("Cat")
animal.feed()
animal.play()
animal.feed()
animal.feed()
animal.feed()
animal.feed()
animal.observe()

