input('Welcomn to the worlds best love calculator.\n')
name_1=input("Enter your name please: \n")
name_2=input("Enter your lovers name please: \n")
name_1x=name_1.lower()
name_2x=name_2.lower()
a_1=name_1x.count("t")
a_2=name_1x.count("r")
a_3=name_1x.count("u")
a_4=name_1x.count("e")
a_5=name_1x.count("l")
a_6=name_1x.count("o") 
a_7=name_1x.count("v")
a_8=name_1x.count("e")
b_1=name_2x.count("t")
b_2=name_2x.count("r")
b_3=name_2x.count("u")
b_4=name_2x.count("e")
b_5=name_2x.count("l")
b_6=name_2x.count("o")
b_7=name_2x.count("v")
b_8=name_2x.count("e")
count_1=str(a_1+a_2+a_3+a_4+a_5+a_6+a_7+a_8)
count_2=str(b_1+b_2+b_3+b_4+b_5+b_6+b_7+b_8)
print(f"Total love percentage = ${count_1 +count_2}%")











print(name_1x , name_2x)