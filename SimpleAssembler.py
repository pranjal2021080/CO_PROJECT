import sys

def bnr(a):
    n = bin(a).replace('0b','')
    x = n[::-1]   
    while len(x) < 8:
        x += '0'
    n = x[::-1]
    return n

A={"add":"10000","sub":"10001","mul":"10110","xor":"11010","or":"11011","and":"11100"}
B={"mov":"10010","rs":"11000","ls":"11001"}
C={"mov":"10011","div":"10111","not":"11101","cmp":"11110"}
D={"ld":"10100","st":"10101"}
E={"jmp":"11111","jlt":"01100","jgt":"01101","je":"01111"}
F={"hlt":"01010"}

reg={"R0":"000","R1":"001","R2":"010","R3":"011","R4":'100',"R5":"101","R6":"110","FLAGS":"111"}

operators=['xor','mov','add','sub','mul','or ','and','ls ','rs ','div','not','cmp','hlt','var','ld ','st ','jmp','jlt','jgt','je ']
variables=[]
labels=[]
labels_pos=[]
lst=[]

#with open("C://Users//Anay//Downloads//test.txt","r") as f:
    #text = f.readlines()
text=sys.stdin.readlines()
for lines in text:
    if lines=="\n":
        continue
    lst.append(lines.strip())
if len(lst) == 0:
    print("[ERROR] NO INSTRUCTIONS GIVEN!")
    quit()
for i in range(len(lst)):
    if lst[i][-1]==":":
        print("[ERROR]INCORRECT LABEL INSTRUCTION!")
        quit()
for i in range(len(lst)):
    l=lst[i].split()
    for j in range(len(l)):
        if l[j].count(":")>1:
            print("[ERROR] NESTED LABELS!")
            quit()
for i in range(len(lst)):
    if lst[i][0]+lst[i][1]+lst[i][2]=="add":
        l1=lst[i].split()
        if len(l1)!=4:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="sub":
        l1=lst[i].split()
        if len(l1)!=4:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="mul":
        l1=lst[i].split()
        if len(l1)!=4:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="xor":
        l1=lst[i].split()
        if len(l1)!=4:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="or ":
        l1=lst[i].split()
        if len(l1)!=4:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="and":
        l1=lst[i].split()
        if len(l1)!=4:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="jmp":
        l1=lst[i].split()
        if len(l1)!=2:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="jlt":
        l1=lst[i].split()
        if len(l1)!=2:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="jgt":
        l1=lst[i].split()
        if len(l1)!=2:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="je ":
        l1=lst[i].split()
        if len(l1)!=2:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="ld ":
        l1=lst[i].split()
        if len(l1)!=3:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="st ":
        l1=lst[i].split()
        if len(l1)!=3:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="div":
        l1=lst[i].split()
        if len(l1)!=3:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="not":
        l1=lst[i].split()
        if len(l1)!=3:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="cmp":
        l1=lst[i].split()
        if len(l1)!=3:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
            quit()
    if lst[i][0]+lst[i][1]+lst[i][2]=="mov":
        l1=lst[i].split()
        if len(l1)!=3:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
    if lst[i][0]+lst[i][1]+lst[i][2]=="rs ":
        l1=lst[i].split()
        if len(l1)!=3:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
    if lst[i][0]+lst[i][1]+lst[i][2]=="ls":
        l1=lst[i].split()
        if len(l1)!=3:
            print("[ERROR]INCORRECT NUMBER OF REGISTERS/VARIABLES!")
for i in range(len(lst)):
    if lst[i].split()[0][-1]==":":
        labels.append(lst[i].split()[0])
        labels_pos.append(i)
        p=lst[i].split()
        str1=''
        for j in range(1,len(p)):
            str1+=p[j]+' '
        lst[i]=str1

num=['0','1','2','3','4','5','6','7','8','9']

#print(lst)

def var():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="var":
            continue
    
def add():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="add":
            return True
    
def sub():    
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="sub":
            return True
def mul():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="mul":
            return True
def xor():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="xor":
            return True

def Or():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="or ":
            return True

def And():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="and":
            return True
def mov1():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="mov":
            if lst[i][-1] in num:
                if lst[i][-2]=="$" or lst[i][-2] in num:
                    return True
def rs():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="rs ":
            return True

def ls():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="ls ":
            return True

def mov2():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="mov":
            if (lst[i][-2]).lower()=="r":
                return True

def div():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="div":
            return True
def Not():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="not":
            return True

def cmp():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="cmp":
            return True
lst1=[]

def jlt():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="jlt":
            return True

def jmp():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="jmp":
            return True

def jgt():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="jgt":
            return True

def je():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="je ":
            return True

def ld():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="ld ":
            return True

def lbl():
    for i in range(len(lst)):
        if lst[i].split()[0][-1]==":":
            return True

