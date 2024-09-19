def descnumber():
    number = int(input("please insert a number --> "))
    for i in range(number, -1, -1):
        print(i)

def repeatexc():
    while True:
        answer = input("Do you want to do it again? 'Y' to proceed --> ")
        if answer == "Y" or answer == "y":
            print("re-executing program.")
            descnumber()
        elif answer != "Y" or answer != "y":
            print("exiting program.")
            break
        
descnumber()
repeatexc()
