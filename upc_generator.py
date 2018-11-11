import random

print('UPC CODE GENERATOR')
UPC = []
i=0
f = open("upclist.txt","w")
limit = int(input("Limit:"))
while (i<limit):
    i +=1
    number = random.randint(100000000000,999999999999)

    example = str(number)

    a = example[0]
    b = example[11]
    a = int(a)
    b = int(b)

    c1 = example[1]
    c2 = example[2]
    c3 = example[3]
    c4 = example[4]
    c5 = example[5]
    c1 = int(c1)
    c2 = int(c2)
    c3 = int(c3)
    c4 = int(c4)
    c5 = int(c5)

    d1 = example[6]
    d2 = example[7]
    d3 = example[8]
    d4 = example[9]
    d5 = example[10]
    d1 = int(d1)
    d2 = int(d2)
    d3 = int(d3)
    d4 = int(d4)
    d5 = int(d5)


    r1 = a + c2 + c4 + d1 + d3 + d5
    r2 = r1*3

    r3 = c1 + c3 + c5 + d2 + d4
    r4 = r2 + r3 
    r5 = r4 + b
    
    if(r5%10==0):
        UPC.append(number)
        f.write(str(number) + '\n')
        print("Successful")
    else:
        print("Fail")

print("UPC:{}".format(UPC))
f.close()
