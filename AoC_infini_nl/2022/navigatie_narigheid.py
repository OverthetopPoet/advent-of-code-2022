import turtle
f = open('input.txt')
instructies = f.readlines()
f.close()

richting = 0
horizontale_afstand = 0
verticale_afstand = 0


def draai(richting, graden):
    graden = int(graden / 45)
    while graden >= 8:
        graden -= 8
    while graden <= -8:
        graden -= 8

    if graden < 0:
        graden += 8
    richting += graden
    if richting >= 8:
        richting -= 8
    return richting


def beweeg(horizontale_afstand, verticale_afstand, richting, afstand):
    if richting == 0:
        verticale_afstand += afstand
    elif richting == 1:
        verticale_afstand += afstand
        horizontale_afstand += afstand
    elif richting == 2:
        horizontale_afstand += afstand
    elif richting == 3:
        horizontale_afstand += afstand
        verticale_afstand -= afstand
    elif richting == 4:
        verticale_afstand -= afstand
    elif richting == 5:
        verticale_afstand -= afstand
        horizontale_afstand -= afstand
    elif richting == 6:
        horizontale_afstand -= afstand
    elif richting == 7:
        horizontale_afstand -= afstand
        verticale_afstand += afstand

    return horizontale_afstand, verticale_afstand


turtle.home()
for instructie in instructies:
    instructie = instructie.replace('\n', '')

    split_instructie = instructie.split(' ')
    ins_naam = split_instructie[0]
    ins_waarde = int(split_instructie[1])

    if ins_naam == 'draai':
        richting = draai(richting, ins_waarde)
        turtle.setheading((richting+2)*45)
    else:
        if ins_naam == 'spring':
            turtle.penup()
            turtle.forward(ins_waarde)
            horizontale_afstand, verticale_afstand = beweeg(
                horizontale_afstand, verticale_afstand, richting, ins_waarde)
            turtle.pendown()
        else:
            turtle.forward(ins_waarde)
            horizontale_afstand, verticale_afstand = beweeg(
                horizontale_afstand, verticale_afstand, richting, ins_waarde)

if horizontale_afstand < 0:
    horizontale_afstand *= -1
if verticale_afstand < 0:
    verticale_afstand *= -1

manhattan_afstand = horizontale_afstand+verticale_afstand
print('De Manhattan afstand tussen begin- en eindpunt is: '+str(manhattan_afstand))
while True:
    pass
