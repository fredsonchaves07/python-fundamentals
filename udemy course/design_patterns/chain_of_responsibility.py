from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self.sucessor: Handler

    @abstractmethod
    def handler(self, letter):
        pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler):
        self.letters = ["A", "B", "C"]
        self.sucessor = sucessor

    def handler(self, letter):
        if letter in self.letters:
            return f"handler_abc: {letter}"
        return self.sucessor.handler(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler):
        self.letters = ["D", "E", "F"]
        self.sucessor = sucessor

    def handler(self, letter):
        if letter in self.letters:
            return f"handler_def: {letter}"
        return self.sucessor.handler(letter)


class HandlerUnsolved(Handler):
    def handler(self, letter):
        return "handler_unsolved"


if __name__ == "__main__":
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handler("F"))
