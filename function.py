import random
from string import ascii_letters, digits

alfabe = ascii_letters[:25]
nimerik = digits

# 3
def kod_aleyatwa_alfabetik_san_repetisyon(alfabe, n):
    """
    Yon fonksyon ki pou jenere yon
    kòd aleyatwa ki gen n karaktè 
    alfabetik san repetisyon
    """
    kod = random.sample(alfabe, n)
    return ''.join(kod)

# 4
def kod_aleyatwa_alfanimerik_san_repitisyon(alfanimerik, n):
    """
    Yon fonksyon ki pou jenere yon kod
    aleyatwa ki gen n karakte alfanimerik
    san repetisyon
    """
    kod = random.sample(alfanimerik, n)
    return ''.join(kod)

# 5
def slugify(chenn):
    """
    Yon fonksyon ki pou
    suglifye yon chenn karakte
    """
    chenn = chenn.lower()
    chenn = chenn.replace(" ", "-")
    slug = ""
    for karakte in chenn:
        if karakte in alfabe or karakte in nimerik or karakte == "-":
            slug += karakte

    return slug

# 8 
def separe_let_ak_vigil(mo):
    nouvo_mo = ""
    for let in mo:
        nouvo_mo += let+","

    return nouvo_mo

# 9 


if __name__ == '__main__':
    alfanimerik = alfabe + nimerik

    print( 
        kod_aleyatwa_alfabetik_san_repetisyon(alfabe, 6),
        kod_aleyatwa_alfanimerik_san_repitisyon(alfanimerik, 6),
        slugify("ch@mane servius"),
        separe_let_ak_vigil("chamane")
    )
