# creare una def che si occupi di fare una somma di un valore dato dall'utente, x volte
def decoratore(funzione):
    def wrapper():
        print ("prima")
        funzione()
        print ("dopo")
    return wrapper

class calcolatrice():
    @decoratore
    def somma():
        x = 0
        while True:
            risposta = int(input("inserisci un numero:"))
            x += risposta
            continue_ = input("Vuoi continuare?")
            if continue_ == "no":
               print (x)
               break

calcolo = calcolatrice()
calcolatrice.somma()