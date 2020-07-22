from random import randint
class Die():
    def __init__(self):
        self.sides=6

    def roll_die(self,i):
        self.sides=randint(1,i)
        print(f"筛子数：{self.sides}")

die1=Die()
for i in range(10):
    die1.roll_die(10)

