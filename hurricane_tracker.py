import turtle

def irma_setup():
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    (t, wn, map_bg_img) = irma_setup()

    irma_file = open("C:\\Users\\nick pc\\PycharmProjects\\pythonProject\\StarterFiles\\StarterFiles\\data\\irma.csv", "r")
    contents = irma_file.readlines()
    t.penup()
    t.speed(1)
    for i in contents[2:]:
        i = i.strip()
        i = i.split(",")
        lat = float(i[2])
        lon = float(i[3])
        wind = float(i[4])

        if wind < 74:
            t.pensize(1)
            t.color("white")
        elif wind <= 95:
            t.pensize(3)
            t.color("blue")
            t.write("1")
        elif wind <= 110:
            t.pensize(6)
            t.color("green")
            t.write("2")
        elif wind <= 129:
            t.pensize(9)
            t.color("yellow")
            t.write("3")
        elif wind <= 156:
            t.pensize(12)
            t.color("orange")
            t.write("4")
        else:
            t.pensize(15)
            t.color("red")
            t.write("5")

        t.goto(lon, lat)
        t.pendown()
    turtle.done()

def maria_setup():
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Maria")

    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

def maria():

    (t, wn, map_bg_img) = maria_setup()

    maria_file = open("C:\\Users\\nick pc\\PycharmProjects\\pythonProject\\StarterFiles\\StarterFiles\\data\\maria.csv", "r")
    contents = maria_file.readlines()
    t.penup()
    t.speed(1)
    for i in contents[2:]:
        i = i.strip()
        i = i.split(",")
        lat = float(i[2])
        lon = float(i[3])
        wind = float(i[4])

        if wind < 74:
            t.pensize(1)
            t.color("white")
        elif wind <= 95:
            t.pensize(3)
            t.color("blue")
            t.write("1")
        elif wind <= 110:
            t.pensize(6)
            t.color("green")
            t.write("2")
        elif wind <= 129:
            t.pensize(9)
            t.color("yellow")
            t.write("3")
        elif wind <= 156:
            t.pensize(12)
            t.color("orange")
            t.write("4")
        else:
            t.pensize(15)
            t.color("red")
            t.write("5")

        t.goto(lon, lat)
        t.pendown()
    turtle.done()

def jose_setup():
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Jose")

    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

def jose():
    (t, wn, map_bg_img) = jose_setup()
    jose_file = open("C:\\Users\\nick pc\\PycharmProjects\\pythonProject\\StarterFiles\\StarterFiles\\data\\jose.csv", "r")
    contents = jose_file.readlines()
    t.penup()
    t.speed(1)
    for i in contents[2:]:
        i = i.strip()
        i = i.split(",")
        lat = float(i[2])
        lon = float(i[3])
        wind = float(i[4])

        if wind < 74:
            t.pensize(1)
            t.color("white")
        elif wind <= 95:
            t.pensize(3)
            t.color("blue")
            t.write("1")
        elif wind <= 110:
            t.pensize(6)
            t.color("green")
            t.write("2")
        elif wind <= 129:
            t.pensize(9)
            t.color("yellow")
            t.write("3")
        elif wind <= 156:
            t.pensize(12)
            t.color("orange")
            t.write("4")
        else:
            t.pensize(15)
            t.color("red")
            t.write("5")

        t.goto(lon, lat)
        t.pendown()
    turtle.done()

def choice():
    options = input("Which hurricane would you like to simulate? (Irma, Maria or Jose): ")
    options = options.lower()
    if options == "maria":
        maria()
    elif options == "irma":
        irma()
    elif options == "jose":
        jose()
    else:
        print("This is not a valid option.")

choice()
