import math
#  ** , / , * , // , + , -

'''
pi=math.pi
r=3
area=pi*r**2
volume=4/3*pi*r**3
reound= round(volume,3)
print (area,volume)
print (reound)
'''


'''
name ="Priyanshu"
bol= True
print(type(name), type(bol))


# splicing ['inclusive','exclusive']

py="PYTHON"
print(py[-4:6]+name[2])  #string concactication & splicing

py2=py[0].lower()+py[1:-2]+py[-1].lower()
print(py2)

#alternating characters Capitalization
py3 = ""

for i in range(len(py2)):
    if i % 2 == 0:
        py3 += py2[i].upper()
    else:
        py3 += py2[i].lower()

print(py3)


# Jython
print ("J"+py[1:])
'''


# elif malnourished   BMI = kg/Height**2   # Height in meters .
bmi=0.4555
if bmi in range(1,15):  #range works with integer only
    #replaces if bmi< > or <bmi< , variation etc . 
    pass
    


# conditional checks |-->  AND , OR . requireing checks for equi , iso , scalene .
x,y,z=input("enter x,y,z:")

if x==y and y==z:
    print("Equilateral")

elif x==y or y==z or x==z:
    print ("Isocales")

elif x!=y and y!=z and x!=z:
    print("Scalene")



# CElcious to Farhennite  -->  C=(F-32)*5/9  # take input celsus as Float , Then Round at end 