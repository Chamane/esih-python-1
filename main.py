import string 

def dekripte(antre):
    dekripte = antre.split('-')

    mekanik = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    adekripte = []
    for eleman in dekripte:
        if len(eleman) == 1:
            adekripte.append(mekanik[int(eleman)])
        elif len(eleman) == 2:
            if eleman[0] == '0':
                adekripte.append(mekanik[int(eleman[1])].upper())
    
    return "".join(adekripte)

def kripte(antre):
    pass



if __name__ in "__main__":
    retou = dekripte("00-01-02-3-4-5-6")
    print(retou)