class MetodoPagamento:
    metodoPagamento = 'Carta di credito'
    test = True
    def effettua_pagamento(self):
        importo = int(input('Inserisci la quantita di denaro che vuoi pagare: $'))
        print (f"hai pagato ${importo} tramite {self.metodoPagamento}")

class ApplePay(MetodoPagamento):
    metodoPagamento = 'Apple Pay'
    def effettua_pagamento(self):
        importo = int(input('Inserisci la quantita di denaro che vuoi pagare: $'))
        print (f"Hai pagato ${importo} tramite {self.metodoPagamento}.")

class PayPal(MetodoPagamento):
    metodoPagamento = 'PayPal'
    def effettua_pagamento(self):
        importo = int(input('Inserisci la quantita di denaro che vuoi pagare: $'))
        print (f"Hai pagato ${importo} tramite {self.metodoPagamento}.")

class BonificoBancario(MetodoPagamento):
    metodoPagamento = 'bonifico bancario'
    def effettua_pagamento(self):
        if BonificoBancario.__test(self):
            importo = int(input('Inserisci la quantita di denaro che vuoi pagare: $'))
            print (f"Hai pagato ${importo} tramite {self.metodoPagamento}.")
        else:
            print ('something went wrong')
               
    def __test(self):
        if self.test == True:
            return True
        else:
            return False
        
def gestorepagamenti(pagamento):
    pagamento.effettua_pagamento()
    
pagamentoBB = BonificoBancario()

gestorepagamenti(pagamentoBB)
