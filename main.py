import tkinter as tk
import gaus as g
M = 50
x0 = 400
y0 = 200
fig = [400,200,50]
global running
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Point3D(Point):
    def __init__(self, x, y, z):
        super(Point3D, self).__init__(x,y)
        self.z = z
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame()
        toolbar.pack(side=tk.TOP, fill=tk.X)

        goToFirst = tk.Button(toolbar, text='Первая лабораторная', command=lambda: FirstLab("№1"),
                              compound=tk.TOP)
        goToFirst.pack(side=tk.LEFT)

        goToSecond = tk.Button(toolbar, text='Вторая лабораторная', command=lambda: SecondLab("№2"),
                               compound=tk.TOP)
        goToSecond.pack(side=tk.LEFT)

        goToThird = tk.Button(toolbar, text='Третья лабораторная', command=lambda: FirstLab("№3"),
                              compound=tk.TOP)
        goToThird.pack(side=tk.LEFT)

class FirstLab(tk.Toplevel):
    def __init__(self, name):
        super().__init__(root)
        self.init_child(name)

    def init_child(self, name):
        self.title("Лабораторная работа " + name)
        self.geometry("820x550+300+200")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.canv = tk.Canvas(self, width=820, height=400, bg="white")
        self.draw_coord()
        self.canv.pack()
        self.getChoos()

    def getChoos(self):
        self.selected = tk.IntVar()
        self.first_task = tk.Radiobutton(self, text="Задание №1", variable=self.selected, value=1, command=self.select)
        self.first_task.place(x=20, y=490)

        self.second_task = tk.Radiobutton(self, text="Задание №2", variable=self.selected, value=2, command=self.select)
        self.second_task.place(x=20, y=520)

        self.third_task = tk.Radiobutton(self, text="Задание №3", variable=self.selected, value=3, command=self.select)
        self.third_task.place(x=150, y=490)

        self.fourth_task = tk.Radiobutton(self, text="Задание №4", variable=self.selected, value=4, command=self.select)
        self.fourth_task.place(x=150, y=520)

    def draw_coord(self):
        self.x0 = 400
        self.y0 = 200
        self.xm = 800
        self.ym = 0
        self.canv.create_line(self.x0 - 400, self.y0, self.xm + 10, self.y0,
                              fill='black', arrow=tk.LAST)

        self.canv.create_line(self.x0, self.ym, self.x0, self.y0 + 200,
                              fill='black', arrow=tk.FIRST)
        for i in range(self.x0 - 400, self.xm + 1):
            if i % 50 == 0:
                self.canv.create_line(i, self.ym, i, self.y0 + 200, fill='black')
                self.canv.create_text(i - 15, 200 + 10, text=str(int((i - 400) / 50)))
        for i in range(self.ym, self.y0 + 200):
            if i % 50 == 0:
                if int((i - 200) / 50) == 0:
                    continue
                self.canv.create_text(410, i + 15, text=str(int(-1 * (i - 200) / 50)))
                self.canv.create_line(self.ym, i, self.y0 + 610, i, fill='black')

    def select(self):
        l = self.selected.get()
        if l == 1:
            self.draw_element_1()
        if l == 2:
            self.draw_element_2()
        if l == 3:
            self.draw_element_2()
        if l == 4:
            self.draw_element_4()

    def destroyWid(self):
        list = self.winfo_children()
        for i in list:
            if str(type(i))=="<class 'tkinter.Canvas'>" or str(type(i))=="<class 'tkinter.Radiobutton'>":
                continue
            i.destroy()

    def draw_element_1(self):
        # Ввод функции
        self.destroyWid()
        funcLabel = tk.Label(self, text="Значение функции в видк K*x + B")
        funcLabel.place(x=20, y=410)
        funcValue = tk.Entry(self)
        funcValue.place(x=50, y=440)

        # Ввод первой точки
        firstPointLabel = tk.Label(self, text="Координаты первой точки")
        firstPointLabel.place(x=300, y=410)
        firstPointX = tk.Entry(self, width=3)
        firstPointX.place(x=350, y=440)
        firstPointY = tk.Entry(self, width=3)
        firstPointY.place(x=400, y=440)

        # Ввод второй точки
        secondPointLabel = tk.Label(self, text="Координаты второй точки")
        secondPointLabel.place(x=550, y=410)
        secondPointX = tk.Entry(self, width=3)
        secondPointX.place(x=600, y=440)
        secondPointY = tk.Entry(self, width=3)
        secondPointY.place(x=650, y=440)

        calBtn = tk.Button(self, text="Расчитать", command= lambda:self.calc_1(funcValue, firstPointX, firstPointY, secondPointX, secondPointY))
        calBtn.place(x=350, y=500)

        self.answ = tk.Label(self, text='Данные не введены', fg="#eee", bg="#333")
        self.answ.place(x=550, y=500)

    def draw_element_2(self):
        # Ввод первой точки
        self.destroyWid()
        firstPointLabel = tk.Label(self, text="Первая точка",bg="red")
        firstPointLabel.place(x=30, y=410)
        firsPointX = tk.Entry(self, width=3)
        firsPointX.place(x=30, y=440)
        firsPointY = tk.Entry(self, width=3)
        firsPointY.place(x=90, y=440)

        # Ввод второй точки
        secondPointLabel = tk.Label(self, text="Вторая точка",bg="blue")
        secondPointLabel.place(x=230, y=410)
        secondPointX = tk.Entry(self, width=3)
        secondPointX.place(x=230, y=440)
        secondPointY = tk.Entry(self, width=3)
        secondPointY.place(x=290, y=440)

        thirdPointLabel = tk.Label(self, text="Третья точка",bg="green")
        thirdPointLabel.place(x=430, y=410)
        thirdPointX = tk.Entry(self, width=3)
        thirdPointX.place(x=430, y=440)
        thirdPointY = tk.Entry(self, width=3)
        thirdPointY.place(x=490, y=440)

        # Ввод четвертой точки
        fourthPointLabel = tk.Label(self, text="Четвертая точка",bg="yellow")
        fourthPointLabel.place(x=630, y=410)
        fourthPointX = tk.Entry(self, width=3)
        fourthPointX.place(x=630, y=440)
        fourthPointY = tk.Entry(self, width=3)
        fourthPointY.place(x=690, y=440)

        if self.selected.get() == 2:
            func = lambda: self.calc_2(firsPointX,firsPointY,secondPointX,secondPointY,thirdPointX,thirdPointY,fourthPointX, fourthPointY)
        elif self.selected.get() == 3:
            func = lambda: self.calc_3(firsPointX,firsPointY,secondPointX,secondPointY,thirdPointX,thirdPointY,fourthPointX, fourthPointY)
        calBtn = tk.Button(self, text="Расчитать", command=func)
        calBtn.place(x=350, y=500)  
        self.answ = tk.Label(self, text='Данные не введены', fg="#eee", bg="#333")
        self.answ.place(x=550, y=500)
    
    def draw_element_4(self):
        # Ввод функции
        self.destroyWid()
        funcLabel = tk.Label(self, text="Значение плоскости в видк Ax + By + Cz + D = 0")
        funcLabel.place(x=20, y=410)
        funcValue = tk.Entry(self)
        funcValue.place(x=50, y=440)

        # Ввод первой точки
        firstPointLabel = tk.Label(self, text="Координаты первой точки")
        firstPointLabel.place(x=330, y=410)
        firstPointX = tk.Entry(self, width=3)
        firstPointX.place(x=350, y=440)
        firstPointY = tk.Entry(self, width=3)
        firstPointY.place(x=400, y=440)
        firstPointZ = tk.Entry(self, width=3)
        firstPointZ.place(x=450, y=440)

        # Ввод второй точки
        secondPointLabel = tk.Label(self, text="Координаты второй точки")
        secondPointLabel.place(x=580, y=410)
        secondPointX = tk.Entry(self, width=3)
        secondPointX.place(x=600, y=440)
        secondPointY = tk.Entry(self, width=3)
        secondPointY.place(x=650, y=440)
        secondPointZ = tk.Entry(self, width=3)
        secondPointZ.place(x=700, y=440)

        calBtn = tk.Button(self, text="Расчитать", command= lambda:self.calc_4(funcValue, firstPointX, firstPointY, firstPointZ,\
                                                                                secondPointX, secondPointY, secondPointY))
        calBtn.place(x=350, y=500)

        self.answ = tk.Label(self, text='Данные не введены', fg="#eee", bg="#333")
        self.answ.place(x=550, y=500)


    def calc_1(self, funcValue, firstPointX, firstPointY, secondPointX, secondPointY):
        self.canv.delete("all")
        self.draw_coord()
        try:
            f = funcValue.get()
            for i in range(-10000, 10000):
                x = i/160
                new_f = f.replace('x', str(x))
                y = -eval(new_f)
                self.canv.create_oval(M*x+self.x0, self.y0 + M*y, M*x+self.x0 + 5, self.y0 + M*y + 5,
                                      fill='black')
            p1 = Point(int(firstPointX.get()), int(firstPointY.get()))
            
            p2 = Point(int(secondPointX.get()), int(secondPointY.get()))
            
            self.canv.create_oval(M * p1.x + self.x0 - 2, self.y0 + M * -p1.y - 2, M * p1.x + self.x0 + 5,
                                  self.y0 + M * -p1.y + 5,
                                  fill='green')
            self.canv.create_oval(M * p2.x + self.x0 - 2, self.y0 + M * -p2.y - 2, M * p2.x + self.x0 + 5,
                                  self.y0 + M * -p2.y + 5,
                                  fill='red')
            self.get_answer_1(p1.x, p1.y, p2.x, p2.y, f)
        except:
            pass

    def calc_2(self,firsPointX,firsPointY,secondPointX,secondPointY,thirdPointX,thirdPointY,fourthPointX, fourthPointY):
        self.canv.delete("all")
        self.draw_coord()
        p1 = Point(int(firsPointX.get()), int(firsPointY.get()))
        p2 = Point(int(secondPointX.get()), int(secondPointY.get()))

        p3 = Point(int(thirdPointX.get()), int(thirdPointY.get()))
        p4 = Point(int(fourthPointX.get()), int(fourthPointY.get()))

        print(p1.x,p2.y,p3.x,p4.y)
        self.canv.create_line(M * p1.x + self.x0, self.y0 - M*p1.y, M*p2.x + self.x0,self.y0- M*p2.y, fill='black')
        self.canv.create_line(M * p3.x + self.x0, self.y0 - M*p3.y, M*p4.x + self.x0,self.y0- M*p4.y, fill='black')
        self.canv.create_oval(M * p1.x + self.x0 - 3, self.y0 + M * -p1.y - 3, M * p1.x + self.x0 + 5,
                                  self.y0 + M * -p1.y + 5,
                                  fill='red')
        self.canv.create_text(M * p1.x + self.x0 - 3, self.y0 + M * -p1.y - 3, text="A")

        self.canv.create_oval(M * p2.x + self.x0 - 2, self.y0 + M * -p2.y - 2, M * p2.x + self.x0 + 5,
                                  self.y0 + M * -p2.y + 5,
                                  fill='blue')
        self.canv.create_text(M * p2.x + self.x0 - 3, self.y0 + M * -p2.y - 3, text="B")

        self.canv.create_oval(M * p3.x + self.x0 - 2, self.y0 + M * -p3.y - 2, M * p3.x + self.x0 + 5,
                                  self.y0 + M * -p3.y + 5,
                                  fill='green')
        self.canv.create_text(M * p3.x + self.x0 - 3, self.y0 + M * -p3.y - 3, text="C")

        self.canv.create_oval(M * p4.x + self.x0 - 2, self.y0 + M * -p4.y - 2, M * p4.x + self.x0 + 5,
                                  self.y0 + M * -p4.y + 5,
                                  fill='yellow')
        self.canv.create_text(M * p4.x + self.x0 - 3, self.y0 + M * -p4.y - 3, text="D")
        self.get_answ_2(p1,p2,p3,p4)

    def calc_3(self,firsPointX,firsPointY,secondPointX,secondPointY,thirdPointX,thirdPointY,fourthPointX, fourthPointY):
        self.canv.delete("all")
        self.draw_coord()
        p1 = Point(int(firsPointX.get()), int(firsPointY.get()))
        p2 = Point(int(secondPointX.get()), int(secondPointY.get()))

        p3 = Point(int(thirdPointX.get()), int(thirdPointY.get()))
        p4 = Point(int(fourthPointX.get()), int(fourthPointY.get()))

        self.canv.create_line([
                                (M * p1.x + self.x0, self.y0 - M*p1.y), 
                                (M * p2.x + self.x0, self.y0 - M*p2.y),
                                (M * p3.x + self.x0, self.y0 - M*p3.y)
                            ], fill='black')
        self.canv.create_text(M * p1.x + self.x0 - 5, self.y0 - M*p1.y, text="A")
        self.canv.create_text(M * p2.x + self.x0 - 5, self.y0 - M*p2.y, text="B")
        self.canv.create_text(M * p3.x + self.x0  -5, self.y0 - M*p3.y, text="C")
        self.canv.create_oval(M * p4.x + self.x0 - 2, self.y0 + M * -p4.y - 2, M * p4.x + self.x0 + 5,
                                  self.y0 + M * -p4.y + 5,
                                  fill='yellow')
        self.get_answ_3(p1,p2,p3,p4)

    def calc_4(self,funcValue, firsPointX, firsPointY, firsPointZ, secondPointX, secondPointY , secondPointZ):
        self.canv.delete("all")
        self.draw_coord()
        func = funcValue.get()
        p1 = Point3D(int(firsPointX.get()), int(firsPointY.get()), int(firsPointZ.get()))
        p2 = Point3D(int(secondPointX.get()), int(secondPointY.get()), int(secondPointZ.get()))
        symbol_1 = -1 if eval(func.replace('x', str(p1.x)).replace('y', str(p1.y)).replace('z', str(p1.z))) == 0 else eval(func.replace('x', str(p1.x)).replace('y', str(p1.y)).replace('z', str(p1.z))) > 0
        symbol_2 = -1 if eval(func.replace('x', str(p2.x)).replace('y', str(p2.y)).replace('z', str(p2.z))) == 0 else eval(func.replace('x', str(p2.x)).replace('y', str(p2.y)).replace('z', str(p2.z))) > 0
        print(symbol_1, symbol_2)
        if symbol_1 == symbol_2 and symbol_1 == -1:
            self.answ.config(text="На плоскости")
            self.answ.config(bg="yellow", fg="black")
            return
        if symbol_1 and symbol_2 or (not symbol_1 and not symbol_2):
            self.answ.config(text="По одну сторону плоскости")
            self.answ.config(bg="green")
        else:
            self.answ.config(text="По разные плоскости")
            self.answ.config(bg="red")

    def get_answer_1(self, x1, y1, x2, y2, func):
        symbol_1 = -1 if eval(func.replace('x', str(x1))) == y1 else eval(func.replace('x', str(x1))) > y1
        symbol_2 = -1 if eval(func.replace('x', str(x2))) == y2 else eval(func.replace('x', str(x2))) > y2
        print(symbol_1, symbol_2)
        if symbol_1 == symbol_2 and symbol_1 == -1:
            self.answ.config(text="На прямой")
            self.answ.config(bg="yellow", fg="black")
            return
        if symbol_1 and symbol_2 or (not symbol_1 and not symbol_2):
            self.answ.config(text="По одну сторону")
            self.answ.config(bg="green")
        else:
            self.answ.config(text="По разные")
            self.answ.config(bg="red")

    def get_answ_2(self, p1, p2, p3, p4):
        print("p1: ",p1.x, p1.y)
        print("p2: ",p2.x, p2.y)
        print("p3: ",p3.x, p3.y)
        print("p4: ",p4.x, p4.y)
        
        if (p1.x==0 and p2.x==0 and p3.x==0 and p4.x==0) and p2.y>p1.y:
            if p3.y>p1.y :
                self.answ.config(text="Пересекаются")
                self.answ.config(bg="green")
                return
            elif p3.y<p1.y and p4.y>p3.y:
                self.answ.config(text="Пересекаются")
                self.answ.config(bg="green")
                return
            elif p3.y<p1.y and p4.y<p3.y:
                self.answ.config(text="НЕ пересекаются")
                self.answ.config(bg="red")
            return
        elif  p2.y<p1.y:
            if p3.y<p1.y :
                self.answ.config(text="Пересекаются")
                self.answ.config(bg="green")
                return
            elif p3.y>p1.y and p4.y>p3.y:
                self.answ.config(text="НЕ ересекаются")
                self.answ.config(bg="red")
                return
            elif p3.y>p1.y and p4.y<p3.y:
                self.answ.config(text="Пересекаются")
                self.answ.config(bg="green")
                return

        if  p2.x>p1.x:
            print("YES",p2.x)
            if p3.x>p1.x:
                print("YES",p3.x)
                self.answ.config(text="Пересекаются")
                self.answ.config(bg="green")
                return
            elif p4.x>p3.x:
                self.answ.config(text="Пересекаются")
                self.answ.config(bg="green")
                return
            else:
                self.answ.config(text="НЕ ересекаются")
                self.answ.config(bg="red")
                return
        elif p3.x<p1.x:
            self.answ.config(text="Пересекаются")
            self.answ.config(bg="green")
            return
        elif p4.x<p3.x:
            self.answ.config(text="Пересекаются")
            self.answ.config(bg="green")
            return
        else:
            self.answ.config(text="НЕ ересекаются")
            self.answ.config(bg="red")
            return
            
       

                
    def get_answ_3(self,p1,p2,p3,p4):
        flag,matrix = g.gaus([(p2.x-p1.x,p2.x-p3.x,p2.x-p4.x),
                              (p2.y-p1.y,p2.y-p3.y,p2.y-p4.y)])
        print([(p2.x-p1.x,p2.x-p3.x,p2.x-p4.x),
                              (p2.y-p1.y,p2.y-p3.y,p2.y-p4.y)])
        print(matrix[0][2], matrix[1][2])
        if matrix[0][2] >= 0 and matrix[1][2] >= 0:
            self.answ.config(text="Внутри")
            self.answ.config(bg="green", fg="black")
        else:
            self.answ.config(text="Снаружи")
            self.answ.config(bg="red", fg="black")

