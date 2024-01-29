value1 = int(input())
value2 = int(input())

if value1 < value2:
    for i in range (value1, value2 + 1):
        if i%2 == 0:
            print(str(i) + "pari")
        else:
            print("non ci sono numeri pari")
elif value1 > value2:
    for i in range (value2, value1 + 1):
            if i%2 == 0:
                print(str(i) + "pari")
            else:
                print("non ci sono numeri pari")
else:
    print("I valori inseriti sono uguali")
    