
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

def get_marca(numero_marca):
    marca = "Babidu"
    return marca