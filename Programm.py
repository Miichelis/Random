import datetime
day=date.strftime("%w")
day=int(day)
def monday():
    print "Algebra\nXhmeia\nYlkd\nAI\nAI\nGymnastikh\nPython theoria"

def tuesday():
    print "Kampas\nYlkd\nPhotoshop\nPhotoshop\nPython\nPython\nPython"
    
def wednesday():
    print "Ylkd\nYlkd\nThriskeutika\nFysikh\nKampas\nLeitourgika\nLeitourgika"

def thursday():
    print "Kampas\nGeometria\nPAlgebra\nAI\nAI\nLeitourgika(theoria)\nTexnika Themata"


def friday():
    print "Texnika themata\nTexnika Themata\nAgglika\nAgglika\nEkthesh\nEkthesh\nEkthesh"


if day == 0:
    monday()
elif day == 1:
    tuesday()
elif day == 2:
    wednesday()
elif day == 3:
    thursday()
elif day == 4:
    friday()
    
