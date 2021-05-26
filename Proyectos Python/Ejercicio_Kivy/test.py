class One:
    def __init__(self):
        print("Uno")

class Two(One):
    def __init__(self):
        super().__init__()
        print("Dos")

Two()