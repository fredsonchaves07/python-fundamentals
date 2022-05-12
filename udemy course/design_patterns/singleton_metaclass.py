class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.theme = "Dark theme"
        self.font = "18px"


if __name__ == "__main__":
    app1 = AppSettings()
    app1.theme = "Ligth Theme"
    app2 = AppSettings()

    print(app1.theme)
    print(app2.theme)
