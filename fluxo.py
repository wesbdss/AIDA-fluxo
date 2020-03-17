import yaml
import random
import logging

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
    def __init__(self,diretory="fluxo.yaml"):
        self.diretory = diretory
        logging.debug("{} - {}".format(self.__class__,"Fluxo Carregado {}".format(diretory)))
        
    
    def main(self):
        with open(self.diretory,'r') as f:
            self.states = yaml.load(f.read(),Loader=yaml.FullLoader)
        self.state = self.states['init']
        self.checkState()
        print(self.responseState())

    def restartState(self):
        self.state = self.states['init']
        logging.debug("{} - {}".format(self.__class__,"Fluxo Resetado"))

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
        logging.debug("{} - {}".format(self.__class__,"Proximo Estado"))
        
        if "output" not in self.states[self.state].keys():
            logging.debug("{} - {}".format(self.__class__,"Encerrar Fluxo"))
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
                plogging.debug("{} - {}".format(self.__class__,"Não Há um Proximo estado"))
                exit(1)

    def checkState(self):
        if self.state in self.states.keys():
            return True
        else:
            logging.debug("{} - {}".format(self.__class__,"Label não existente ou estado inválido"))
            exit(1)
if if __name__ == "__main__":
    a = Fluxo()
    a.main()
