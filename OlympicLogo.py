import turtle as t
c=['blue','black','red','yellow','green']
t.pensize(20)
for n in range(5):
    t.color(c[n])
    t.penup()
    if n<3:
        t.goto(-240+240*n,0)
    else:
        t.goto(-120+240*(n-3),-100)
    t.pendown()
    t.circle(100)

