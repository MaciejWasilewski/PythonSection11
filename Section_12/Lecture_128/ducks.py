#lecture 138, 139
class Duck:
    def walk(self):
        print("walk like a duck")

    def swim(self):
        print("swim like a duck")

    def quack(self):
        print("quack like a duck")


class Penguin:
    def walk(self):
        print("walk like a penguin")

    def swim(self):
        print("swim like a penguin")

    def quack(self):
        print("quack like a penguin")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    p=Penguin()
    test_duck(donald)
    test_duck(p)
