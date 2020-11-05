def tasa_nominal_a_tasa_efectiva(tasa, cotizacion, deseado):
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
    print(m)
    n = switcher.get(deseado, deseado) / switcher.get(cotizacion, 1)
    print(n)
    t = tasa[0] / 100
    te = (1 + t / m) ** n - 1
    print("La tasa efectiva ", deseado, " es de ", te*100)
    return te

def tasa_efectiva_a_tasa_nominal(tasa, cotizacion, deseado):
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
    n = switcher.get(deseado, deseado) / switcher.get(cotizacion, 1)
    t = tasa[0] / 100
    tn = m * ((1 + t) ** (1 / n) - 1)
    print("La tasa nominal ", deseado, " es de ", tn*100)
    return tn

def tasa_efectiva_a_tasa_efectiva(tasa, deseado):
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
    n1 = switcher.get(tasa[1], tasa[1])
    n2 = switcher.get(deseado, deseado)
    t = tasa[0] / 100
    te = (1 + t) ** (n2/n1) - 1
    print("La tasa efectiva ", deseado, " es de ", te*100)
    return te

