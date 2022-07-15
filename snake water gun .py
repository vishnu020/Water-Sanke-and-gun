


import random
def matchwin(com,you):
    if com==you:
        return None
    elif com=="w":
        if you=="s":
            return True
        elif you=="g":       
            return False

    elif com=="g":
        if you=="s":
            return True
        elif you=="w":      
            return False 

    elif com=="s":
        if you=="g":
            return True
        elif you=="w":       
            return False             


print("comuter trun: water(w) snake(s) gun(g)")
a= random .randint(1,3)

if a==1:
    com="w"
elif a==2:
    com="s"
elif a==3:
    com="g"   


you=input("your  choise: water(w) snake(s) gun(g)\n") 

b=matchwin(com,you)
print(f"computer choose {com}")
print(f"you choose {you} ")

if(b==None):
    print("tie")
elif (b==True):
    print("you win ")
else: 
    print("you loose")    













