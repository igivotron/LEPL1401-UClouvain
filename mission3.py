import turtle                # module des graphiques tortue
tortue = turtle.Turtle()     # créer une nouvelle tortue
tortue.speed(0)      # tracé rapide
tortue.ht()
turtle.bgcolor('silver')

belgian = ['black', 'yellow', 'red']
verstappen = ['red', 'white', 'blue']
french = ['blue', 'white', 'red']
lux = ['red', 'white', 'skyblue']
hans = ['black','red','yellow']

def rectangle(size1, size2, color,pos_x, pos_y):
    """
    :param size1: Longueur du rectangle
    :param size2: Largeur du rectangle
    :param color: Couleur du rectangle
    :param pos_x: position x de la tortue au premier trait
    :param pos_y: position y de la tortue au premier trait
    :return: None
    """
    tortue.goto(pos_x, pos_y)
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(size1)
        tortue.right(90)
        tortue.forward(size2)
        tortue.right(90)

    tortue.end_fill()
    tortue.penup()
    tortue.forward(size1)

def v_flag(l, color_flag,pos_x,pos_y):
    """
    :param l: Longueur du rectangle
    :param color_flag: Liste contenant les couleurs du drapeaux
    :return: None
    """
    tortue.penup()
    pos_x += -3 * l / 2
    pos_y += l
    for i in range(3):
        rectangle(l, 2*l, color_flag[i], pos_x, pos_y)
        pos_x += l

def h_flag(l, color_flag, pos_x, pos_y):
    """
    :param l: Largeur du rectangle
    :param color_flag: Couleurs du drapeau
    :return: None
    """
    tortue.penup()
    pos_x += -3 * l / 2
    pos_y += l
    for i in range(3):
        rectangle(3*l, 2*l/3, color_flag[i], pos_x, pos_y)
        pos_y -= 2*l/3

def star(m, color, pos_x, pos_y):
    tortue.penup()
    tortue.goto(pos_x-m/2, pos_y+m/5)
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(5):
        tortue.forward(m)
        tortue.left(72)
        tortue.forward(m)
        tortue.right(144)
    tortue.end_fill()

    tortue.penup()

def eu_flag(l,pos_x, pos_y):
    tortue.penup()
    pos_x += -3 * l / 2
    pos_y += l
    rectangle(3*l,2*l,'mediumblue',pos_x,pos_y)
    pos_x += +3 * l / 2
    pos_y += -l
    tortue.goto(pos_x,pos_y)
    tortue.color('black')
    for i in range(12):
        tortue.fd(2/3*l)
        tortue.left(30)
        last_heading = tortue.heading()
        tortue.setheading(0)
        star(l/15,'yellow',tortue.xcor(),tortue.ycor())
        tortue.goto(pos_x,pos_y)
        tortue.setheading(last_heading)

v_flag(50, belgian,-350, 200)
h_flag(50, verstappen, -175, 200)
h_flag(50, hans, 0, 200)
h_flag(50, lux, 175, 200)
v_flag(50, french, 350, 200)
eu_flag(100, 0, 0)

turtle.exitonclick()
