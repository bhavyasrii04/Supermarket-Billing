from datetime import datetime

name=input("Enter your name:")
#Lists of items
lists='''
Rice     Rs 20/kg
Sugar    Rs 30/kg
Salt     Rs 20/kg
oil      Rs 110/liter
paneer   Rs 80/kg
Maggi    Rs 50/each
Boost    Rs 90/each
colgate  Rs 85/each


'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items

items={'rice':20,
       'sugar':30,
       'salt':20,
       'oil':110,
       'panner':80,
       'Maggi':50,
       'boost':90,
       'colgate':85}
option=int(input("Forlist of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit"))
    if inp1==2:
        break 
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,item,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry this item is not available")
    else:
        print("You entered wrong number")
    inp=input("can i bill the items YES or NO")   
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Bhavya Supermarket",25*"=")
            print(25*" ","kadapa")
            print("Name:",name,30*" ","Date",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',2*' ',ilist[i],13*' ',qlist[i],10*" ",plist[i]) 
            print(75*"-")
            print(50*" ",'TotaAmount:','Rs',totalprice)
            print("gstamount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'FinalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")

