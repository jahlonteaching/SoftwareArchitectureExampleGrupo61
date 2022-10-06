from example.architecture.controller import Controller
from example.architecture.model import Model
from example.architecture.view import TkView

if __name__ == "__main__":
    controller = Controller(Model(), TkView())
    controller.start()
