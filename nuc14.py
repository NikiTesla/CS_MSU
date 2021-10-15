import matplotlib.pyplot as plt
import numpy as np
import math

def Gauss(x,m,d):
    return ((2*math.pi*d*d)**-0.5)*math.exp(-(x-m)**2/(2*d**2))
def Puasson(x,m):
    return (m**x/math.factorial(x))*math.exp(-m)
    

def read(filename):
    p=open(filename,"r")
    S=p.readlines()

    for i in range(len(S)):
        S[i]=int(S[i])
    p.close()  
     
    return S

def middle(X):
    return sum(X)/len(X)

def sigma(X):
    m=middle(X)
    N=len(X)
    n=N*(N-1)
    s=0

    for i in range(N):
        s+=(X[i]-m)**2

    return (s/n)**0.5

def writeinf(X):
    m=middle(X)
    d=sigma(X)

    print("среднее число частиц: ",m)
    print("стандартное отклонение среднего: ",d)
    print("стандартное отклонение среднего по пуассону: ",(m/100)**0.5)
    print("скорость счёта: ",m/30," +- ",d/30,"\n")

def den(X):   
    dict={i:X.count(i) for i in range(min(X),max(X)+1)}

    return dict

def graph(X,A,B,M,S):
    m=middle(X)
    d=sigma(X)

    fig=plt.figure()
    
    plt.axis([A,B,0,M+3])
    plt.xlabel("k",fontsize=20)
    plt.ylabel(r"$n_k$",fontsize=20)

    R=len(den(X).keys())
    plt.hist(X,bins=R)

    L=[i for i in range(A,B)]
    P=[100*Puasson(i,m) for i in L]
    G=[100*Gauss(i,m,(m)**0.5) for i in L]

    plt.plot(L,P,"k*")
    plt.plot(L,G,"r")
    plt.legend(["распределение Пуассона","распределение Гаусса","количество событий"])
    plt.grid(True)
    plt.title(S)
    plt.plot()
    plt.show()

def F(x,X):
    D=den(X)
    s=0
    x=int(math.ceil(x))
    for key in D:
        if key<=x:
            s+=D[key]
        else: break    
    return s/100

def plotF(X,A,B):
    L=[i/100 for i in range(100*A,100*B)]
    U=[F(i,X) for i in L]
    plt.plot(L,U)
    
def printtable(X):
    D=den(X)
    for key in D:
        print(key," ",D[key])

        
        
X1=read("ex1.txt")
X2=read("ex2.txt")

writeinf(X1) 
writeinf(X2)

A=min(X1)
B=max(X2)+1 
M=max(den(X1).values())

graph(X1,A,B,M,"Гистограмма распределения в упр.1")
graph(X2,A,B,M,"Гистограмма распределения в упр.2")

print("таблица частот 1 упр: \n")
printtable(X1)
print("таблица частот 2 упр: \n")
printtable(X2)

fig=plt.figure()

plotF(X1,A,B)
plotF(X2,A,B)

plt.grid(True)
plt.legend(["Упр.1","Упр.2"])
plt.title("Эмпирические функциии распределения")
plt.xlabel("x",fontsize=20)
plt.ylabel("F(x)",fontsize=20)
plt.show()

DF=[abs(F(i,X2)-F(i,X1)) for i in range(A,B) ]

print("таблица для функций распределения")

for i in range(A,B):
    F1=F(i,X1)
    F2=F(i,X2)
    print(i," ",int(100*F1)," ",F1," ",int(100*F2)," ",F2," ",DF[i-A])

D=max(DF)
t=(50**0.5)*D

print("значение статистики: ",t)
