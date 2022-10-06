import uuid

from example.architecture.model import Model
from example.architectureabstractions.abtractions import View


class Controller:

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_generate_uuid(self):
        self.model.uuid.append(uuid.uuid4())
        self.view.append_to_list(self.model.uuid[-1])

    def handle_click_clear_list(self):
        self.model.uuid.clear()
        self.view.clear_list()
