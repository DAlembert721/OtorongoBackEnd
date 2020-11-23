def calculo_futuro_a_tasa_simple(capital, descuento, tiempo, tasa, tipo_tiempo):
    descuento /= 100

    saldo = capital * (1 - descuento)
    if tipo_tiempo == 'exacto':
        tiempo /= 365
    else:
        tiempo /= 360
    tasa /= 100
    futuro = saldo * (1 + tasa * tiempo)
    # print("La tasa de interes anual es de:  ", tasa * 100)
    # print("El futuro a tasa simple es de: ", futuro)
    return round(futuro, 2)


def calculo_tasa_interes(capital, descuento, tiempo, tipo_tiempo, futuro):
    descuento /= 100
    saldo = capital * (1 - descuento)
    if tipo_tiempo == 'exacto':
        tiempo /= 365
    else:
        tiempo /= 360
    interes = (futuro / saldo - 1) / tiempo
    # print("La tasa de interes anual con año ", tipo_tiempo, " es de: ", interes * 100)
