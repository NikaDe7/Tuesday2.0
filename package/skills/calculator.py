from tkinter import*
from math import*

def Call():
    tk=Tk()
    tk.geometry("260x360")
    #поле
    ent=Entry(font="Arial 14", justify="right")
    ent.place(x=20, y=30, width=220, height=30)
    #0
    def B0_click():
        ent.insert(END,"0")
    B0=Button(text="0", font="14", command=B0_click)
    B0.pack()
    B0.place(x=20, y=290, width=100, height=40)
    #1
    def B1_click():
        ent.insert(END,"1")
    B1=Button(text="1", font="14", command=B1_click)
    B1.pack()
    B1.place(x=20, y=240, width=40, height=40)
    #2
    def B2_click():
        ent.insert(END,"2")
    B2=Button(text="2", font="14", command=B2_click)
    B2.pack()
    B2.place(x=80, y=240, width=40, height=40)
    #3
    def B3_click():
        ent.insert(END,"3")
    B3=Button(text="3", font="14", command=B3_click)
    B3.pack()
    B3.place(x=140, y=240, width=40, height=40)
    #4
    def B4_click():
        ent.insert(END,"4")
    B4=Button(text="4", font="14", command=B4_click)
    B4.pack()
    B4.place(x=20, y=190, width=40, height=40)
    #5
    def B5_click():
        ent.insert(END,"5")
    B5=Button(text="5", font="14", command=B5_click)
    B5.pack()
    B5.place(x=80, y=190, width=40, height=40)
    #6
    def B6_click():
        ent.insert(END,"6")
    B6=Button(text="6", font="14", command=B6_click)
    B6.pack()
    B6.place(x=140, y=190, width=40, height=40)
    #7
    def B7_click():
        ent.insert(END,"7")
    B7=Button(text="7", font="14", command=B7_click)
    B7.pack()
    B7.place(x=20, y=140, width=40, height=40)
    #8
    def B8_click():
        ent.insert(END,"8")
    B8=Button(text="8", font="14", command=B8_click)
    B8.pack()
    B8.place(x=80, y=140, width=40, height=40)
    #9
    def B9_click():
        ent.insert(END,"9")
    B9=Button(text="9", font="14", command=B9_click)
    B9.pack()
    B9.place(x=140, y=140, width=40, height=40)
    #.
    def BP_click():
        ent.insert(END,".")
    BP=Button(text=".", font="14", command=BP_click)
    BP.pack()
    BP.place(x=140, y=290, width=40, height=40)
    #С
    def BC_click():
        ent.delete(0,END)
    BC=Button(text="C", font="14", command=BC_click)
    BC.pack()
    BC.place(x=20, y=80, width=40, height=40)
    #Radical
    def BR_click():
        a=float(ent.get())
        ent.delete(0,END)
        if a<0:
            ent.insert(END,"Помилка")
        else:
            ent.insert(END,sqrt(a))    
    BR=Button(text="*1/2*", font="14", command=BR_click)
    BR.pack()
    BR.place(x=80, y=80, width=40, height=40)
    #Modul
    def BK_click():
        a=float(ent.get())
        ent.delete(0,END)
        ent.insert(END,abs(a))
    BK=Button(text="|x|", font="14", command=BK_click)
    BK.pack()
    BK.place(x=140, y=80, width=40, height=40)
    #=
    def BE_click():
        c=float(ent.get())
        if b=="+":
            ent.delete(0,END)
            ent.insert(END,a+c)
        if b=="-":
            ent.delete(0,END)
            ent.insert(END,a-c)
        if b=="*":
            ent.delete(0,END)
            ent.insert(END,a*c)
        if b=="/":
            if c==0:
                ent.delete(0,END)
                ent.insert(END,"Помилка")
            else:
                ent.delete(0,END)
                ent.insert(END,a/c)
    BE=Button(text="=", font="14", command=BE_click)
    BE.pack()
    BE.place(x=200, y=80, width=40, height=40)
    #/
    def BD_click():
        global a,b
        a=float(ent.get())
        b="/"
        ent.delete(0,END)
    BD=Button(text="/", font="14", command=BD_click)
    BD.pack()
    BD.place(x=200, y=140, width=40, height=40)
    #*
    def BM_click():
        global a,b
        a=float(ent.get())
        b="*"
        ent.delete(0,END)
    BM=Button(text="*", font="14", command=BM_click)
    BM.pack()
    BM.place(x=200, y=190, width=40, height=40)
    #+
    def BPL_click():
        global a,b
        a=float(ent.get())
        b="+"
        ent.delete(0,END)
    BPL=Button(text="+", font="14", command=BPL_click)
    BPL.pack()
    BPL.place(x=200, y=290, width=40, height=40)
    #-
    def BMS_click():
        global a,b
        a=float(ent.get())
        b="-"
        ent.delete(0,END)
    BMS=Button(text="-", font="14", command=BMS_click)
    BMS.pack()
    BMS.place(x=200, y=240, width=40, height=40)
    return 'Готово'
