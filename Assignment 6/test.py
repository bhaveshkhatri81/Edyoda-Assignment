class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name} has {self.coat_color} coat.")


class JackRussellTerrier(Dog):
    def special_skill(self):
        print(f"{self.name} can jump very high!")

    def play_fetch(self):
        print(f"{self.name} loves playing fetch!")


class Bulldog(Dog):
    def special_skill(self):
        print(f"{self.name} has a strong grip!")

    def snore(self):
        print(f"{self.name} is known to snore loudly.")


# Creating objects and using the functionalities
dog1 = JackRussellTerrier("Max", 3, "white and brown")
dog2 = Bulldog("Buddy", 5, "brindle")

dog1.description()
dog1.get_info()
dog1.special_skill()
dog1.play_fetch()

dog2.description()
dog2.get_info()
dog2.special_skill()
dog2.snore()
