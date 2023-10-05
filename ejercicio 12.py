precio_pan_normal=3.49
descuento_no_fresca=0.6
pan_no_fresca=(int(input('Cuantas barras antiguas han sido vendidas:')))
precio_pan_no_fresca=round(float(precio_pan_normal * pan_no_fresca * (1-descuento_no_fresca) ),2)
print('El precio de pan normal es',precio_pan_normal,'€')
print('El descuento que se le hace al pan no fresco es del',(descuento_no_fresca * 100),'%')
print('El precio del pan no fresco es de',precio_pan_no_fresca,'€')