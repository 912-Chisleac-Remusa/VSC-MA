import matplotlib.pyplot as plt
import numpy as np

#Range of numbers
domain=np.linspace(-100,100,10000)
niu=0.6

def f1(x):
    #return 0.05*x**2
    return 10*np.sin(0.1*x+10)

def f1_der(x):
    #return 0.01*2*x
    return np.cos(0.1*x+10)

def gen_seq():
    global niu
    domain_n=[50]
    for i in range(1,301):
        domain_n.append(domain_n[i-1]-niu*f1_der(domain_n[i-1]))
    return domain_n


def print_plot():
    y=[]
    for x in domain:
        y.append(f1(x))

    domain_n=gen_seq()
    y_n=[]
    for x in domain_n:
        y_n.append(f1(x))


    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(10,10))

    plt.axis('square')
    plt.xticks([i for i in range(-100,101,10)])
    plt.yticks([i for i in range(-100,101,10)])


    plt.plot(domain,y)
    plt.plot(domain_n[300],y_n[300],"ro")
    plt.legend()
    plt.show()
    pass

def main():
    global niu
    while True:
        print("====Menu====")
        print("[1]. Set niu")
        print("[2]. Print grapf")
        print("[0]. Exit")
        print()
        print("[ ]: ",end="")

        dialog=int(input())

        if dialog == 1:
            niu=float(input("niu: "))
        elif dialog == 2:
            print_plot()
        else:
            break

main()

