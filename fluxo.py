import yaml
import random

# 
#  A estrutura
# 

# init: LABEL

# label:
#   response: "RESPOSTA"
#   output:
#     label1: "LABEL"
#     label2: "LABEL"



class Fluxo:
    def __init__(self):
        pass
    
    def main(self,dir = 'fluxo.yaml'):
        with open(dir,'r') as f:
            self.states = yaml.load(f.read(),Loader=yaml.FullLoader)
        self.state = self.states['init']
        self.checkState()
        print(self.responseState())

    def restartState(self):
        self.state = self.states['init']

    def responseState(self):
        if "response" not in self.states[self.state].keys():
            print(self.__class__,"Não Há resposta disponível")
        response = ''
        if type(self.states[self.state]['response']) == list:
            response = self.states[self.state]['response']
            response = response[random.randrange(0,len(self.states[self.state]['response']))]
        else: 
            response = self.states[self.state]['response']
        return response
    def nextState(self,intent):
        if "output" not in self.states[self.state].keys():
            print(self.__class__,"Encerrar chabot")
            exit(0)

        if intent in self.states[self.state]['output'].keys():
            self.state = self.states[self.state]['output'][intent]
            self.checkState()
        else:
            intent="empty"
            if intent in self.states[self.state]['output'].keys():
                self.state = self.states[self.state]['output'][intent]
                self.checkState()
            else:
                print(self.__class__,"Não há um proximo estado")
                exit(1)

    def checkState(self):
        if self.state in self.states.keys():
            return True
        else:
            print(self.__class__,"Label Não existente, estado inválido")
            exit(1)
a = Fluxo()
a.main()