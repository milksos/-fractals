from simpletk import *
from tkinter.messagebox import askokcancel
import turtle

def AskOnExit(event):
    if askokcancel('Подтверждение','Вы действительно хотите выйти из програмы?'):
        app.destroy()

def koch(ln, n):
    if n == 0:
        t.fd(ln)
    else:
        for i in [0, 60, -120, 60]:
            t.left(i)
            koch(ln/3, n-1)

def sneg(event):
    window = turtle.Screen()
    t.reset()
    window.bgcolor(a[color_form%5])
    t.speed(0)
    t.penup()
    t.goto(-250, 150)
    t.pensize(2)
    t.color('white')
    t.pendown()
    koch(500, r)
    t.right(120)
    koch(500, r)
    t.right(120)
    koch(500, r)
    t.right(120)
    t.hideturtle()
    #window.exitonclick()

def draw_free(ln,n):
    if ln>5 and n>0:
        if ln < 40:
            t.color('green')
        else:
            t.color('red')
        t.forward(ln)
        t.right(25)
        draw_free(ln-15,n-1)
        t.left(50)
        draw_free(ln-15,n-1)
        if ln < 40:
            t.color('green')
        else:
            t.color('red')
        t.right(25)
        t.backward(ln)
        

def tree(sender):
    window = turtle.Screen()
    t.reset()
    t.speed(0)
    window.bgcolor(a[color_form%5])
    t.left(90)
    t.penup()
    t.backward(150)
    t.pendown()
    t.color('red')
    draw_free(100,r)
    #window.exitonclick()

    
def draw_sierpinski(length,n):
    if n==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,n-1)
        t.fd(length/2)
        draw_sierpinski(length/2,n-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,n-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)

def tr_serp(sender):
    window = turtle.Screen()
    t.reset()
    t.speed(0)
    t.penup()
    t.goto(-200, -150)
    window.bgcolor(a[color_form%5])
    t.color('white')
    t.pendown()
    draw_sierpinski(350,r)
    
def onChange(sender):
    global r
    if rEdit.text!="":
        r=int(rEdit.text)

def change_color(sender):
    global color_form
    color_form+=1


app=TApplication('Проектная работа фракталы')
app.position=(20,200)
app.size=(440,300)

color_form=0
a=['blue','brown','gold','navy','lightcoral']

kohBtn=TButton(app,width=120,text='Снежинка Коха')
kohBtn.position=(20,220)

treeBtn=TButton(app,width=120,text='Дерево')
treeBtn.position=(160,220)

serpBtn=TButton(app,width=120,text='Тр-к Серпинского')
serpBtn.position=(300,220)

ColorBtn=TButton(app,width=120,text='Изменить цвет')
ColorBtn.position=(160,40)

kohBtn.onClick=sneg
treeBtn.onClick=tree
serpBtn.onClick=tr_serp
ColorBtn.onClick=change_color


f=("Ms Sans Serif",12)
rEdit=TEdit(app,font=f,width=50)
rEdit.position=(30,40)
rEdit.text="2"
rEdit.onChange=onChange


t = turtle.Turtle()
window = turtle.Screen()

app.onCloseQuery=AskOnExit
window.exitonclick()
app.run()
