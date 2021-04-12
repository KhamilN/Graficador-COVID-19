import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
import math as mt

def wget(url): #esta funcion importa archivos para Windows, es para la base de datos
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)
wget('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
def es_numero(num,cant):  #Esta funcion revisa que el input sea correcto o en caso contrario informa la necesidad de caracteres numericos
    if len(num)==cant:          #requiere que un input tenga una determinada cantidad de caracteres
         if num.isdigit() is True:  #chequea que el input sea numerico
             return True
         else:     #En caso de que el input no sea numerico, informa de ese requerimiento
            print('Ingrese exclusivamente caracteres numericos por favor.')
            return False        
    else:                   #En caso de que el input no tenga la cantidad necesaria, informa cual es.
        str_cant=str(cant)  
        print('Ingrese '+str_cant+' caracteres por favor.')
        return False
        
def es_fecha_correcta(num,inicio,final):  #Esta función revisa que las fechas esten en los valores correctos
    num=int(num)
    if num>=inicio and num<=final:      #chequea que un int este dentro de los limites requeridos
        return True
    else:     #si el input no esta dentro de los limites, informa cuales son.
        str_inicio=str(inicio)
        str_final=str(final)
        print('Ingrese un numero entre '+str_inicio+' y '+str_final+' por favor')
        return False

def año(num):    #Chequea que el año ingresado sea válido.
    if es_numero(num,4) is True:
        if es_fecha_correcta(num,2019,2020) is True:
            return True
        else:
            return False
    else:
        return False

def mes(num):   #Chequea que el mes ingresado sea válido.
    if es_numero(num,2) is True:
        if es_fecha_correcta(num,1,12) is True:
            return True
        else:
            return False
    else:
        return False

cant_dias={31:['01','03','05','07','08','10','12'],30:['04','06','09','11']} #lista de meses con sus cantidades de dias respectivas.
def cant_dias_en_mes(mes):  #Comprueba que el numero del dia coincida con la cantidad de dias del mes
    if mes in cant_dias[31]:
        return 31
    elif mes in cant_dias[30]:
        return 30
    elif mes == '02':
        if año_inicio =='2020':
            return 29
        if año_inicio =='2019':
            return 28

def dia(num,limite):   #Chequea que el dia ingresado sea válido.
    if es_numero(num,2) is True:
        if es_fecha_correcta(num,1,limite) is True:
            return True
        else:
            return False
    else:
        return False

def graficar_casos(fecha,lista_paises,matriz,log): #Esta funcion genera los graficos. Recibe una lista de fechas, una de los paises a graficar, y una matriz con los valores de cada país
    for z in range (0,num_paises):
        plt.subplot(1, 2, 1)  # grafico de nuevos casos
        plt.plot(fecha,matriz[:,0,z],':', label=lista_paises[z])
        print(fecha)
        print(matriz[:,0,z])
    plt.xlabel('fecha')
    plt.xticks(rotation=90)
    plt.ylabel('casos')
    log   
    plt.title('Casos totales de COVID-19 según la fecha')
    plt.legend()
def graficar_muertes(fecha,lista_paises,matriz):
    for z in range (0,num_paises):
        plt.subplot(1, 2, 2)  #grafico de nuevas muertes
        plt.plot(fecha,matriz[:,1,z],':', label=lista_paises[z])
    plt.ylabel('muertes')
    plt.xlabel('fecha')
    plt.xticks(rotation=90)
    plt.title('Muertes totales por COVID-19 según la fecha')
    plt.legend()

def find_intersecciones_y_graficar(fecha,matriz,dato_a_graficar): # Esta funcion encuentra las intersecciones entre las lineas a graficar y las señala con un punto azul
    largo=len(fecha)
    for pais in range (0,num_paises): #este for recorre cada país a graficar
        if pais<num_paises:
            for pais_a_comparar in range(pais+1,num_paises): #este for selecciona paises a comparar con el elegido arriba
                interseccion_indice=[]
                for valores in range (0,largo): #este for recorre las listas de valores sean de casos o de muertes
                    if matriz[valores,dato_a_graficar,pais]==matriz[valores,dato_a_graficar,pais_a_comparar]:#este if detecta si hay valores en comun y  guarda el indice en una lista
                        interseccion_indice.append(valores)
                y_interseccion=[]
                x_interseccion=[]
                for x in interseccion_indice: #este for trae el valor de X y el valor de Y de las intersecciones
                    y_interseccion.append(matriz[x,dato_a_graficar,pais])
                    x_interseccion.append(fecha[x])
                if dato_a_graficar==0:
                    plt.subplot(1, 2, 1)  # casos
                    plt.scatter(x_interseccion,y_interseccion,s = 10,c='blue' , linewidth = 5)
                elif dato_a_graficar==1:
                    plt.subplot(1, 2, 2)  # casos
                    plt.scatter(x_interseccion,y_interseccion,s = 10,c='blue' , linewidth = 5)

#este bloque obtiene la lista de paises del csv y toma una sola iteración de cada una para que 
# el input de pais elegido chequee contra esto.
data=pd.read_csv('full_data.csv')
columna_pais=pd.DataFrame(data, columns= ['location'])
lista_paises_repetidos=columna_pais.values.tolist()        #genera una lista de la columna de paises de la base de datos
lista_paises_correcta=np.unique(lista_paises_repetidos)    #guarda una sola iteración de cada país de la base de datos

#este bloque obtiene la lista de paises del csv y toma una sola iteración de cada una para que 
# el input de pais elegido chequee contra esto.



print('Bienvenido al graficador de COVID-19')   
confirmacion_pais=0     #variable de confirmación del input
while confirmacion_pais==0: #chequea que el usuario confirme su ingreso
    num_paises=(input('Ingrese numero de paises a comparar(Ej:02): '))
    while es_numero(num_paises,2) is False: #chequea que el ingreso sea la cantidad correcta de caracteres numericos
        num_paises=(input('Ingrese numero de paises a comparar(Ej:02): '))
    num_paises=int(num_paises)
    lista_paises_a_graficar=[] #lista en la que se almacenaran los paises a graficar
    for x in range (0,num_paises):  # for que carga la lista de paises
        pais=input('Ingrese país(utilizando el nombre en inglés y con mayúscula(ej:Spain)): ')    
        if pais in lista_paises_correcta: #Chequea que el input de pais sea válido en la base de datos
            lista_paises_a_graficar.append(pais)
        else:
            while pais not in lista_paises_correcta: #En caso de input invalido, requiere volver a ingresar
                print('Error al ingresar el nombre del país. Por favor, vuelva a intentar.(recuerde utilizar el nombre en inglés y con mayúscula(ej:Spain))')
                pais=input('Ingrese país(utilizando el nombre en inglés y con mayúscula(ej:Spain)): ')
            else:
                lista_paises_a_graficar.append(pais)
    print('usted ha seleccionado',end=' ') #muestra la lista ingresada y pide confirmacion
    print(lista_paises_a_graficar,end=' ') #muestra la lista ingresada y pide confirmacion
    conf=input('¿es correcto?(si/no)')     #muestra la lista ingresada y pide confirmacion
    while not(conf=='si' or conf=='no'):   #chequea que el input de confirmación sea estrictamente si o no
        conf=input('Ingrese si o no: ')
    if conf=='si':
        confirmacion_pais=1
    elif conf=='no':
        confirmacion_pais=0


error_fecha=1
while error_fecha==1:
    confirmacion_fechas=0
    while confirmacion_fechas==0:
        print('Ingresar la fecha de inicio del periodo a consultar') #el csv usa el formato año-mes-dia
        año_inicio=(input('Ingrese año de inicio(Ej:2020): '))
        while año(año_inicio)is False:
            año_inicio=(input('Ingrese año de inicio(Ej:2020): '))
        mes_inicio=(input('Ingrese mes de inicio(Ej:06): '))
        while mes(mes_inicio)is False:
            mes_inicio=(input('Ingrese mes de inicio(Ej:06): '))
        dia_inicio_limite=cant_dias_en_mes(mes_inicio)
        dia_inicio=(input('Ingrese dia de inicio(Ej:08): '))
        while dia(dia_inicio,dia_inicio_limite)is False:
            dia_inicio=(input('Ingrese dia de inicio(Ej:08): '))

        fecha_inicio=año_inicio+'-'+mes_inicio+'-'+dia_inicio

        año_cierre=(input('Ingrese año de cierre(Ej:2020): '))
        while año(año_cierre)is False:
            año_cierre=(input('Ingrese año de cierre(Ej:2020): '))
        mes_cierre=(input('Ingrese mes de cierre(Ej:06): '))
        while mes(mes_cierre)is False:
            mes_cierre=(input('Ingrese mes de cierre(Ej:06): '))
        dia_cierre_limite=cant_dias_en_mes(mes_inicio)
        dia_cierre=(input('Ingrese dia de cierre(Ej:08): '))
        while dia(dia_cierre,dia_cierre_limite)is False:
            dia_cierre=(input('Ingrese dia de cierre(Ej:08): '))

        fecha_cierre=año_cierre+'-'+mes_cierre+'-'+dia_cierre
        print('usted ha seleccionado',end=' ') 
        print(fecha_inicio,end=' y ')
        print(fecha_cierre,end=' ')
        conf=input('¿es correcto?(si/no)')
        while not(conf=='si' or conf=='no'):
            conf=input('Ingrese si o no: ')
        if conf=='si':
            confirmacion_fechas=1
        elif conf=='no':
            confirmacion_fechas=0
    if np.datetime64(fecha_cierre)<np.datetime64(fecha_inicio):
        error_fecha=1
        print('La fecha de cierre es anterior a la fecha de inicio. Ingrese los datos en el orden correcto por favor.')
    else:
        error_fecha=0
#lista_paises_a_graficar
#fecha_inicio
#fecha_cierre

#creación de array con valores de fechas para eje x
fechaFinal = (np.datetime64(fecha_cierre)+np.timedelta64(1, 'D'))
fechas=np.array(np.arange(fecha_inicio, fechaFinal, dtype='datetime64[D]'))

#seteo de magnitud de dimensiones para array de valores de Y (nuevos casos, muertes)
dias = (np.datetime64(fechaFinal) - np.datetime64(fecha_inicio) )
columnas = 2
matrices = len(lista_paises_a_graficar)
matrizDatos = np.zeros([np.size(fechas), columnas, matrices], dtype=np.int64)

#Verificaciones de matriz

#print(matrizDatos)
#print(np.size(fechas)*columnas*matrices)
#print(np.size(matrizDatos))
#print(np.shape(matrizDatos))


#Verificacion array de fechas
''' 
print(fechas)
print(np.size(fechas))
'''

#busqueda de fecha en particular
'''
inicio = np.where(fechas == np.datetime64('2020-05-02'))[0]
print(inicio)
'''

#recoleccion de datos del pais necesario
datosPais = pd.DataFrame(data, columns= ['date','location','new_cases','new_deaths'])
for pais in lista_paises_a_graficar:
    arrayDatosPais = np.array(datosPais[datosPais.location == pais], )

    #print(arrayDatosPais)
    if ((np.datetime64(arrayDatosPais[0,0])) < (np.datetime64(fecha_inicio))):
        inicioDatoPais = int(np.where(arrayDatosPais == fecha_inicio)[0])
        inicioMatrizDatos = int(0)
        
    else:
        
        #inicioMatrizDatos = int(np.where(fechas == np.datetime64(arrayDatosPais[0][0]))[0])
        inicioMatrizDatos = int(np.where(arrayDatosPais == fecha_inicio)[0])
        inicioDatoPais = int(0)

    #print(inicioDatoPais)
    #print(inicioMatrizDatos)
    
    if (np.datetime64(arrayDatosPais[int((np.shape(arrayDatosPais)[0]))-1][0]) < (np.datetime64(fecha_cierre))):
        finalDeCarrera = np.size(fechas)
        
    else:
        
        finalDeCarrera = int(np.shape(arrayDatosPais)[0])
        finalDeCarrera = int(np.where(arrayDatosPais == fecha_cierre)[0])

   # print(finalDeCarrera)
   # print(np.size(fechas))

    
    print('inicioDatoPais: ',inicioDatoPais)
    print('inicioMatrizDatos: ',inicioMatrizDatos)
    print('inicioMatrizDatos+x: ',inicioMatrizDatos)
    print('finalDeCarrera: ',finalDeCarrera)

    for x in range(inicioDatoPais, finalDeCarrera, 1):
        
        '''
        print('x: ',x)
        print('inicioDatoPais: ',inicioDatoPais)
        print('inicioMatrizDatos: ',inicioMatrizDatos)
        print('inicioMatrizDatos+x: ',inicioMatrizDatos+x)
        print('finalDeCarrera: ',finalDeCarrera)
        '''
        
        if (int((np.shape(arrayDatosPais)[0]))>(int(np.shape(fechas)[0]))):

            if mt.isnan(arrayDatosPais [(x), 2]):
                print('nin_cases 1')
                matrizDatos[x-inicioDatoPais, 0, int(lista_paises_a_graficar.index(pais))] = int(0)
            else:
                print('cases 1')
                matrizDatos[x-inicioDatoPais, 0, int(lista_paises_a_graficar.index(pais))] = int(arrayDatosPais[x, 2])

            if mt.isnan(arrayDatosPais [(x), 3]):
                print('nin_death 1')
                matrizDatos [x-inicioDatoPais, 1, int(lista_paises_a_graficar.index(pais))] = int(0)
            else:
                print:('death 1')
                matrizDatos[x-inicioDatoPais, 1, int(lista_paises_a_graficar.index(pais))] = int(arrayDatosPais[x, 3])
        else:
            if ((x<inicioMatrizDatos) or (x>(int((np.shape(arrayDatosPais)[0]))))):
                
                matrizDatos[x, 0, int(lista_paises_a_graficar.index(pais))] = int(0)
                matrizDatos[x, 1, int(lista_paises_a_graficar.index(pais))] = int(0)
            
            else:
                if mt.isnan(arrayDatosPais [(x-1), 2]):
                    print('nin_cases 2')
                    matrizDatos[x, 0, int(lista_paises_a_graficar.index(pais))] = int(0)
                else:
                    print('cases 2')
                    matrizDatos[x, 0, int(lista_paises_a_graficar.index(pais))] = int(arrayDatosPais[x-1, 2])

                if mt.isnan(arrayDatosPais [(x-1), 3]):
                    print('nin_death 2')
                    matrizDatos[x, 1, int(lista_paises_a_graficar.index(pais))] = int(0)
                else:
                    print('death 2')
                    matrizDatos[x, 1, int(lista_paises_a_graficar.index(pais))] = int(arrayDatosPais[x-1, 3])


#plt.plot(fechas,matrizDatos[:,0,0])
#plt.show()

len_paises=len(lista_paises_a_graficar)
if len_paises==1:
    graficar_casos(fechas,lista_paises_a_graficar,matrizDatos,'')
    graficar_muertes(fechas,lista_paises_a_graficar,matrizDatos)
elif len_paises==2:
    graficar_casos(fechas,lista_paises_a_graficar,matrizDatos,'')
    graficar_muertes(fechas,lista_paises_a_graficar,matrizDatos)
    find_intersecciones_y_graficar(fechas,matrizDatos,0)
    find_intersecciones_y_graficar(fechas,matrizDatos,1)
elif len_paises>2:
    graficar_casos(fechas,lista_paises_a_graficar,matrizDatos,'plt.yscale(log)')
    find_intersecciones_y_graficar(fechas,matrizDatos,0)

plt.get_current_fig_manager().window.state('zoomed')
plt.show()