def st():
    for i in range(len(lst)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="st ":
            return True
result=[]
error=[]
for i in range(len(lst)):
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="var":
        variables.append(lst[i].split()[1])
    # if lst[i]=='\n':
    #     continue
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="add":
        if add()==True:
            result.append((A["add"])+"00"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]]+reg[lst[i].split()[3]])
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="sub":
        if sub()==True:
            result.append((A["sub"])+"00"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]]+reg[lst[i].split()[3]])
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="cmp":
        if cmp()==True:
            result.append(C["cmp"]+"00000"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]])
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="not":
        if Not()==True:
            result.append(C["not"]+"00000"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]])
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="div":
        if div()==True:
            result.append(C["div"]+"00000"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]])
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="ls ":
        if ls()==True:
            lst[i]=lst[i].replace('$','')
            if int(lst[i].split()[2])<256 and int(lst[i].split()[2])>=0:
                K=(B["ls"]+reg[lst[i].split()[1]])+str(bnr(int(lst[i].split()[2])))
                result.append(K)
            else:
                print("[ERROR] IMM VALUE GREATER THAN 8 BITS!")
                quit()
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="rs ":
        if rs()==True:
            lst[i]=lst[i].replace('$','')
            if int(lst[i].split()[2])<256 and int(lst[i].split()[2])>=0:
                K=(B["rs"]+reg[lst[i].split()[1]])+str(bnr(int(lst[i].split()[2])))
                result.append(K)
            else:
                print("[ERROR] IMM VALUE GREATER THAN 8 BITS!")
                quit()
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="or ":
        if Or()==True:
            result.append((A["or"])+"00"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]]+reg[lst[i].split()[3]])
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="and":
        if And()==True:
            result.append((A["and"])+"00"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]]+reg[lst[i].split()[3]])
    if (lst[i][0]).lower()=="m":
        if lst[i][-1] in num:
            if lst[i][-2]=="$" or lst[i][-2] in num:
                if mov1()==True:
                    lst[i]=lst[i].replace('$','')
                    if int(lst[i].split()[2])<256 and int(lst[i].split()[2])>=0:
                        K=(B["mov"]+reg[lst[i].split()[1]])+str(bnr(int(lst[i].split()[2])))
                        result.append(K)
                    else:
                        print("[ERROR] IMM VALUE GREATER THAN 8 BITS!")
                        quit()
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="mov":
        if (lst[i][-2]).lower()=="r":
            if mov2()==True:
                result.append(C["mov"]+"00000"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]])
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="xor":
        if xor()==True:
            result.append((A["xor"])+"00"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]]+reg[lst[i].split()[3]])
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="mul":
        if mul()==True:
            result.append((A["mul"])+"00"+reg[lst[i].split()[1]]+reg[lst[i].split()[2]]+reg[lst[i].split()[3]])
    for j in range(len(variables)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="st ":
            if st()==True:
                if lst[i].split()[2]==variables[j]:
                    result.append(D["st"]+reg[lst[i].split()[1]]+str(bnr(len(lst)-len(variables)+j)))
                else:
                    print("[ERROR] UNDEFINED VARIABLE ERROR!")
                    quit()
    for j in range(len(variables)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="ld ":
            if ld()==True:
                if lst[i].split()[2]==variables[j]:
                    result.append(D["ld"]+reg[lst[i].split()[1]]+str(bnr(len(lst)-len(variables)+j)))
                else:
                    print("[ERROR] UNDEFINED VARIABLE ERROR!")
                    quit()
    for j in range(len(labels)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="jmp":
            if jmp()==True:
                if lst[i].split()[1]+":"==labels[j]:
                    result.append("11111"+"000"+str(bnr(labels_pos[j])))
                else:
                    print("[ERROR] USE OF UNDEFINED LABEL!")
                    quit()
    for j in range(len(labels)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="jlt":
            if jlt()==True:
                if lst[i].split()[1]+":"==labels[j]:
                    result.append("01100"+"000"+str(bnr(labels_pos[j])))
                else:
                    print("[ERROR] USE OF UNDEFINED LABEL!")
                    quit()
    for j in range(len(labels)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="jgt":
            if jgt()==True:
                if lst[i].split()[1]+":"==labels[j]:
                    result.append("01101"+"000"+str(bnr(labels_pos[j])))
                else:
                    print("[ERROR] USE OF UNDEFINED LABEL!")
    for j in range(len(labels)):
        if (lst[i][0]+lst[i][1]+lst[i][2]).lower()=="je ":
            if je()==True:
                if lst[i].split()[1]+":"==labels[j]:
                    result.append("01111"+"000"+str(bnr(labels_pos[j])))
                else:
                    print("[ERROR] USE OF UNDEFINED LABEL!")

if (lst[-1][0]+lst[-1][1]+lst[-1][2]).lower()=="hlt":
    result.append(F["hlt"]+"00000000000")

def hlt_error_check_1():
    for i in range(len(lst)):
        if (lst[-1][0]+lst[-1][1]+lst[-1][2]).lower()!="hlt":
            return True
        else:
            return False

if hlt_error_check_1()==True:
    print("[ERROR] LAST INSTRUCTION IS NOT HALT!")
    quit()
hlt_lst=[]
for i in range(len(lst)):
    if lst[i][0]+lst[i][1]+lst[i][2]=="hlt":
        hlt_lst.append(i)
if len(hlt_lst)>1:
    print("[ERROR] MULTIPLE HALT INSTRUCTIONS!")
    quit()

for i in range(len(lst)):
    if (lst[i][0]+lst[i][1]+lst[i][2]).lower() not in operators:
        print(f'[ERROR] ILLEGAL INSTRUCTION IN LINE {i+1}')
        quit()


lst3=[]
for i in range(len(lst)):
    lst3.append(lst[i][0]+lst[i][1]+lst[i][2])
if lst3.count("hlt")==0:
    print("[ERROR] HALT INSTRUCTION MISSING!")
    quit()

for i in range(len(lst)):
    for j in range(1,len(lst[i])-2):
        if lst[i][j]+lst[i][j+1]+lst[i][j+2] in operators and lst[i][0]+lst[i][1]+lst[i][2] not in operators:
           print(f"[ERROR] INSTRUCTION IS BEING USED AS VARIABLE OR REGISTER IN LINE {i+1}!")
           quit()

for k in range(len(result)):
    print(result[k])