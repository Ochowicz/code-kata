from preloaded import Animal


class Cat(Animal):
    def __init__(slef, name):
        super().__init__(name)

    def speak(self):
        return f'{self.name} meows.'