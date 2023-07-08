import sys

A={"10000":"add","10001":"sub","10110":"mul","11010":"xor","11011":"or","11100":"and"}
B={"10010":"mov","11000":"rs","11001":"ls"}
C={"10011":"mov","10111":"div","11101":"not","11110":"cmp"}
D={"10100":"ld","10101":"st"}
E={"jmp":"11111","jlt":"01100","jgt":"01101","je":"01111"}
F={"hlt":"01010"}

reg={"000":"R0","001":"R1","010":"R2","011":"R3",'100':"R4","101":"R5","110":"R6","111":"FLAGS"}

operators=['xor','mov','add','sub','mul','or ','and','ls ','rs ','div','not','cmp','hlt','var','ld ','st ','jmp','jlt','jgt','je ']

with open('C://Users//Anay//simtest01.txt','r') as f:
    text=f.readlines()

lst=[]
for line in text:
    lst.append(line.strip())
print(lst)

reg1={'R0':'00000001','R1':'00000000','R2':'00000000','R3':'00000000','R4':'00000000','R5':'00000000','R6':'00000000','FLAGS':'00000000'}

def bnr(a):
    n = bin(a).replace('0b','')
    x = n[::-1] 
    while len(x) < 8:
        x += '0'
        n = x[::-1]
    return n

def bnr1(a):
    n = bin(a).replace('0b','')
    x = n[::-1]
    while len(x)<16:
        x += '0'
        n = x[::-1]
    return n

def addition(a,b):
    if int(a,2)+int(b,2)<256:
        res=(bnr(int(a,2)+int(b,2)))
        return res

def subtraction(a,b):
    if int(a,2)-int(b,2)>=0:
        res=(bnr(int(a,2)-int(b,2)))
        return res

def multiplaction(a,b):
    res=(bnr(int(a,2)*int(b,2)))
    return res

def XOR(a,b):
    res=(bnr(int(a,2)^int(b,2)))
    return res

def OR(a,b):
    res=(bnr(int(a,2) | int(b,2)))
    return res

def AND(a,b):
    res=(bnr(int(a,2) & int(b,2)))
    return res

def RS(a,b):
    a=bnr(int(a,2)>>int(b,2))
    return a

def LS(a,b):
    a=bnr(int(a,2)<<int(b,2))
    return a

def NOT(a):
    L=[]
    str1=''
    for i in range(len(a)):
        L.append(a[i])
    for j in range(len(L)):
        if L[j]=='0':
            str1+='1'
        elif L[j]=='1':
            str1+='0'
    return str1

def CMP(a,b):
    if int(a,2)>int(b,2):
        FLAGS='00000001'
    return FLAGS

