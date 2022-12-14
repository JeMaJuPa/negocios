from openpyxl import Workbook
from openpyxl.styles import Font

def limpiar():
    datos = []
    print("Ingresa el nombre del archivo (no escribas nada para salir): ",end="")
    res = input()
    while res != "":
        with open(res) as archivo:
            lineaAnterior = ""
            for linea in archivo:
                #Omite lineas vacias
                datosL = []
                datosLinea = linea.split(' ')
                if lineaAnterior != datosLinea[0]:
                    if esNumero(linea[0:2]): #Vefificar que sea una linea valida
                        contador = 0
                        #Saca la IP
                        datosL.append(datosLinea[contador])
                        for dato in datosLinea:
                            #Omite lineas vacias
                            if dato != "-" or contador == 0:
                                if contador == 3:
                                    #Saca la fecha
                                    datosL.append(dato[1:12])
                                    #Saca la hora
                                    datosL.append(f"{dato[13:15]}:00:00")
                                if contador == 5: # Obtiene el metodo
                                    if dato != "\"-\"":
                                        datosL.append(dato[1:len(dato)])
                                    else:
                                        datosL.append("NA")
                                if contador == 10: #Obtiene la URL
                                    if "localhost" not in dato:
                                        datosL.append(dato) #URL
                                        if "https://ingsoftware.reduaz.mx/moodle/login/index.php" == dato:
                                            print(dato.find("id="))
                                        datosL.append(dato[dato.find("id=")+3:dato.find("\" ")]) # ID
                                        datosL.append(asignarCurso(datosL[len(datosL)-1])) # Nombre curso
                                    else:
                                        datosL.append("NA")
                                        datosL.append("NA")
                                        datosL.append("NA")
                            contador+=1
                        if len(datosL) > 4:
                            if datosL[3] != "NA" and datosL[4] != "\"-\"" and datosL[6] != "NA":
                                datosL.append(asignarSistema(linea)) # Sistema operativo
                                if datosL[0][0:4] == "10.2":
                                    datosL.append("Interna")
                                else:
                                    datosL.append("Externa")
                                datos.append(datosL)
                        lineaAnterior = datosLinea[0]
        print("Ingresa el nombre del archivo (no escribas nada para salir): ",end="")
        res = input()
    guardarDatos(datos,datos[0][1].replace("/","_",2))

def asignarCurso(id):
    cursos = [["642", "Matem??ticas para ingenier??a"],
              ["640", "Sistema Operativo Linux"],
              ["617", "Estrategias de aprendizaje"],
              ["618", "Estrategias de aprendizaje"],
              ["633", "Estrategias de aprendizaje"],
              ["598", "??lgebra"],
              ["599", "??lgebra"],
              ["600", "??lgebra"],
              ["643", "L??gica y Algoritmos"],
              ["644", "L??gica y Algoritmos"],
              ["606", "Introducci??n a Ingenier??a de Software"],
              ["586", "Introducci??n a Ingenier??a de Software"],
              ["574", "Introducci??n a la Programaci??n"],
              ["585", "Laboratorio de Introducci??n a la Programaci??n"],
              ["629", "Laboratorio de Programaci??n Orientada a Objetos I"],
              ["624", "Introducci??n al Desarrollo de Aplicaciones Web"],
              ["622", "Programaci??n Orientada a Objetos I"],
              ["650", "Sistema Operativo Linux"],
              ["630", "Sistema Operativo Linux"],
              ["646", "An??lisis y dise??o de algoritmos"],
              ["612", "An??lisis y Dise??o de Algoritmos"],
              ["645", "Matem??ticas discretas"],
              ["647", "Matem??ticas discretas"],
              ["610", "Programaci??n Orientada a Objetos II"],
              ["609", "Laboratorio de Programaci??n Orientada a Objetos II"],
              ["575", "Programaci??n Orientada a Objetos II"],
              ["625", "Estructuras de Datos y Laboratorio"],
              ["601", "Sistemas de Base de Datos I"],
              ["602", "Laboratorio de Sistemas de Base de Datos I"],
              ["654", "Miner??a de Datos I"],
              ["631", "??tica y Normatividad Jur??dica Inform??tica"],
              ["626", "Laboratorio de Sistemas de Base de Datos II"],
              ["611", "T??picos Selectos de Sistemas de Informaci??n"],
              ["603", "Sistemas de Base de Datos II"],
              ["641", "Pruebas y mantenimiento de software"],
              ["623", "Negocios Electr??nicos"],
              ["583", "Seguridad en Redes y Sistemas de Software"],
              ["588", "Seminario de Investigaci??n"],
              ["587", "Seminario de Tesis"],
              ["565", "Curso nuevo ingreso 2022"]]
    for curso in cursos:
        if curso[0] == id:
            return curso[1]
    return "NA"
def asignarSistema(linea):
    if "Windows" in linea:
        return "Windows"
    elif "Linux; Android" in linea:
        return "Android"
    elif "Linux x86_64" in linea:
        return "Linux"
    elif "iPhone" in linea:
        return "iPhone"
    elif "Macintosh" in linea:
        return "Macintosh"
    else:
        return "NA"

def guardarDatos(datos, nombre):
    book = Workbook()
    limpio = book.active
    limpio['A1'] = 'IP'
    limpio['A1'].font = Font(bold=True)
    limpio['B1'] = 'FECHA DE ACCESO'
    limpio['B1'].font = Font(bold=True)
    limpio['C1'] = 'HORA DE ACCESO'
    limpio['C1'].font = Font(bold=True)
    limpio['D1'] = 'METODO'
    limpio['D1'].font = Font(bold=True)
    limpio['E1'] = 'URL'
    limpio['E1'].font = Font(bold=True)
    limpio['F1'] = 'ID'
    limpio['F1'].font = Font(bold=True)
    limpio['G1'] = 'CURSO'
    limpio['G1'].font = Font(bold=True)
    limpio['H1'] = 'SISTEMA OPERATIVO'
    limpio['H1'].font = Font(bold=True)
    limpio['I1'] = 'INTERNA / EXTERNA'
    limpio['I1'].font = Font(bold=True)
    
    filas = 0
    abc = "ABCDEFGHI"
    for fila in datos:
        columnas = 0
        for columna in fila:
            limpio[f'{abc[columnas]}{filas+2}'] = columna
            columnas+=1
        filas+=1
    book.save(f'{nombre}.xlsx')

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