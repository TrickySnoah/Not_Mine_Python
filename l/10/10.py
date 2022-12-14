import pickle
import random
import retailitem as tenri
def chungus():
    try:
       inve=open("INV.dat","rb")
       inv=pickle.load(inve)
       inve.close()
    except:
        inve=open("INV.dat","wb")
        inve.close()
        print("the inventory was empty")
    print("menu\n1 to go to the inv\n2 to go to the store")
    opt=input("where do you want to go?")
    if opt=="1":
        password=input("you shall not pass...unless you enter the right password")
        if password=="money":     
            inventory()
        else:
            print("wrong lol")
    elif opt=="2":
        try:
            if inv>0:
                pass
            else:
                bigdangalangcrash=oopsiewhoopsie
        except:
            print("the inv is empty.")
        else:
            store()
def inventory():
    invento=[]
    while True:
        print("menu\n1 to show the inv\n2to add stuff to the inv\n3 to write inv data\n4 to leave")
        opt=input("what do you want to do?")
        if opt=="1":
            showinv()
        elif opt=="2":
            invento=addinv(invento)
        elif opt=="3":
            invento=saveinv(invento)
        else:
            break
def showinv():
    try:
        inve=open("INV.dat","rb")
        inv=pickle.load(inve)
        inve.close()
        if len(inv)<1:
            oopsie=whoopsie
    except:
        print("the inventory is empty.")
        return
    else:
        for obj in inv:
            print(obj)
        return
def addinv(invento):
    while True:
        name=input("what's the name of the item?")
        amount=int(input("how many are there?"))
        price=int(input("how much does it cost?"))
        item=tenri.RetailItem(name,amount,price)
        invento.append(item)
        another=input("Add another? (y/n)")
        if another=="n":
            return invento
def saveinv(invento):
    try:
        inve=open("INV.dat","rb")
        invento2=pickle.load(inve)
        invento+=invento2
        inve.close()
    except:
        pass
    inve=open("INV.dat","wb")
    pickle.dump(invento,inve)
    inve.close()
    return []
def store():
    cart={}
    while True:
        print("menu\n1 to see your cart\n2 to show the inv\n3 to buy something"+
              "\n4 to empty the cart\n5 to checkout")
        opt=input("what do you want to do?")
        if opt=="1":
            cart=seecart(cart)
        if opt=="2":
            showinv2()
        if opt=="3":
            cart=buy(cart)
        if opt=="4":
            cart=empty()
        if opt=="5":
            checkout(cart)
            break
def seecart(cart):
    if len(cart)>0:
        for obj in cart:
            print(f"{cart[obj][0]}\n{cart[obj][2]}\n")
        return cart
    else:
        print("your cart is empty dummy")
        return cart
def showinv2():
    try:
        inve=open("INV.dat","rb")
        inv=pickle.load(inve)
    except:
        print("the inventory is empty.")
        return
    else:
        for obj in inv:
            print(obj)
        return
def buy(cart):
    try:
        inve=open("INV.dat","rb")
        inv=pickle.load(inve)
    except:
        print("the inventory is empty.")
        return cart
    else:
        showinv2()
        while True:
            l=1
            item=input("What do you want to buy?")
            for obj in inv:
                if tenri.RetailItem.name(obj)==item:
                    for ite in cart:
                        if tenri.RetailItem.name(obj)==tenri.RetailItem.name(ite):
                            cart[ite][2]+=1
                            l=0
                            print("you bought something")
                            break
                    if l==1:
                        cart[obj]=[tenri.RetailItem.name(obj),obj,1]
                        print("you bought something")
                        l=0
                        break
            if l==1:
                print("that item doesn't exist dumy")
            else:
                another=input("Buy another? (y/n)")
                if another=="n":
                    break
    return cart
def empty():
    return {}
def checkout(cart):
    seecart(cart)
    continuebuying=input("do you want to buy these thinges? (y/n)")
    if continuebuying=="y":
        print("Thanks for buying stuff")
    else:
        print("Buy something next time")
chungus()