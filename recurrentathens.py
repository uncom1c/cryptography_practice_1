# рекуррентнный афинный шифр 
global a,b,alphabet, rec_a, rec_b

a= int(input("Введите а:  "))
b = int(input("Введите b:  "))

alphabet = []

ende = int(input("Поставьте 1 если требуется зашифровать и 2 если расшифровать:  "))
for i in range(97, 123):
    alphabet.append(chr(i))

rec_a =[a, a]
rec_b = [b,b]

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
            f_x = (rec_a[i]*x + rec_b[i]) % m
            out += alphabet[f_x]
        else:
            out+= text[i]
    return out

def decypher(text):
    out = ''
    m = len(alphabet)

    for i in range(len(text)):
        if text[i] in alphabet:
            minusa = find_opposite(rec_a[i],m)

            x = alphabet.index(text[i]) 
            f_x = (minusa * (x + m - rec_b[i]))%m
            out += alphabet[f_x]
        else:
            out+= text[i]
    return out

m = len(alphabet)

text = input("Введите свой текст:    ")
for i in range(len(text)):
    if len(rec_a) == i:
        rec_a.append((rec_a[-1]*rec_a[-2])%m)
    if len(rec_b) == i:
        rec_b.append((rec_b[-1]+rec_b[-2])%m)


if ende == 2:
    print(decypher(text))
elif ende == 1:
    print(encypher(text))
else:
    print("не понял")
    
