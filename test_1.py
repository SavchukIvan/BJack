import tkinter as tk


class Game(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):

        toolbar = tk.Frame(bg='#015A7C', bd=2)
        toolbar.pack(side=tk.LEFT, fill=tk.Y)

        self.add_img = tk.PhotoImage(file="cards.png")
        btn_open_dialog = tk.Button(toolbar, text='Start Game', command=self.open_dialog, bg='#015A7C', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(pady=10)

        self.add_img_2 = tk.PhotoImage(file="settings.png")
        btn_open_settings = tk.Button(toolbar, text='Settings', command=self.open_dialog, bg='#015A7C', bd=0,
                                      compound=tk.TOP, image=self.add_img_2)
        btn_open_settings.pack(pady=10)

        self.add_img_3 = tk.PhotoImage(file="books.png")
        btn_open_rules = tk.Button(toolbar, text='Rules', command=self.open_dialog, bg='#015A7C', bd=0,
                                      compound=tk.TOP, image=self.add_img_3)
        btn_open_rules.pack(pady=10)

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('new game')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = Game(root)
    app.pack()
    background_image = tk.PhotoImage(file='wall.png')
    background_label = tk.Label(root, image=background_image)
    background_label.pack()
    root.title("Scalding BlackJack")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