def DIV(a,b):
    if int(b,2)!=0:
        Q=bnr(int(a,2)//int(b,2))
    return Q


flag=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
for i in range(len(lst)):
    if lst[i][0:5]=='10000':
        PC=i
        if (int(reg1[reg[lst[i][7:10]]],2)+int(reg1[reg[lst[i][10:13]]],2))<=255:
            reg1[reg[lst[i][13::]]]=addition(reg1[reg[lst[i][7:10]]],reg1[reg[lst[i][10:13]]])
            flag[-4]=='0'
        else:
            if flag[-4]=='1':
                flag[-4]='1'
            elif flag[-4]=='0':
                flag[-4]='1'
        flag_res=''
        for j in range(len(flag)):
            flag_res+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res)
    if lst[i][0:5]=='10001':
        PC=i
        if (int(reg1[reg[lst[i][7:10]]],2)-int(reg1[reg[lst[i][10:13]]],2))>=0:        
            reg1[reg[lst[i][13::]]]=subtraction(reg1[reg[lst[i][7:10]]],reg1[reg[lst[i][10:13]]])
            flag[-4]='0'
        else:
            if flag[-4]=='1':
                flag[-4]='1'
            elif flag[-4]=='0':
                flag[-4]='1'
        flag_res1=''
        for j in range(len(flag)):
            flag_res1+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res1)
    if lst[i][0:5]=='10110':
        PC=i
        if int(reg1[reg[lst[i][7:10]]],2)*int(reg1[reg[lst[i][10:13]]],2)<=255:
            reg1[reg[lst[i][13::]]]=multiplaction(reg1[reg[lst[i][7:10]]],reg1[reg[lst[i][10:13]]])
            flag[-4]='0'
        else:
            if flag[-4]=='1':
                flag[-4]='1'
            elif flag[-4]=='0':
                flag[-4]='1'
        flag_res2=''
        for j in range(len(flag)):
            flag_res2+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res2)
    if lst[i][0:5]=='11010':
        PC=i
        reg1[reg[lst[i][13::]]]=XOR(reg1[reg[lst[i][7:10]]],reg1[reg[lst[i][10:13]]])
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        flag_res3=''
        for j in range(len(flag)):
            flag_res3+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res3)
    if lst[i][0:5]=='11011':
        PC=i
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        reg1[reg[lst[i][13::]]]=OR(reg1[reg[lst[i][7:10]]],reg1[reg[lst[i][10:13]]])
        flag_res4=''
        for j in range(len(flag)):
            flag_res4+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res4)
    if lst[i][0:5]=='11100':
        PC=i
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        reg1[reg[lst[i][13::]]]=AND(reg1[reg[lst[i][7:10]]],reg1[reg[lst[i][10:13]]])
        flag_res5=''
        for j in range(len(flag)):
            flag_res5+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res5)
    if lst[i][0:5]=='11000':
        PC=i
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        reg1[reg[lst[i][5:8]]]=RS(reg1[reg[lst[i][5:8]]])
        flag_res6=''
        for j in range(len(flag)):
            flag_res6+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res6)   
    if lst[i][0:5]=='11001':
        PC=i
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        reg1[reg[lst[i][5:8]]]=LS(reg1[reg[lst[i][5:8]]])
        flag_res7=''
        for j in range(len(flag)):
            flag_res7+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res7)
    if lst[i][0:5]=='11101':
        PC=i
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        reg1[reg[lst[i][13::]]]=NOT(reg1[reg[lst[i][10:13]]])
        flag_res8=''
        for j in range(len(flag)):
            flag_res8+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res8)
    if lst[i][0:5]=='10010':
        PC=i
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        reg1[reg[lst[i][5:8]]]=str(lst[i][8::])
        flag_res9=''
        for j in range(len(flag)):
            flag_res9+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res9)
    if lst[i][0:5]=='10011':
        PC=i
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        reg1[reg[lst[i][13::]]]=(reg1[reg[lst[i][10:13]]])
        flag_res10=''
        for j in range(len(flag)):
            flag_res10+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res10)
    if lst[i][0:5]=='11110':
        PC=i
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        if reg1[reg[lst[i][10:13]]]<reg1[reg[lst[i][13::]]]:
            flag[-3]='1'
        elif reg1[reg[lst[i][10:13]]]>reg1[reg[lst[i][13::]]]:
            flag[-2]='1'
        elif reg1[reg[lst[i][10:13]]]==reg1[reg[lst[i][13::]]]:
            flag[-1]='1'
        flag_res11=''
        for j in range(len(flag)):
            flag_res11+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res11)
    if lst[i][0:5]=='10111':
        PC=i
        flag[-4]='0'
        flag[-3]='0'
        flag[-2]='0'
        flag[-1]='0'
        if int(reg1[reg[lst[i][13::]]],2)!=0:
            reg1['R0']=DIV(reg1[reg[lst[i][10:13]]],reg1[reg[lst[i][13::]]])
            reg1['R1']=bnr(int(reg1[reg[lst[i][10:13]]],2)-int(reg1['R0'])*int(reg1[reg[lst[i][13::]]]))
        flag_res12=''
        for j in range(len(flag)):
            flag_res12+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res12)
    if lst[i][0:5]=='10100':
        PC=i
        reg1[reg[lst[i][5:8]]]=lst[i][8::]
        flag_res13=''
        for j in range(len(flag)):
            flag_res13+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res13)
    if lst[i][0:5]=='10101':
        PC=i
        lst[i][8::]=reg1[reg[lst[i][5:8]]]
        flag_res14=''
        for j in range(len(flag)):
            flag_res14+=flag[j]
        print(str(bnr(PC))+' '+'00000000'+str(reg1['R0'])+' '+'00000000'+str(reg1['R1'])+' '+'00000000'+str(reg1['R2'])+' '+'00000000'+str(reg1['R3'])+' '+'00000000'+str(reg1['R4'])+' '+'00000000'+str(reg1['R5'])+' '+'00000000'+str(reg1['R6'])+' '+flag_res14)


lst1=[]
for i in range(len(lst)):
    lst1.append(lst[i])
for i in range(len(lst)):
    if lst[i][0:5]=='10101' or lst[i][0:5]=='10100':
        lst1.append('00000000'+lst[i][8::])
while len(lst1)<256:
    lst1.append('0000000000000000')

for k in range(len(lst1)):
    print(lst1[k])
