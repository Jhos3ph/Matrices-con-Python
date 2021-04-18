import random
from Num_Racionales import *

class Matriz:

    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.elementos = []
    

    def elem_Random(self):
        elementos = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(str(random.randint(-5, 5)))
            elementos.append(fila)
        self.elementos = list(elementos)
        self.imprimir_Matriz()


    def elementos_por_teclado(self):
        print(f'........... {self.nombre} ...........')
        elementos = []
        for fila in range(1, self.filas+1, 1):
            filastring = input(f'fila {fila}:   ')
            lista = []
            numstring = ''
            for i in filastring+',':
                if i == ',':
                    lista.append(numstring)
                    numstring = ''
                else:
                    numstring = numstring+i
            elementos.append(lista)
        self.elementos = list(elementos)


    def imprimir_Matriz(self):
        print(f'...........{self.nombre}..................')
        for fila in self.elementos:
            print(fila)


    def multiplicar_por_Escalar(self, escalar):
        self.nombre = f'({self.nombre})^t'
        new_matriz = []
        escalar = Numero_Racional(escalar)
        for fila in range(0, self.filas, 1):
            new_matriz.append([])
            for columna in range(0, self.columnas, 1):
                new_matriz[fila].append(escalar.multiplicar_dividir(self.elementos[fila][columna]))
        self.elementos = list(new_matriz)

    
    def convertir_Transpuesta(self):
        print(f'SE APLICO LA TRANSPUESTA A LA MATRIZ')
        self.nombre = '(' + self.nombre + ')^t'
        new_matriz = []
        for fila in range(0, self.columnas, 1):
            new_matriz.append([])
            for columna in range(0, self.filas, 1):
                new_matriz[fila].append(self.elementos[columna][fila])
        self.elementos = list(new_matriz)
        self.filas, self.columnas = self.columnas, self.filas


    def sumar_Matrices(self, matriz1, matriz2, restar=False):
        if (matriz1.filas == matriz2.filas) and (matriz1.columnas == matriz2.columnas):
            self.filas = matriz1.filas
            self.columnas = matriz1.columnas
            sig_menos = Numero_Racional('-1')
            for fila in range(0, matriz1.filas, 1):
                self.elementos.append([])
                for columna in range(0, matriz1.columnas, 1):
                    elem_matriz1 = Numero_Racional(matriz1.elementos[fila][columna])
                    if restar:
                        elem_matriz2 = sig_menos.multiplicar_dividir(matriz2.elementos[fila][columna])
                    else:
                        elem_matriz2 = matriz2.elementos[fila][columna]         
                    self.elementos[fila].append(elem_matriz1.sumar_restar(elem_matriz2))
        else:
            print('Las matrices deben ser de la misma dimension para sumar')


    def restar_Matrices(self, matriz1, matriz2):
        self.sumar_Matrices(matriz1, matriz2, True)


    def Elemento_delProducto(self, matriz1, matriz2, fila, columna):
        if (fila > matriz1.filas) or (columna > matriz2.columnas):
            print('El elemento no existe')
            return None
        else:
            if matriz1.columnas == matriz2.filas:
                elemento_ij = '0'
                for k in range(0, matriz1.columnas, 1):
                    acumulador = Numero_Racional(elemento_ij)
                    numero = Numero_Racional(matriz1.elementos[fila-1][k])
                    elemento_ij = acumulador.sumar_restar(numero.multiplicar_dividir(matriz2.elementos[k][columna-1]))
                return elemento_ij
            else:
                print('Las operacion no esta definida')
                return None


    def multiplicar_Matrices(self, matriz1, matriz2):
        new_matriz = []
        for fila in range(0, matriz1.filas, 1):
            new_matriz.append([])
            for columna in range(0, matriz2.columnas, 1):
                new_matriz[fila].append(self.Elemento_delProducto(matriz1, matriz2, fila+1, columna+1))
        self.elementos = list(new_matriz)
        self.filas = matriz1.filas
        self.columnas = matriz2.columnas


    def permutar_filas(self, fila1, fila2, matriz):
        print(f'---P{fila1}{fila2}---')
        new_matriz = []
        for i in range(len(matriz)):
            if i == fila1-1:
                new_matriz.append(matriz[fila2-1])
            elif i == fila2-1:
                new_matriz.append(matriz[fila1-1])
            else:
                new_matriz.append(matriz[i])
        return new_matriz


    def multiplicar_fila(self, fila, escalar, matriz):
        print(f'---M{fila}({escalar})---')
        new_matriz = []
        constante = Numero_Racional(escalar)
        fila_mult = []
        for elemento in matriz[fila-1]:
            fila_mult.append(constante.multiplicar_dividir(elemento))

        for i in range(len(matriz)):
            if i == fila-1:
                new_matriz.append(fila_mult)
            else:
                new_matriz.append(matriz[i])
        return new_matriz


    def sumar_filas(self, fila_a_modificar, fila2, escalar, matriz):
        print(f'---{self.nombre}{fila_a_modificar}{fila2}({escalar})---')
        new_matriz = []
        constante = Numero_Racional(escalar)
        fila_mult =[]
        for elemento in matriz[fila2-1]:
            fila_mult.append(constante.multiplicar_dividir(elemento))

        for i in range(len(matriz)):
            if i == fila_a_modificar-1:
                new_fila = []
                for j in range(len(fila_mult)):
                    constante2 = Numero_Racional(fila_mult[j])
                    new_fila.append(constante2.sumar_restar(matriz[i][j]))
                new_matriz.append(new_fila)
            else:
                new_matriz.append(matriz[i])
        return new_matriz


