# class Bird():
#    def __init__(self, name):
#        self.name = name

#    def fly(self):
#        print(f"{self.name} is flying")

# class Ping(Bird):
#    pass

# p = Ping("Sarah")
# p.fly()


class Bird():
    def fly(self):
        print("Эта птица летает")


class Duck(Bird):
    def fly(self):
        print("Эта утка летает быстро")


def fly_in_the_sky(animal):
    animal.fly()


b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)


