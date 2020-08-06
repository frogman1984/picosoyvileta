
categoria = ''
def categoria_producto(numero):
    numero = int(numero)
    global categoria
    if numero == 1:
        categoria = "Bañadores"
    elif numero == 2:
        categoria = "Camisas / Polos"
    elif numero == 3:
        categoria = "Camisetas"
    elif numero == 4:
        categoria = "Chaquetas"
    elif numero == 5:
        categoria = "Complementos"
    elif numero == 6:
        categoria = "Conjuntos"
    elif numero == 7:
        categoria = "Interiores"
    elif numero == 8:
        categoria = "Pantalones"
    elif numero == 9:
        categoria = "Pijamas"
    elif numero == 10:
        categoria = "Vestidos / Faldas"
    return categoria

def get_marca():
    numero_marca = input(""" Cual seria la Marca?
        1 - "Babidu"
        2 - "Sardon"
        3 - "Tuc-Tuc"
        4 - "Mauli"
        5 - "Dolce Petit"
        6 - "Ma Petit Lola"
        7 - "Street Monkey" """)
    numero = int(numero_marca)
    global marca
    if numero == 1:
        marca = "Babidu"
    elif numero == 2:
        marca = "Sardon"
    elif numero == 3:
        marca = "Tuc-Tuc"
    elif numero == 4:
        marca = "Mauli"
    elif numero == 5:
        marca = "Dolce Petit"
    elif numero == 6:
        marca = "Ma Petit Lola"
    elif numero == 7:
        marca = "Street Monkey"
    return marca