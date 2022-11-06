print("Ingrese los valores:")
print("|M00 M01 M02|")
print("|M10 M11 M12|")
print("|M20 M21 M22|")

M00 = float(input('Ingrese el valor M00: '))
M01 = float(input('Ingrese el valor M01: '))
M02 = float(input('Ingrese el valor M02: '))
M10 = float(input('Ingrese el valor M10: '))
M11 = float(input('Ingrese el valor M11: '))
M12 = float(input('Ingrese el valor M12: '))
M20 = float(input('Ingrese el valor M20: '))
M21 = float(input('Ingrese el valor M21: '))
M22 = float(input('Ingrese el valor M22: '))

determinante_M= (M00*M11*M22) + (M10*M21*M02) + (M20*M01*M12) - (M02*M11*M20) - (M12*M21*M00) - (M22*M01*M10)

if determinante_M!=0:
   print ("El determinante de esta matriz es: ",determinante_M)

else:
    print ("El detrrminante de esta matriz es 0")