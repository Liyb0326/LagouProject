import yaml


class Person:
    name: str = "lucy"
    age: int = 20
    __money: int = 10000


    def eat(self):
        print(f"{self.name} is eating")

    def running(self):
        print(f"{self.name} is running")


class FunnyMan(Person):
    def fun(self):
        print(f"{self.name} is funny boy")


p = Person()
print(p.name)
p.eat()
p.running()
print(f"{p._Person__money} is too much")

f = FunnyMan()
f.fun()
print(dir(p))
print()

yaml.s

