import tkinter as tk
import uuid


class UUIDGen:
    def __init__(self):
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
                                              command=self.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_list_button = tk.Button(self.frame,
                                           text="Clear list",
                                           command=self.handle_click_clear_list)
        self.clear_list_button.pack()

        # Inicializar la lista de uuid
        self.uuid = []

        # Iniciar el loop
        self.root.mainloop()

    def handle_click_generate_uuid(self):
        self.uuid.append(uuid.uuid4())
        self.list.insert(tk.END, self.uuid[-1])

    def handle_click_clear_list(self):
        self.uuid.clear()
        self.list.delete(0, tk.END)
