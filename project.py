
import tkinter as tk
import playsound as p


window = tk.Tk()
window.geometry=("2000x2000")


def playsound0(event):
    print(event)
    p.playsound("tmp_7901-951678082.mp3")
    
def playsound1(event):
    print(event)
    p.playsound("joel-oh-hell-nah.mp3") 

def playsound2(event):
    print(event)
    p.playsound("clash-royale-hog-rider.mp3")

def playsound3(event):
    print(event)
    p.playsound("vine-boom.mp3")

def playsound4(event):
    print(event)
    p.playsound("bye-bye-mewing_fMVssQz.mp3")


buttin1=tk.Button(window,text="DESPAWN",anchor="center")
buttin1.bind("<Button-1>",playsound0)
buttin2=tk.Button(window,text="NAH",anchor="center")
buttin2.bind("<Button-1>",playsound1)
buttin3=tk.Button(window,text="CLASH",anchor="center")
buttin3.bind("<Button-1>",playsound2)
buttin4=tk.Button(window,text="VINE",anchor="center")
buttin4.bind("<Button-1>",playsound3)
buttin5=tk.Button(window,text="BYE BYE",anchor="center")
buttin5.bind("<Button-1>",playsound4)

buttin1.grid(row=0,column=0)
buttin2.grid(row=1,column=1)
buttin3.grid(row=2,column=2)
buttin4.grid(row=3,column=3)
buttin5.grid(row=4,column=4)
 
window.mainloop()