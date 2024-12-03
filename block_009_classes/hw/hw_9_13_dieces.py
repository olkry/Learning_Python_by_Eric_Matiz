from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f'Выпало {randint(1, self.sides)}')

if __name__ == '__main__':
    die_6 = Die()
    die_10 = Die(10)
    die_20 = Die(20)

    die_20.roll_die()
    die_20.roll_die()
    die_20.roll_die()
    die_20.roll_die()
    die_20.roll_die()
    die_20.roll_die()
    die_20.roll_die()
    die_20.roll_die()
    die_20.roll_die()
    die_20.roll_die()




