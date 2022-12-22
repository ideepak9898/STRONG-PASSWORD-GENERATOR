#This project is on generating strong password of minimum length of 10 unit

import random
Num = random.randint(10,16)

Upper =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

Lower =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

Number =['0','1','2','3','4','5','6','7','8','9']

Special = ['$','%','!','@','#','&','~','<','>','?','/','*','|']

Total = Special + Lower + Upper + Number
# atleast one character of all type
Pass = random.choice(Special) +random.choice(Lower) +random.choice(Upper) +random.choice(Number) 

for i in range (Num-4):
    a = random.choice(Total)
    Pass = Pass + a
print(Pass)
