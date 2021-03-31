import Model
import View

class Controller:
    def __init__(self, ):
        self.model = Model.Model(self)
        self.view = View.View(self)

def main():
    c = Controller()

if __name__ == '__main__':
    quit(main())