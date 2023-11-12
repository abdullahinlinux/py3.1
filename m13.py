
print('Welcomn to the worlds best love calculator.\n')
name_1=input("Enter your name please: \n")
name_2=input("Enter your lovers name please: \n")
name_x=str(name_1)+str(name_2) 
name = name_x.lower()
print(name)
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
true=str(t+r+u+e)
love=str(l+o+v+e)
true_love=true+love
print(f"Total love percentage = ${true_love}%")
if (true_love<31):
    print(f"Too low level love. You need to buy ${95-true_love} kg love")
elif (true_love>30 and true_love<50):
    print(f"Your love is too few. Need more${90-true_love} kg love to love each other deeply.")
elif(true_love>50 and true_love<80):
 print(f"Not enough love. Need more${85-true_love} kg love between each other.")
else:
 print("You two are already in a true love.")
