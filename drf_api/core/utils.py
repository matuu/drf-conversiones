from decimal import Decimal


def mm_a_pulgadas(valor):
    """
    1mm = (1/25.4)″ = 0.03937007874″ --> d(″) = d(mm) / 25.4
    """
    try:
        return (valor / Decimal('25.4')).quantize(Decimal('0.001'))
    except TypeError:
        valor = Decimal("%s" % valor)
        return (valor / Decimal('25.4')).quantize(Decimal('0.001'))


def pulgadas_a_mm(valor):
    """
    1″ = 25.4mm --> d(mm) = d(″) × 25.4
    """
    try:
        return (valor * Decimal('25.4')).quantize(Decimal('0.001'))
    except TypeError:
        valor = Decimal("%s" % valor)
        return (valor * Decimal('25.4')).quantize(Decimal('0.001'))


# TODO: Otras transformaciones

def lluvia_desde_api(perfil, valor):
    """
    Transformar valor segun preferencias del perfil.
    """
    if perfil.lluvia_pref == 'mm':
        return valor
    else:
        return mm_a_pulgadas(valor)


def lluvia_para_api(perfil, valor):
    """
    Transformar valor segun preferencias del perfil.
    """
    if perfil.lluvia_pref == 'mm':
        return valor
    else:
        return pulgadas_a_mm(valor)

# TODO: resto de métodos para transformar los valores
