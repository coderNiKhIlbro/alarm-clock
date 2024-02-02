 
from tkinter import *

root=Tk()
notify_widget=Toplevel()
screenh=root.winfo_screenheight()
screenw=root.winfo_screenwidth()
geostr = f"280x200+{screenw-300}+{screenh-300}"
notify_widget.geometry(geostr)
notify_widget.title("Alarm")


root.mainloop()