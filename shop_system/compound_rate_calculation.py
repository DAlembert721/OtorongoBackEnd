import shop_system.rate_change as ct
def futuro_a_tasa_compuesta(capital, tasa, tiempo_dias, cotizacion, deseado):
    switcher = {
        'Diaria': 1,
        'Quincenal': 15,
        'Mensual': 30,
        'Bimestral': 60,
        'Trimestral': 90,
        'Cuatrimestral': 120,
        'Semestral': 180,
        'Anual': 360
    }
    s = 0
    if deseado == 'Nominal':
        m = switcher.get(tasa[1], tasa[1]) / switcher.get(cotizacion, cotizacion)
        n = tiempo_dias / switcher.get(cotizacion, cotizacion)
        tn = tasa[0] / 100
        s = capital * (1 + tn / m) ** n
        print("El futuro a tasa nominal es de: ", s)
    else:
        te = ct.tasa_efectiva_a_tasa_efectiva(tasa, tiempo_dias)
        s = capital * (te + 1)
        print("El futuro a tasa efectiva es de: ", s)
    return round(s, 2)


def calculo_tasa_efectiva(futuro, capital, deseado, tiempo_dias):
    switcher = {
        'Diaria': 1,
        'Quincenal': 15,
        'Mensual': 30,
        'Bimestral': 60,
        'Trimestral': 90,
        'Cuatrimestral': 120,
        'Semestral': 180,
        'Anual': 360
    }
    n = switcher.get(deseado, 0)
    te = (futuro / capital) ** (n / tiempo_dias) - 1
    print("la tasa efectiva es ", deseado, " de ", te * 100)
    return te


def calculo_tasa_nominal(futuro, capital, tiempo_dias, cotizacion, deseado):
    switcher = {
        'Diaria': 1,
        'Quincenal': 15,
        'Mensual': 30,
        'Bimestral': 60,
        'Trimestral': 90,
        'Cuatrimestral': 120,
        'Semestral': 180,
        'Anual': 360
    }
    m = switcher.get(deseado, deseado) / switcher.get(cotizacion, 0)
    n = tiempo_dias / switcher.get(cotizacion, 0)
    tn = m * ((futuro / capital) ** (1 / n) - 1)
    print("la tasa nominal es ", deseado, " de ", tn * 100)
    return tn


def calculo_interes_nominal(capital, tasa, cotizacion, tiempo_dias):
    switcher = {
        'Diaria': 1,
        'Quincenal': 15,
        'Mensual': 30,
        'Bimestral': 60,
        'Trimestral': 90,
        'Cuatrimestral': 120,
        'Semestral': 180,
        'Anual': 360
    }
    m = switcher.get(tasa[1], tasa[1]) / switcher.get(cotizacion, 1)
    n = tiempo_dias / switcher.get(cotizacion, 1)
    t = tasa[0] / 100
    interes = capital * (((1 + t / m) ** n) - 1)
    print("El interes es de: ", interes)
    return interes


def calculo_interes_efectiva(capital, tasa, tiempo_dias):
    switcher = {
        'Diaria': 1,
        'Quincenal': 15,
        'Mensual': 30,
        'Bimestral': 60,
        'Trimestral': 90,
        'Cuatrimestral': 120,
        'Semestral': 180,
        'Anual': 360
    }
    n = tiempo_dias / switcher.get(tasa[1], tasa[1])
    interes = capital * (((1 + tasa[0]/100) ** n) - 1)
    print("El interes es de:", interes)
    return interes

