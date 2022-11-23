def limpiar():
    datos = []
    print("Ingresa el nombre del archivo: ",end="")
    with open(input()) as archivo:
        for linea in archivo:
            #Omite lineas vacias
            if esNumero(linea[0:2]): #Vefificar que sea una linea valida
                contador = 0
                datosL = []
                datosLinea = linea.split(' ')
                #Saca la IP
                datosL.append(datosLinea[contador])
                for dato in datosLinea:
                    #Omite lineas vacias
                    if dato != "-" or contador == 0:
                        if contador == 3:
                            #Saca la fecha
                            datosL.append(dato[1:12])
                            #Saca la hora (pura hora)
                            datosL.append(dato[13:15])
                        if contador == 5:
                            if dato != "\"-\"":
                                datosL.append(dato[1:len(dato)])
                            else:
                                datosL.append("")
                        if contador == 6:
                                datosL.append(dato)
                    contador+=1
    
def esNumero(cadena):
    try:
        int(cadena)
        return True
    except:
        return False
    
def main():
    limpiar()
    
if __name__ == '__main__':
    main()