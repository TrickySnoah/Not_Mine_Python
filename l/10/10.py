import pickle
import random
def menu():
   try:
       inve=open("INV.dat","rb")
       inv=pickle.load(inve)
       inve.close()
    except:
        inve=open("INV.dat","wb")
        inve.close()
        print("the inventory was empty")
    if len(inv)>0:
        print("menu\n1 to go to the inv\n2 to go to the store")
        opt=input("where do you want to go?")
        if opt=="1":
            inventory()
        elif opt=="2":
            store()
def inventory():
    print('menu\n1 to show the inv\n2to add stuff to the inv\n3 to save the inv\n4 to leave