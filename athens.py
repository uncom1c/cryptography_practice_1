# афинный шифр 
global a,b,alphabet

a= int(input("Введите а:  "))
b = int(input("Введите b:  "))

alphabet = []

ende = int(input("Поставьте 1 если требуется зашифровать и 2 если расшифровать:  "))
for i in range(97, 123):
    alphabet.append(chr(i))

def find_opposite(a, m):
    for i in range(m):
        if (a*i)%m == 1:
            return i
        
def encypher(text):
    out = ''
    m = len(alphabet)
    for i in range(len(text)):
        if text[i] in alphabet:
            x = alphabet.index(text[i]) 
            f_x = (a*x + b) % m
            out += alphabet[f_x]
        else:
            out+= text[i]
    return out

def decypher(text):
    out = ''
    m = len(alphabet)
    minusa = find_opposite(a,m)

    for i in range(len(text)):
        if text[i] in alphabet:
            x = alphabet.index(text[i]) 
            f_x = (minusa * (x + m - b))%m
            out += alphabet[f_x]
        else:
            out+= text[i]
    return out

text = input("Введите свой текст:    ")

if ende == 2:
    print(decypher(text))
elif ende == 1:
    print(encypher(text))
else:
    print("не понял")
    
