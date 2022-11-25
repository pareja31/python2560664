#determinar cuantas horas extras trabaja si la jornada es de 48 horas
#libro: wordpress python "libro online" 

jornada= 48
vh= 8000
he=9000
htr=int(input("horas trabajadas"))
print("horas trabajadas ", htr)
print("la jornada es ", jornada)
if (htr>jornada):
    hte=htr-jornada
    print("horas trabajadas extras ",hte)
else:
    print("no tiene horas trabajadas extras")
    phe=he*htr
    print("pago de horas extras")
    print(phe)
    pj=(jornada*vh)+phe
    print("el pago por su jornada es ",pj, "pesos")

