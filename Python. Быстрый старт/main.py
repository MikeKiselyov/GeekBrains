# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import turtle
from alphabet import alphabet

cursor = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("#000000")
cursor.pensize(3)


def displayMessage(message, fontSize, color, x, y):
    cursor.color(color)
    message = message.upper()

    for character in message:
        if character in alphabet:
            letter = alphabet[character]
            cursor.penup()
            for dot in letter:
                cursor.goto(x + dot[0] * fontSize, y + dot[1] * fontSize)
                cursor.pendown()

            x += fontSize

        if character == " ":
            x += fontSize
        x += characterSpacing


fontSize = 27
characterSpacing = 7
fontColor = "#4688F1"

message = "testing is power"
displayMessage(message, fontSize, fontColor, -270, 0)
