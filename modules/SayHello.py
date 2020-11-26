class SayHello:

    def __init__(self, name="World"):
        self.name = name

    def say(self):
        print(f'Hello {self.name}')


if __name__ == "__main__":
    app = SayHello()
    app.say()
    app = SayHello("hoge")
