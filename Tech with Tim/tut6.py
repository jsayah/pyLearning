class _Private:# single underscore denotes private class
    def __init__(self, name) -> None:
        self.name = name


class NotPrivate:
    def __init__(self, name) -> None:
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("Hello")

    def display(self):
        print("Hi")