
# import turtle
# shapeInput = input("Circle and square, what is your favourite shape?: ")
# if shapeInput == "circle" or shapeInput == "square":
#     print(shapeInput)
# else:
#     print("Sorry, I don't have this shape")
# colorInput = input('What color will it be?, yellow, red or blue? :')
# if colorInput == 'yellow' or colorInput == 'red' or colorInput == 'blue':
# 	print(colorInput)
# else:
# 	print("Sorry, I don't have this color :(")

# wn = turtle.Screen()
# wn.bgcolor("black")
# wn.title("Your shape")

# displayShape = turtle.Turtle()
# displayShape.shape(shapeInput)
# displayShape.color(colorInput)
# turtle.done()


def testshape():
    import turtle

    shapeInput = input('Circle and square: ')

    if shapeInput == "circle":
        colorInput = input('What color will it be?, yellow, red or blue: ')
        if colorInput == "yellow" or colorInput == "blue" or colorInput == "red":
            c = turtle.Turtle()
            c.pensize(3)
            c.circle(100)
            c.title("Your shape")
            displayShape = turtle.Turtle()
            displayShape.shape(shapeInput)
            displayShape.color(colorInput)
            turtle.done()
    elif shapeInput == "square":
        colorInput = input('What color will it be?, yellow, red or blue? :')
        if colorInput == "yellow" or colorInput == "blue" or colorInput == "red":
            c = turtle.Turtle()
            c.pensize(3)
            c.circle(100)
            c.title("Your shape")
            for i in range(4):
                c.forward(50)
                c.rt(90)
            displayShape = turtle.Turtle()
            displayShape.shape(shapeInput)
            displayShape.color(colorInput)
            turtle.exitonclick()
    else:
        print("Nothing")
#     if shapeInput == 'circle' or shapeInput == 'square':
#         colorInput = input('What color will it be?, yellow, red or blue? :')

#         if colorInput == 'yellow' or colorInput == 'red' or colorInput == 'blue':
#             wn = turtle.Screen()
#             wn.bgcolor("black")
#             # wn.pensize(3)
#             wn.title("Your shape")
#             # wn.circle(100)

#             displayShape = turtle.Turtle()
#             displayShape.shape(shapeInput)
#             displayShape.color(colorInput)

#             turtle.done()

#         else:
#             print("Sorry, I don't have this color :(")
#     else:
#         print("Sorry, I don't have this shape :(")


# if __name__ == "__main__":
#     testshape()
