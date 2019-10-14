import math  
from random import shuffle 
from random import randint

global vetorClasses
vetorClasses = []


#Função que le o arquivo.
def readDataFun(fileName): 
  
    data = [] 
    f = open(fileName, 'r') 
    lines = f.read().splitlines()
    f.close() 

    for i in range(0, len(lines)): 
        line = lines[i];
        data.append(line) 

    return data 

#Função que calcula a distância euclidiana dos pontos.
def EuclideanDistance(x,y):
    distance = 0

    a = x.split(' ')
    b = y.split(' ')[:-1]

    for i in range(0,(len(a)-1)):
        distance += math.pow(float(a[i]) - float(b[i]),2) 

    return (math.sqrt(distance), y[-1])

#Função de classificação.
def classify(feature,k,training):
    global vetorClasses
    distancias = []
    for i in training:
        distancias.append(EuclideanDistance(feature,i))
    distancias.sort()    

    for i in range(0,k):
        vetorClasses[int(distancias[i][1])] += 1
    
    maior = 0
    for i in range(len(vetorClasses)):
        if vetorClasses[i] >= vetorClasses[maior]:
            maior = i
    clearArray()        
    return maior

#Função que limpa o vetor de classes.
def clearArray():
    for i in range(len(vetorClasses)):
        vetorClasses[i] = 0

#Função que separa treino e teste.
def FoldsFun(k,data,iterations):
    corrects = 0.0
    total = len(data)
    matrix = [[0 for x in range(10)] for y in range(10)] 

    training = data[iterations:len(data)]
    test = data[0:iterations]

    for item in test:
        itemClass = item[-1]
        feature = item[:-1]
        
        deduction = classify(feature,k,training)

        if(float(deduction) == float(itemClass)):
            corrects += 1
            matrix[int(itemClass)][int(deduction)] += 1
        else:
            matrix[int(itemClass)][int(deduction)] += 1

    print("")
    print("------Matriz de Confusão------")
    print(" 0  1  2  3  4  5  6  7  8  9  = LABEL")
    for i in range(0,10):
        print(matrix[i], end="")
        print(" =",i)
    print("")
        
    accuracy = corrects / iterations
    return accuracy

#Função que devolve a porcentagem de acerto.
def accuracyFun(k,data,iterations):
    accuracy = 0.0
    shuffle(data)

    accuracy = FoldsFun(k, data,iterations)
    print("Accuracy: %f" % accuracy)
  
#Função main.
def main():
    global vetorClasses

    data = readDataFun('treinamento.txt')

    print("Digite um valor para [K]:", end="")
    k = input()

    print("\n[1] você escolher o folds [2] aleatorio entre 25%,50%,75%:", end="")
    tmp = input()

    if(int(tmp) == 1):
        print("Digite um valor para [Folds]:", end="")
        folds = input()
    else:
        tmp = (randint(0,100))

        if(tmp < 33):
            var = 25
            folds = (25 * len(data))/100
        elif(33 < tmp < 66):
            var = 50
            folds = (50 * len(data))/100
        elif(66 < tmp):
            var = 75
            folds = (75 * len(data))/100

        print("Porcentagem escolhida: %d" % var, end="")
        print("%")

    for i in range(0,10):
        vetorClasses.append(0)

    accuracyFun(int(k),data,int(folds))
  
if __name__ == '__main__': 
    main() 