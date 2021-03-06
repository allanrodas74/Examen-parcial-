cantidad = float (input("el monto de la inversion:"))
interes =float (input("el interes por año :"))
años= float(input("numero de años :"))
print("capital final :"+str(round(cantidad+(interes/100 +1)**años,2)))