class Matriz_Cuadrada(Matriz):

    def __init__(self, nombre, filas):
        super().__init__(nombre, filas=filas, columnas=filas)


    def get_determinante(self):
        return self.determinante(self.elementos)


    def determinante(self, matriz):
        if len(matriz) == 2:
            diag_prin = Numero_Racional(matriz[0][0])
            diag_prin = Numero_Racional(diag_prin.multiplicar_dividir(matriz[1][1]))
            diag_sec = Numero_Racional('-1')
            diag_sec = Numero_Racional(diag_sec.multiplicar_dividir(matriz[0][1]))
            diag_sec = diag_sec.multiplicar_dividir(matriz[1][0])
            return diag_prin.sumar_restar(diag_sec)
        else:
            trayecto, linea = self.recorrido(matriz)
            resultado = Numero_Racional('0')

            for n in range(len(matriz)):
                if trayecto == 'columnas':
                    coeficiente, matriz_menor = self.decompostor(n, linea, matriz)
                    coeficiente = Numero_Racional(coeficiente)
                else:
                    coeficiente, matriz_menor = self.decompostor(linea, n, matriz)
                    coeficiente = Numero_Racional(coeficiente)
                termino = coeficiente.multiplicar_dividir(self.determinante(matriz_menor))
                resultado = Numero_Racional(resultado.sumar_restar(termino))
            return resultado.reprecentacion


    def recorrido(self, matriz):
        trayecto = 'filas'
        linea = 0
        cantid_ceros = 0
        for fila in range(len(matriz)):
            cont_2 = self.contador_ceros('filas', fila, matriz)
            if cont_2 > cantid_ceros:
                trayecto = 'filas'
                linea = fila
                cantid_ceros = cont_2
        for columna in range(len(matriz)):
            cont_2 = self.contador_ceros('columnas', columna, matriz)
            if cont_2 > cantid_ceros:
                trayecto = 'columnas'
                linea = columna
                cantid_ceros = cont_2
        return (trayecto, linea)


    def contador_ceros(self, trayecto, indice, matriz):
        contador = 0
        if trayecto == 'filas':
            for columna in range(len(matriz)):
                if matriz[indice][columna] == '0':
                    contador += 1
            return contador
        else:
            for fila in range(len(matriz)):
                if matriz[fila][indice] == '0':
                    contador += 1
            return contador


    def decompostor(self, fila_cofactor, colum_cofactor, matriz):

        if (fila_cofactor + colum_cofactor) % 2 == 0:
            cofactor = matriz[fila_cofactor][colum_cofactor]
        else:
            sign_negativo = Numero_Racional('-1')
            cofactor = sign_negativo.multiplicar_dividir(matriz[fila_cofactor][colum_cofactor])
        matriz_menor = []
        for i in range(len(matriz)):
            new_fila = []
            for j in range(len(matriz)):
                if i != fila_cofactor and j != colum_cofactor:
                    new_fila.append(matriz[i][j])
            if new_fila != []:
                matriz_menor.append(new_fila)
        return (cofactor, matriz_menor)


    def agregar_Inversa(self, matriz):
        matriz_ejerc = matriz.elementos
        determinante = self.determinante(matriz_ejerc)
        if determinante == '0':
            print('La matriz cuadrada ingresada no tiene inversa')
        else:
            identidad = self.matriz_Identidad(len(matriz_ejerc))
            for columna in range(len(identidad)):
                if matriz_ejerc[columna][columna] == '0':
                    matriz_ejerc = self.permutar_filas(self.fila_optima(columna, columna, matriz_ejerc), columna, matriz_ejerc)
                elem_princip = Numero_Racional(matriz_ejerc[columna][columna])
                matriz_ejerc = self.multiplicar_fila(columna+1, elem_princip.invertirso(), matriz_ejerc)
                identidad = self.multiplicar_fila(columna+1, elem_princip.invertirso(), identidad)
                for fila in range(len(identidad)):
                    if fila != columna:
                        elemento = Numero_Racional(matriz_ejerc[fila][columna])
                        matriz_ejerc = self.sumar_filas(fila+1, columna+1, elemento.multiplicar_dividir('-1'), matriz_ejerc)
                        identidad = self.sumar_filas(fila+1, columna+1, elemento.multiplicar_dividir('-1'), identidad)
            self.elementos = list(identidad)


    def matriz_Identidad(self, dimension):
        matriz = []
        for i in range(dimension):
            fila = []
            for j in range(dimension):
                if i == j:
                    fila.append('1')
                else:
                    fila.append('0')
            matriz.append(fila)
        return matriz


    def fila_optima(self, fila, columna, elementos):
        fila_optima = None
        for i in range(fila+1, len(elementos)):
            if elementos[i][columna] != '0':
                fila_optima = elementos[i][columna]
                break
        return fila_optima


if __name__ == '__main__':
    a = Matriz_Cuadrada('A', 3)
    a.elem_Random()
    a_inv = Matriz_Cuadrada('A^-1', 3)
    a.agregar_Inversa(a)
    a.imprimir_Matriz()