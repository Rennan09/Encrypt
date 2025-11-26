from random import randint
variability = randint(1,20)

print("="*100)
base = str(input(f" Welcome! Please write the text to be encrypted: "))

Ph1 = base.lower()
table = []

vlang = {
         " ": "0",
         "A": "1-",
         "E": "9",
         "I": "8",
         "O": "7",
         "U": "6",
         "a": "1",
         "e": "2",
         "i": "3",
         "o": "4",
         "u": "5"}

clang = {
         "b": 1 ,
         "c": 2 ,
         "d": 3 ,
         "f": 4 ,
         "g": 5 ,
         "h": 6 ,
         "j": 7 ,
         "k": 8 ,
         "l": 9 ,
         "m": 10,
         "n": 11,
         "p": 12,
         "q": 13,
         "r": 14,
         "s": 15,
         "t": 16,
         "v": 17,
         "w": 18,
         "x": 19,
         "y": 20,
         "z": 21,}

def Slicing (order):
    for chr in order:
        if chr in vlang:
            subs = vlang.get(chr)
            order = order.replace(chr, subs)
        else:
            continue
    global final
    final = order
    order = ""
def Washing (Ph1):
    global order
    menu = {v:k for k,v in clang.items()}
    for chr in Ph1:
        if chr in clang:
            food = int(clang.get(chr)) + variability
            if food > 21:
               food = food % 21
            food = menu.get(food)
            table.append(food)
            #Ph1 = Ph1.replace(chr, food) Maybe in the future.
        else:
            table.append(chr)
            continue
    order = "".join(table)
    table.clear()

base = str(input)
Washing (Ph1)
Slicing (order)
print("="*100)
print (final + "0" + str(variability) )
print("="*100)
working = True

while working == True:
        ask = str(input("Do you want to encrypt another text? (Y/N)"))
        if ask == "N" or ask == "n":
            working = False
            break
        if ask == "Y" or ask == "y":
            base = str(input("Write the text here: "))
            Ph1 = base.lower()
            Washing (Ph1)
            Slicing (order)
            print("="*100)
            print (final + "0" + str(variability) )
            print("="*100)
        else:
            print("Invalid input! Please, try again using Y or N.")

                
print("="*100)
print("Thanks for using me, bye!")
print("="*100)
