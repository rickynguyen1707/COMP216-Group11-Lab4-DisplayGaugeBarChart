import tkinter as tk
from math import pi, cos, sin


low_r = 0 # chart low range
hi_r = 100 # chart hi range
root = tk.Tk()
name_var=tk.IntVar()
name_var=1



class Meter(tk.Frame):
    def __init__(self, master=None, **kw):
        tk.Frame.__init__(self, master, **kw)

        self.meter = []
        self.angle = []
        self.temp = tk.IntVar(self, 0)
        self.var = tk.IntVar(self, 0)

        self.canvas = tk.Canvas(self, width=200, height=160,
                                borderwidth=2, relief='sunken',
                                bg='grey')
        self.scale = tk.Scale(self, orient='horizontal', from_=0, to=100, variable=self.var)
        self.label = tk.Label(root, text = 'Desired Temp', font=('calibre',10, 'bold'))
        self.entry = tk.Entry(root,textvariable=self.temp, font=('calibre',10,'normal'))
    

        for j, i in enumerate(range(0, 100, 5)):
            self.meter.append(self.canvas.create_line(1, 1, 10, 20,
                                                      fill='grey%i' % i,
                                                      width=3,
                                                      arrow='last'))
            self.angle.append(0)
            self.canvas.lower(self.meter[j])
            self.updateMeterLine(0.2, j)

        self.canvas.create_arc(10, 40, 190, 220, extent=108, start=36,
                               style='arc', outline='black')
        self.canvas.create_text(49,15,font="Times 20 italic bold", text="G a", fill='red')
        self.canvas.create_text(92,15,font="Times 20 italic bold", text="s o", fill='black')
        self.canvas.create_text(123,15,font="Times 20 italic bold", text="l i", fill='black')
        self.canvas.create_text(158,15,font="Times 20 italic bold", text="n e", fill='green')
        self.canvas.create_text(40,78,font="Times 12 bold", text=low_r, fill='red')
        self.canvas.create_text(152,78,font="Times 12 bold", text=hi_r)

        self.btn = tk.Button(root,text='Start',command=self.updateVariableFromEntry)

        self.canvas.pack(fill='both')
        self.label.pack()
        self.entry.pack()
        self.btn.pack()
    

        self.var.trace_add('write', self.updateMeter)
        self.updateMeterTimer()

    def updateMeterLine(self, a, l=0):
        """Draw a meter line (and recurse for lighter ones...)"""
        oldangle = self.angle[l]
        self.angle[l] = a
        x = 100 - 70 * cos(a * pi)
        y = 100 - 70 * sin(a * pi)
        self.canvas.coords(self.meter[l], 100, 100, x, y)
        l += 1
        if l < len(self.meter):
            self.updateMeterLine(oldangle, l)

    def updateMeter(self, name1, name2, op):
        """Convert variable to angle on trace"""
        mini = self.scale.cget('from')
        maxi = self.scale.cget('to')
        pos = (self.var.get() - mini) / (maxi - mini)
        self.updateMeterLine(pos * 0.789 + 0.1)

    def updateMeterTimer(self):
        """Fade over time"""
        self.var.set(self.var.get())
        self.after(20, self.updateMeterTimer)

    def updateVariableFromEntry(self):
        self.var.set(self.temp.get())

if __name__ == '__main__':
    meter = Meter(root)
    meter.pack()
    root.mainloop()