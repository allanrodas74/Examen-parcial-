a =float(input("su altura en metros:"))
est=a
m=float(input("su peso en lb:"))
IMC=m/est # para saber su masa coporal 
print("masa coporal :" + str(IMC))

#para saber en que forma se encuentra sabiendo su peso coporal 

if IMC >=0 and IMC <=70.99:
    print("desnutrido")
elif IMC >= 1.50 and IMC <=120.00:
    print("delgado ")
    
elif IMC >=1.75 and IMC <=160.99:
        print("normal")
        
elif IMC >=2.00 and IMC <=200.99:
            print("sobrepeso")

elif IMC>=40.00:
    print('obesidad')
