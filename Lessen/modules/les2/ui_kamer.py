class ui_kamer():
    laatste_positie = 1

    def __init__(self):
        self.positie = ui_kamer.laatste_positie
        ui_kamer.laatste_positie = ui_kamer.laatste_positie + 1

