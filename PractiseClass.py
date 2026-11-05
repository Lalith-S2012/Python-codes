class livingbeings():
    def __init__(self, breathing, eating):
        self.breathing = breathing
        self.eating = eating

    def organs(self):
        print("We breathe through", self.breathing)
        print("We eat through", self.eating)
class humans(livingbeings):
    def __init__(self, drinking, breathing, eating):
        self.drinking = drinking
        super()()
    def organ(self):
        print("We drink through", self.drinking)

ob1 = humans("Lungs", "Mouth", "Throat")

    
