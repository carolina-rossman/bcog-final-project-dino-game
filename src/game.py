import tkinter as tk 
import FinalProject_PracticeCode

class Display(): 
    def __init__(self, root): 
        pass 
        self.init_window()
        # load scrolling background from other .py
    
    def load_dino(self): 
        self.dino = tk.PhotoImage(file = "../stimuli/dino.png")

    def create_powerups(self): 
        pass
    def create_powerdowns(self):
        pass

    def init_window(self): 
        pass
    def avoid_obstacles(self): 
        pass
        # load obstacles 




def main(): 
     my_display = Display()
     my_display.root.mainloop() 

if __name__ == "__main__":
    main()