#Calculator
AR=[]
prajeis=["+","-","*","/"]
posous_arithmous=int(input("posous arithmous thes na doseis: "))
ar=float(input("dose arithmo: "))
AR.append(ar)
while posous_arithmous <= 1:
    posous_arithmous=int(input("posous arithmous thes na doseis: "))
    
prajh=raw_input("dose prajh: ")

while prajh not in prajeis:
    prajh=raw_input("dose prajh: ")
i=0
while i < posous_arithmous-1:
    ar=float(input("dose epomeno arithmo: "))
    AR.append(ar)
    i+=1

def prosthesh(LISTA_AR):
    s=0
    for i in range(len(LISTA_AR)):
        s+=LISTA_AR[i]
    return s

def afairesh(LISTA_AR):
    MEG=LISTA_AR[0]
    for i in range(1,len(LISTA_AR)):
        MEG-=LISTA_AR[i]
            
    return MEG

def pol(LISTA_AR):
    g=1
    for item in LISTA_AR:
        g*=item
    return g

def dier(LISTA_AR):
    flag=0
    j=1
    MEG=LISTA_AR[0] 
    for i in range(1,len(LISTA_AR)):
        if LISTA_AR[i] == 0:
            return "den ginete diereshi me to miden"
            flag=1
    while j <= len(LISTA_AR)-1 and flag == 0:
        MEG=MEG*(1.0)/LISTA_AR[j]
        j+=1
    if flag == 0:
        return MEG

if prajh == "+":
    print prosthesh(AR)
elif prajh == "-":
    print afairesh(AR)
elif prajh == "*":
    print pol(AR) 
else:
    print dier(AR)

        
        
    
    
        
        
