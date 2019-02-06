from tkinter import * #from tkinter import Tk, Label, Button, StringVar, Frame, OptionMenu, Listbox
import os
from pyplayer import PyPlayer

class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        top_frame = Frame(master).pack(side = "top")
        bottom_frame = Frame(master).pack(side = "bottom")

        self.player = PyPlayer()

        #self.label_index = 0
        #self.label_text = StringVar()
        #self.label_text.set(self.LABEL_TEXT[self.label_index])
        #self.label = Label(master, textvariable=self.label_text)
        #self.label.bind("<Button-1>", self.cycle_label_text)
        #self.label.pack()
        #self.close_button = Button(top_frame, text="Close", command=master.quit)
        #self.close_button.pack(side = "right")

        #tkvar = StringVar(top_frame)

        # Dictionary with options
        #choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
        #tkvar.set('Pizza') # set the default option

        #self.popupMenu = OptionMenu(top_frame, tkvar, *choices)
        #self.popupMenu.pack()

        self.listbox = Listbox(top_frame)
        self.listbox.pack()
        tkvar = StringVar(top_frame)

        for file in os.listdir('./'):
            if '.mp3' in file or '.mp4' in file:
                self.listbox.insert(END, file)

        self.listbox.bind('<Double-Button-1>', self.test)

        self.play_btn = Button(bottom_frame , text="Play", command=self.play)
        self.play_btn.pack(side = "left")

        self.stop_btn = Button(bottom_frame , text="Stop", command=self.stop)
        self.stop_btn.pack(side = "left")

        self.pause_btn = Button(bottom_frame , text="Pause", command=self.pause)
        self.pause_btn.pack(side = "left")

        #self.play = Button(master, text="Play", command=self.printThis('stop'))
        #self.play.pack()

    def test(self, evt) -> None:
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item %d: "%s"' % (index, value))
        self.player.play_temp_song(value)

    def play(self):
        print('play')
        self.player.start_song_again()

    def pause(self):
        print('pause')
        self.player.pause_temp_song()

    def stop(self):
        print('stop')
        self.player.stop()

    def greet(self):
        print("Greetings!")

    def printThis(self, s: str) -> None:
        print(s)

    #def cycle_label_text(self, event):
        #self.label_index += 1
        #self.label_index %= len(self.LABEL_TEXT) # wrap around
        #self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = MyFirstGUI(root)


root.mainloop()
