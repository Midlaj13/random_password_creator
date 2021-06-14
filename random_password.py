import random
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["!","@","#","$","%","&","*","+"]

print("create a wonderful password")
a=int(input("no. of letters"))
b=int(input("how many numbers?"))
c=int(input("number of symbols?"))
password=[]
for a in range (1,a+1):
    password.append(random.choice(alphabets))
    
for b in range (1,b+1):
    password.append(random.choice(numbers))
for c in range (1,c+1):
    password.append(random.choice(symbols))

random.shuffle(password)

pss=""
for char in password:
    pss+=char

print(f"your password is {pss}")