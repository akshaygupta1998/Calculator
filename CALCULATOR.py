Expression=input("Expression:")
num=["1","2","3","4","5","6","7","8","9","0"]
operands=["+","-","/","*"]
p=["(",")","."]
Expression=Expression.replace(" ","")

for j in range(len(Expression)):
    if Expression[j] not in num and Expression[j] not in operands and Expression[j] not in p:
        print("Expression is not right!!!")
        break

list=[]

for k in range(len(Expression)):
    list.append(Expression[k])

def operation(n1,n2,operand):
    if operand=="+":
        return str(float(n1)+float(n2))
    elif operand=="-":
        return str(float(n1)-float(n2))
    elif operand=="*":
        return str(float(n1)*float(n2))
    elif operand=="/":
        if n2==0:
            print("Number not divisible by 0")
        else:
            return str(float(n1)/float(n2))

a=0
while a< len(list)-1:
    if list[a] in num and list[a+1]=="(":
        print("Expression is not right!!")
        break
    if list[a] in num and list[a+1] in num:
        list[a]+=list[a+1]
        del list[a+1]
    elif list[a] in num and list[a+1]==".":
        if list[a+2] in num:
            list[a]+=list[a+1]+list[a+2]
            del list[a+1]
            del list[a+1]
        else:
            print("Expression is not right!")
            break
    else:
        a=a+1
print(list)
l=["(",")"]
while len(list)!=1:
    b=0
    while b<len(list):
        if list[b]=="(":
            if list[b+2]==")":
                del list[b]
                del list[b+1]
        b=b+1
    b=0
    while b<len(list):
        if list[b] in ["*","/"]:
            if (list[b-1]) not in l and (list[b+1]) not in l:
                list[b-1]=operation(list[b-1],list[b+1],list[b])
                del list[b+1]
                del list[b]
            else :
                pass
        b=b+1
    b=0
    while b<len(list):
        if list[b] in ["+","-"]:
            if (list[b-1]) not in l and (list[b+1]) not in l:
                list[b-1]=operation(list[b-1],list[b+1],list[b])
                del list[b+1]
                del list[b]
            else:
                pass
        # print(list)
        b=b+1

print(list[0])