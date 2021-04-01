import Model
import View
import GetPixels

class Controller:
    def __init__(self, ):
        #self.process = GetPixels.getPixels(self)
        self.model = Model.Model(self)
        self.view = View.View(self)

def main():
    c = Controller()

if __name__ == '__main__':
    quit(main())