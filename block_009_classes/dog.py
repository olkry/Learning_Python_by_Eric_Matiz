class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        print(f'{self.name} rolled over.')



my_dog = Dog("Charly", 12)

print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()