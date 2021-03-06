memorias_RAM= int (input("introducir  el numero de memoria ram que no son nuevas :"))
precio=20.00
descuento=0.6
costo =memorias_RAM*precio*(1-descuento)
print('el costo de las memorias Ram nuevas es :' +str(precio) + '$')
print(' el descuendo de las memorias RAM usadad' + str(descuento*100)+ "%")
print( ' el precio de las memorias Ram usadas:' + str(round(costo,2))+ "$")
