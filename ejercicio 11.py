intereses=0.04
cantidad=float(input('Cuanto dinero va a insertar:'))
primer_año=round(cantidad * (1 + intereses),2)
print('El primer año a recibido',primer_año,'€')
segundo_año=round(primer_año * (1 + intereses),2)
print('El segundo año a recibido',segundo_año,'€')
tercer_año=round(segundo_año * (1 + intereses),2)
print('El tercer año a recibido',tercer_año,'€')