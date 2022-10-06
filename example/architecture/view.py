import tkinter as tk

from example.architectureabstractions.abtractions import View


class TkView(View):
    def setup(self, controller):
        # Configurar tkinter
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("UUIDGen")

        # Crear la GUI
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.label = tk.Label(self.frame, text="Result:")
        self.label.pack()
        self.list = tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH, expand=1)
        self.generate_uuid_button = tk.Button(self.frame,
                                              text="Generate UUID",
                                              command=controller.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_list_button = tk.Button(self.frame,
                                           text="Clear list",
                                           command=controller.handle_click_clear_list)
        self.clear_list_button.pack()

    def append_to_list(self, item):
        self.list.insert(tk.END, item)

    def clear_list(self):
        self.list.delete(0, tk.END)

    def start_main_loop(self):
        self.root.mainloop()
