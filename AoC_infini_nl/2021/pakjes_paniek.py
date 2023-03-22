import random
input_file = 'input.txt'
f = open(input_file)
speelgoedlijst = f.readlines()
f.close()


missende_onderdelen = 0
onderdelen = {}
ingepakte_cadeaus = 0
if input_file == 'input.txt':
    ingepakte_cadeaus = 20
elif input_file == 'test_input.txt':
    ingepakte_cadeaus = 3


def bereken_onderdelen(onderdel_lijst, onderdelen):
    sum = 0
    for onderdel in onderdel_lijst.keys():
        if onderdel != 'totaal':
            nieuw_onderdel = onderdelen.get(onderdel)
            if nieuw_onderdel == None:
                sum += onderdel_lijst[onderdel]
            else:
                sum += (bereken_onderdelen(nieuw_onderdel, onderdelen)*onderdel_lijst[onderdel])

    return sum


for speelgoed in speelgoedlijst:
    speelgoed = speelgoed.replace('\n', '')
    if not 'onderdelen missen' in speelgoed:

        split_lijst = speelgoed.split(':')
        speelgoed_naam = split_lijst[0]
        speelgoed_onderdelen = split_lijst[1].split(',')
        temp_onderdelen = {}
        for onderdel in speelgoed_onderdelen:
            split_onderdel = onderdel.split(' ')

            hoeveelhijd = temp_onderdelen.get(split_onderdel[2])
            if hoeveelhijd == None:
                hoeveelhijd = int(split_onderdel[1])
            else:
                hoeveelhijd += int(split_onderdel[1])
            temp_onderdelen.update({split_onderdel[2]: hoeveelhijd})

        onderdelen.update({speelgoed_naam: temp_onderdelen})
    else:
        missende_onderdelen = int(speelgoed.split(' ')[0])


for onderdel in onderdelen.keys():
    onderdel_lijst = onderdelen.get(onderdel)
    sum_onderdelen = bereken_onderdelen(onderdel_lijst, onderdelen)
    onderdel_lijst.update({'totaal': sum_onderdelen})
    onderdelen.update({onderdel: onderdel_lijst})

max_totaal = 0

for onderdel in onderdelen.keys():
    if onderdelen[onderdel]['totaal'] > max_totaal:
        max_totaal = onderdelen[onderdel]['totaal']

print('Het speelgoed met het grootste aantal aan onderdelen heeft '+str(max_totaal)+' onderdelen.')

geen_speelgoed = []
for onderdel in onderdelen.keys():
    onderdel_lijst = onderdelen.get(onderdel)
    for deel in onderdel_lijst.keys():
        if onderdelen.get(deel) != None:
            geen_speelgoed.append(deel)

for deel in geen_speelgoed:
    try:
        onderdelen.pop(deel)
    except:
        pass

f = open('output.txt')
speelgoedlijst = f.readlines()
f.close()

if speelgoedlijst == []:
    totaal_cadeaus = ingepakte_cadeaus
    totaal_delen = missende_onderdelen
    speelgoed = []
    for key in onderdelen.keys():
        speelgoed.append(key)
    found_combination = False
    speelgoed_combi = []
    while not found_combination:
        speelgoed_combi = []
        totaal_cadeaus = ingepakte_cadeaus
        totaal_delen = missende_onderdelen

        for i in range(ingepakte_cadeaus):
            nieuw_speelgoed = speelgoed[random.randrange(0, len(speelgoed))]
            totaal_delen -= onderdelen[nieuw_speelgoed]['totaal']
            speelgoed_combi.append(nieuw_speelgoed)
            if totaal_delen < 0:
                break

        if totaal_delen == 0:
            found_combination = True

    for speelgoed_naam in speelgoed_combi:
        print(speelgoed_naam[0])

speelgoed = []
for toy in speelgoedlijst:
    speelgoed.append(toy[0])
speelgoed.sort()
speelgoed_text = ''
for toy in speelgoed:
    speelgoed_text += toy
print('Het missende speelgoed is: '+speelgoed_text)
