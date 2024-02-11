#шифр простой подстановки (шифр цезаря)
# так же можно сделать ввод секретного алфавита вручную

alphabet=[]
for i in range(97, 123):
    alphabet.append(chr(i))



secretalphabet=[]
for i in range(98, 123):
    secretalphabet.append(chr(i))

secretalphabet.append(chr(97))
print(secretalphabet)
a = input("Введите свою строку на латинице:  ")
b= int(input("Поставьте 1 если требуется зашифровать и 2 если расшифровать:  "))


def encypher(a):
    out = ''

    for i in range(len(a)):
        if ord(a[i])<123 and ord(a[i])>96:
            out +=secretalphabet[alphabet.index(a[i])]
        else:
            out+=a[i]
    return out
    
def decypher(a):
    out = ''

    for i in range(len(a)):
        if ord(a[i])<123 and ord(a[i])>96:
            out +=alphabet[secretalphabet.index(a[i])]
        else:
            out+=a[i]
    return out

if b == 2:
    print(decypher(a))
elif b == 1:
    print(encypher(a))
else:
    print("не понял")

