import numpy as np


class Aspirador:


    status = ["clean", "dirty"]
    positions = [0, 1, 2, 3]
    t = len(positions)

    floor = [1] * t
    floor = np.array(floor)

    '''Localização do aspirador'''
    contPosition = 0
    '''Valor da posição'''
    myPosition = positions[contPosition]
    '''Status em String na posição'''
    statusFloorPosition = status[floor[myPosition]]


    def dropFloor(self):
        cont = 0
        for i in self.floor:
            n = np.random.choice(2)
            self.floor[cont] = n
            cont += 1
        print(self.floor)


    def getFloor(self):
        floorStatus = []
        for i in self.floor:
            floorStatus.append(self.status[i])
        return (floorStatus)


    def escolherIntervencao(self):
        limpar = 's'
        while (limpar != 'n' and limpar != 'N'):
            limpar = input('\nDeseja sujar ou limpar alguma área (digite s ou n): ')
            if (limpar == 's' or limpar == 'S'):

                print("\n-------------------------------------------")
                print("Esse é a situação de sujeira em todo o chão")
                f = self.getFloor()
                print(f)
                print("-------------------------------------------")

                p = input("\nQual posição deseja alterar o status [0 a 3]: ")
                p = int(p)

                if (p >= 0 and p <= self.t):
                    if self.floor[p] == 1:
                        self.floor[p] = 0
                        print("------------------")
                        print("Ambiente foi limpo")
                        print("------------------")
                    else:
                        self.floor[p] = 1
                        print("------------------")
                        print("Ambiente foi sujo")
                        print("------------------")
                else:
                    print("Digite uma posição válida")
            elif (limpar != 'n' and limpar != 'N'):
                print("Digite um valor válido")
            else:
                print("Ação de modificação de ambiente finalizada")


    def andarAgente(self):
        self.contPosition += 1


    def acaoAgente(contPosition, floor):
        print(floor)
        if (floor[contPosition] == 0):
            print("Ambiente limpo. Agente passando para o seguinte")
            contPosition.andarAgente(contPosition)
            print(contPosition)
        else:
            floor[contPosition] = 0
            print("Ambiente sujo. Agente Limpando ambiente")
            print(floor)


    def limpar(condPosition, t):
        while (condPosition <= t):
            condPosition.acaoAgente(condPosition)
        else:
            t = 0
            print("Todos os ambiente estão limpos. O agente voltou para posição inicial")


aspirador = Aspirador()

print(aspirador.floor)
aspirador.escolherIntervencao()
print(aspirador.floor)
