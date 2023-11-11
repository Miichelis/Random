import random
ola="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()=+_"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower=upper.lower()
nums="1234567890"
symbols="!@#$%^&*()=+_"

passwd=''

def has_upper(passwd):
    has_upperr=False
    for item in passwd:
        if item in upper:
            has_upperr=True
    return has_upperr

def has_lower(passwd):
    has_lowerr=False
    for item in passwd:
        if item in lower:
            has_lowerr=True
    return has_lowerr

def has_nums(passwd):
    has_numss=False
    for item in passwd:
        if item in nums:
            has_numss=True
    return has_numss


def has_symbols(passwd):
    has_symbolss=False
    for item in passwd:
        if item in symbols:
            has_symbolss=True
    return has_symbolss

flag=0
while flag == 0:
    passwd=""
    for i in range(6):
        pass_char=ola[random.randint(0,len(ola))-1]
        passwd += str(pass_char)
    if has_upper(passwd) == True and has_lower(passwd) == True and has_nums(passwd) == True and has_symbols(passwd) == True :
        flag=1
print(passwd)        


