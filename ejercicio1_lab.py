temperaturas = [18, 25, 31, 12, 28, 35, 20]

dia_frios = 0
dia_templados = 0
dia_calurosos = 0

for tem in temperaturas:
    if tem < 15:
        print (f"temperatura fria")
        dia_frios = dia_frios + 1
    elif tem <= 25:
        print(f"temperatura templada")
        dia_templados = dia_templados + 1
    else:
        print(f"temperatura calurosa")
        dia_calurosos = dia_calurosos + 1

print (f"dias frios:{dia_frios}dia_calurosos: {dia_calurosos} Dias templados {dia_templados}")

