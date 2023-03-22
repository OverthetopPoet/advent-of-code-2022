def bereken_pakjes(zijde):
    pakjes = 0
    for i in range(zijde):
        pakjes += 2*(zijde+2*i)
    pakjes += zijde*(3*zijde)
    return pakjes


def bereken_stof(zijde):
    return 8*zijde


inwoners = 17484032
pakjes = 0
zijde = 0

while pakjes < inwoners:
    zijde += 1
    pakjes = bereken_pakjes(zijde)

print('De minimale zijde voor de pakjes is: '+str(zijde))

stukken_stof = 0
continenten = [4541414172, 1340959217, 747769586, 430871505, 368956979, 42709912]
for inwoners in continenten:
    pakjes = 0
    zijde = 0
    while pakjes < inwoners:
        zijde += 1
        pakjes = bereken_pakjes(zijde)
    stukken_stof += bereken_stof(zijde)


print('De elven moeten '+str(stukken_stof)+' stukken stof koopen')
