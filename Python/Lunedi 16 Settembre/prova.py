import newfile
print ("Ciao!")

x = "mirko"

def decoratore(funzione):
    def wrapper():
        print ("io vengo prima della funzione")
        funzione()
        print ("io vengo dopo la funzione")
    return wrapper

def decoratore2(funzione):
    def wrapper():
        print ("Secondo round! io vengo prima della funzione")
        funzione()
        print ("Secondo round! io vengo dopo la funzione")
    return wrapper

@decoratore
@decoratore2


def stampa_var():
    print ("mirko")

stampa_var()

x = newfile.calcolatrice()
x.somma()