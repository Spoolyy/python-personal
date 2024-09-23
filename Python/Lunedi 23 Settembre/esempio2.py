crud = []
choice = input("scegli un opzione fra: 1 | aggiungi , 2 | rimuovi , 3 | modifica , 4 | pulisci :")

if choice == "1":
    add_word = input("scrivi la parola")
    crud.append(add_word)
elif choice == "2":
    crud.clear()
elif choice == "3":
    if len(crud) > 0:
        y = len(crud)
        wordindex = int(input("Scrivi la posizione della parola da modificare:"))
        newword = input("Scrivi la nuova parola")
        crud[wordindex] = newword
else:
    choice2 = input("vuoi continuare?")
    if choice2 == "no":
        pass
    else:
        pass
    