class SecondLab(tk.Toplevel):
    def __init__(self, name):
        super().__init__(root)
        self.init_child(name)
        

    def init_child(self, name):
        self.title("Лабораторная работа " + name)
        self.geometry("820x550+300+200")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.canv = tk.Canvas(self, width=820, height=400, bg="white")
        self.draw_coord()
        #Элементы
        self.circle = [0 + self.x0 - 100, 0 + self.y0 - 100, 100]
        self.insidePoint = [self.x0 - self.circle[0]/4,self.y0 - self.circle[1]/2]
        self.canv.pack()
        self.darawFigure()
        self.drawPlay()

    def draw_coord(self):
        self.x0 = 400
        self.y0 = 200
        self.xm = 800
        self.ym = 0
        self.canv.create_line(self.x0 - 400, self.y0, self.xm + 10, self.y0,
                              fill='black', arrow=tk.LAST)

        self.canv.create_line(self.x0, self.ym, self.x0, self.y0 + 200,
                              fill='black', arrow=tk.FIRST)
        for i in range(self.x0 - 400, self.xm + 1):
            if i % 50 == 0:
                self.canv.create_line(i, self.ym, i, self.y0 + 200, fill='black')
                self.canv.create_text(i - 15, 200 + 10, text=str(int((i - 400) / 50)))
        for i in range(self.ym, self.y0 + 200):
            if i % 50 == 0:
                if int((i - 200) / 50) == 0:
                    continue
                self.canv.create_text(410, i + 15, text=str(int(-1 * (i - 200) / 50)))
                self.canv.create_line(self.ym, i, self.y0 + 610, i, fill='black')

    def start_motor(self,go):
        print(go, fig[0], fig[1], x0)
        if go == "u":
            fig[1] = fig[1] - 10
        elif go == "d":
            fig[1] = fig[1] + 10
        elif go == "l":
            fig[0] = fig[0] - 10
        elif go== "r":
            fig[0] = fig[0] + 10
        elif go == "oy":
            fig[1] = -fig[1] + 2*y0
        elif go == "ox":
            fig[0] = -fig[0] + 2*x0
        elif go == "xy":
            fig[1] = -fig[1] + 2*y0
            fig[0] = -fig[0] + 2*x0
        self.darawFigure()

    def drawPlay(self):
        self.up = tk.Button(self, text ="↑", command= lambda:self.start_motor("u"))
        self.up.place(x=100, y=420)

        self.down = tk.Button(self, text ="↓",command= lambda:self.start_motor("d"))
        self.down.place(x=100, y=470)

        self.left = tk.Button(self, text ="←",command= lambda:self.start_motor("l"))
        self.left.place(x=50, y=450)

        self.right = tk.Button(self, text ="→",command= lambda:self.start_motor("r"))
        self.right.place(x=150, y=450)

        self.oy = tk.Button(self, text ="⇕",command= lambda:self.start_motor("oy"))
        self.oy.place(x=350, y=450)

        self.ox = tk.Button(self, text ="⇔",command= lambda:self.start_motor("ox"))
        self.ox.place(x=450, y=450)

        self.xy = tk.Button(self, text ="⤡",command= lambda:self.start_motor("xy"))
        self.xy.place(x=550, y=450)

    def darawFigure(self):
        self.canv.delete("all")
        self.draw_coord()
        x = fig[0]
        y = fig[1]
        r = fig[2]
        self.canv.create_oval(x-r,y-r,x+r,y+r)
        self.canv.create_line([(x-r, y, x-r/4,y-r/4),
                               (x-r/4,y-r/4, x,y - r),
                               (x,y - r, x+r/4,y-r/4),
                               (x+r/4,y-r/4, x+r,y),
                               (x+r,y, x+r/4,y+r/4),
                               (x+r/4,y+r/4, x,y + r),
                               (x,y + r, x-r/4,y + r/4),
                               (x-r/4,y + r/4,x-r, y)
                               ])

if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Чернов Матвей")
    root.geometry("700x500+300+200")
    root.resizable(False, False)
    root.mainloop()
