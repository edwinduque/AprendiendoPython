import random
class Search:
    def binarySearch(self, arregloOrdenado, numero, intentos):
       
        aux = len(arregloOrdenado)
        if arregloOrdenado[aux//2] > numero:
            intentos += 1
            return self.binarySearch(arregloOrdenado[0:aux//2], numero, intentos) 
        elif arregloOrdenado[aux//2] < numero:
            intentos += 1
            return self.binarySearch(arregloOrdenado[aux//2:], numero, intentos) 
        else:
            return intentos



if __name__ == "__main__":
    search = Search()
    arregloOrdenado =[]
    maximo = 500000
    minimoIntentos = 1000
    maximoIntentos = 0
    for index in range(maximo):
        arregloOrdenado.append(index)
    for veces in range(1000):
        numero = random.randint(0, maximo-1)
        intentos = search.binarySearch(arregloOrdenado, numero, 0)
        if intentos < minimoIntentos:
            minimoIntentos = intentos
            print("Numero ", numero, " nuevo minimo de intentos ", intentos)
        if intentos > maximoIntentos:
            maximoIntentos = intentos
            print("Numero ", numero, " nuevo maximo de intentos ", intentos)
       
     
     
