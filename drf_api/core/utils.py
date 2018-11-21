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


def temp_f_2_c(temp):
    """
    translate Fahrenheit to Celsius
    T(°C) = (T(°F) -32) / 1.8
    """
    tf = (Decimal("%s" % temp) - 32) / Decimal("1.8")
    return tf.quantize(Decimal("0.001"))


def temp_c_2_f(temp):
    """
    translate Celsius to Fahrenheit
    T(°F) = (T(°C) * 1.8) + 32
    """
    tc = (Decimal("%s" % temp) * Decimal("1.8")) + 32
    return tc.quantize(Decimal("0.001"))


def mph_a_kms(mps):
    """
    tranformar Mps to km/h
    1 mile = 1.6093440 Kms
    1 km = 0.6214 miles
    """
    kms = Decimal("%s" % mps) * Decimal("1.6093440")
    return kms.quantize(Decimal('0.001'))


def kms_a_mph(kms):
    mps = Decimal("%s" % kms) * Decimal('0.6214')
    return mps.quantize(Decimal('0.001'))


def lluvia_desde_api(perfil, valor):
    """
    Transformar valor segun preferencias del perfil.
    """
    if perfil.lluvia_pref == 'mm':
        return valor
    else:
        return pulgadas_a_mm(valor)


def lluvia_para_api(perfil, valor):
    """
    Transformar valor segun preferencias del perfil.
    """
    if perfil.lluvia_pref == 'mm':
        return valor
    else:
        return mm_a_pulgadas(valor)


def viento_desde_api(perfil, valor):
    """
    Transformar el viento informado por el cliente a mm si corresponde.
    """
    if perfil.viento_pref == 'kph':
        return valor
    else:
        return mph_a_kms(valor)


def viento_para_api(perfil, valor):
    """
    Transformar el valor de viento a la unidad esperada por el cliente.
    """
    if perfil.viento_pref == 'kph':
        return valor
    else:
        return kms_a_mph(valor)


def temperatura_desde_api(perfil, valor):
    """
    Transformar la temperatura informada por el cliente a °C si corresponde.
    """
    if perfil.temperatura_pref == 'c':
        return valor
    else:
        return temp_f_2_c(valor)


def temperatura_para_api(perfil, valor):
    """
    Transformar el valor de temperatura a la unidad esperada por el cliente.
    """
    if perfil.temperatura_pref == 'c':
        return valor
    else:
        return temp_c_2_f(valor)

