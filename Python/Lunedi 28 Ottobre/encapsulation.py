class Conto_Bancario:
    __saldo = 0
    __titolare = ""
    def __init__(self, saldo, titolare):
        self.__saldo = saldo
        self.__titolare = titolare
        
    def deposita(self):
        while True:
            importo_versamento= int(input("quanto vuoi versare? $"))
            if importo_versamento > 0 :
                self.SET_SALDO(importo_versamento)
                break
            else:    
                print ('Per favore inserisci un valore corretto. (maggiore di 0)')
    
    def preleva(self):
        while True:
            importo_prelievo = int(input("quanto vuoi prelevare? $"))
            if (self.__saldo > importo_prelievo):
                self.__saldo -= importo_prelievo
                print (f"hai prelevato ${importo_prelievo}, il tuo nuovo saldo e' ${self.__saldo}")
                break
            elif self.__saldo == importo_prelievo:
                self.__saldo -= importo_prelievo
                print (f"ATTENZIONE, hai prelevato tutto il saldo a tua disposizione. Il tuo nuovo saldo e' ${self.__saldo}")
                break
            else:
                print (f"La somma inserita supera il saldo massimo, riprova. Max prelievo: ${self.__saldo}")
    
    def visualizza_Saldo(self):
        return self.GET_SALDO(self.__saldo)
    
    def visualizza_Titolare(self):
        return self.GET_TITOLARE(self.__titolare)
    def modifica_Titolare(self):
        return self.SET_TITOLARE(self.__titolare)
     
    def GET_SALDO(self, saldo):
        return saldo
    def SET_SALDO(self, nuovo_saldo):
        if(nuovo_saldo > 0):
            self.__saldo += nuovo_saldo
        else:
            pass
        
    def GET_TITOLARE(self, titolare):
        return titolare
    def SET_TITOLARE(self, nuovo_titolare):
        while True:
            nuovo_titolare = input('Per favore inserisci il nuovo nome del titolare: ')
            if nuovo_titolare != self.__titolare:
                self.__titolare = nuovo_titolare
                print (f"Titolare conto cambiato. il nuovo titolare e': {nuovo_titolare}")
                break
            else:
                print (f"Questa persona e' gia titolare del conto.")
                
conto = Conto_Bancario(1000, 'Alessio Simeone')

print (conto.visualizza_Saldo())
print (conto.visualizza_Titolare())
conto.deposita()
conto.preleva()
conto.modifica_Titolare()