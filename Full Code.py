from tkinter import *
from tkinter import messagebox
import datetime
import random
import time
me=Tk()
me.geometry("1350x750")
me.title("Restaurant Management System")
me.configure(bg="#a0522d")

Top_frame=Frame(me,bg="#a0522d",bd=20,pady=5,relief=RIDGE)
Top_frame.pack(side=TOP)

lbl_title=Label(Top_frame,text="Restaurant Management System",bg="#a0522d",fg="#321414",justify=CENTER,font=("arial",60,"bold"),bd=20)
lbl_title.grid(row=0,column=0)

Rec_cal_frame=Frame(me,bg="#a0522d",bd=10,relief=RIDGE)
Rec_cal_frame.pack(side=RIGHT)

Bt=Frame(Rec_cal_frame,bg="#a0522d",bd=3,relief=RIDGE)
Bt.pack(side=BOTTOM)

Cal_f=Frame(Rec_cal_frame,bg="#a0522d",bd=6,relief=RIDGE)
Cal_f.pack(side=TOP)

Recipt_f=Frame(Rec_cal_frame,bg="#a0522d",bd=4,relief=RIDGE)
Recipt_f.pack(side=BOTTOM)

Menuframe=Frame(me,bg="#a0522d",bd=10,relief=RIDGE)
Menuframe.pack(side=LEFT)
Cost_f=Frame(Menuframe,bg="#a0522d",bd=4,relief=RIDGE)
Cost_f.pack(side=BOTTOM)

Drinks=Frame(Menuframe,bg="#a0522d",bd=10,relief=RIDGE)
Drinks.pack(side=LEFT)
Cake=Frame(Menuframe,bg="#a0522d",bd=10,relief=RIDGE)
Cake.pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()

DateOfOrder=StringVar()
Paidtax=StringVar()
ServiceCharge=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofDrinks=StringVar()
CostofCake=StringVar()
Receipt=StringVar()
################Calculator##################
text=StringVar()
operator=""
#################################
Strawberry_Cake2=StringVar()
PineappleCake2=StringVar()
DarkChocalateCake2=StringVar()
BlackForestCake2=StringVar()
RedVelvet_Cake2=StringVar()
Mango_Cake2=StringVar()
Rasmalai_Cake2=StringVar()

Tea2=StringVar()
Milkshake2=StringVar()
Orangejuice2=StringVar()
Coke2=StringVar()
Falooda2=StringVar()
Coffee2=StringVar()
Thumbshup2=StringVar()

Strawberry_Cake2.set("0")
PineappleCake2.set("0")
DarkChocalateCake2.set("0")
BlackForestCake2.set("0")
RedVelvet_Cake2.set("0")
Mango_Cake2.set("0")
Rasmalai_Cake2.set("0")

Tea2.set("0")
Milkshake2.set("0")
Orangejuice2.set("0")
Coke2.set("0")
Falooda2.set("0")
Coffee2.set("0")
Thumbshup2.set("0")

DateOfOrder.set(time.strftime("%d/%m/%Y"))
##############################
def exit():
    exit=messagebox.askyesno("Exit Restaurant System","Confirm if you want to Exit")
    if exit>0:
        me.destroy()

def reset():
    DateOfOrder.set("")
    Paidtax.set("")
    ServiceCharge.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCake.set("")
    text_recipt.delete("1.0",END)


    Strawberry_Cake2.set("0")
    PineappleCake2.set("0")
    DarkChocalateCake2.set("0")
    BlackForestCake2.set("0")
    RedVelvet_Cake2.set("0")
    Mango_Cake2.set("0")
    Rasmalai_Cake2.set("0")

    Tea2.set("0")
    Milkshake2.set("0")
    Orangejuice2.set("0")
    Coke2.set("0")
    Falooda2.set("0")
    Coffee2.set("0")
    Thumbshup2.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)

    Strawberry_Cake1.config(state=DISABLED)
    PineappleCake1.config(state=DISABLED)
    BlackForestCake1.config(state=DISABLED)
    DarkChocalate_Cake1.config(state=DISABLED)
    RedVelvet_Cake1.config(state=DISABLED)
    Mango_Cake1.config(state=DISABLED)
    Rasmalai_Cake1.config(state=DISABLED)
    Tea1.config(state=DISABLED)
    Milkshake1.config(state=DISABLED)
    Falooda1.config(state=DISABLED)
    Coffee1.config(state=DISABLED)
    Thumbshup1.config(state=DISABLED)
    Coke1.config(state=DISABLED)
    Orangejuice1.config(state=DISABLED)

def CostOfItem():
    Item1=  float(Strawberry_Cake1.get())
    Item2 = float(PineappleCake1.get())
    Item3 = float(BlackForestCake1.get())
    Item4 = float(DarkChocalate_Cake1.get())
    Item5 = float(RedVelvet_Cake1.get())
    Item6 = float(Mango_Cake1.get())
    Item7 = float(Rasmalai_Cake1.get())


    Item8 = float(Tea1.get())
    Item9 = float(Milkshake1.get())
    Item10 =float(Falooda1.get())
    Item11= float(Coffee1.get())
    Item12= float(Thumbshup1.get())
    Item13= float(Coke1.get())
    Item14 =float(Orangejuice1.get())

    Priceofcakes=(Item1*90)+ (Item2*120)+ (Item3*110)+ (Item4*80)+ (Item5*150)+ (Item6*100)+ (Item7*60)
    Priceofdrinks= (Item8*10)+ (Item9*40)+ (Item10*30)+ (Item11*10)+ (Item12*20)+ (Item13*20)+ (Item14*15)

    Drinksprice="₹",str('%.2f' %(Priceofdrinks))
    Cakeprice="₹",str('%.2f' %(Priceofcakes))

    CostofDrinks.set(Drinksprice)
    CostofCake.set(Cakeprice)

    SC="₹",str('%.2f' %(40))
    ServiceCharge.set(SC)

    SubTotalofitems="₹",str('%.2f' %(Priceofcakes+Priceofdrinks+40))
    SubTotal.set(SubTotalofitems)

    Tax="₹",str("%.2f" %((Priceofcakes+Priceofdrinks+40)*0.30))
    Paidtax.set(Tax)

    TT=((Priceofcakes+Priceofdrinks+40)*0.30)
    TC = "₹", str('%.2f' % (Priceofcakes+Priceofdrinks+40+TT))
    TotalCost.set(TC)
def chkStrawberryCake():
    if(var8.get()==1):
        Strawberry_Cake1.configure(state=NORMAL)
        Strawberry_Cake1.focus()
        Strawberry_Cake1.delete("0",END)
        Strawberry_Cake2.set("")
    elif(var8.get()==0):
        Strawberry_Cake1.configure(state=DISABLED)
        Strawberry_Cake2.set("0")
def chkPineappleCake():
    if (var9.get() == 1):
        PineappleCake1.configure(state=NORMAL)
        PineappleCake1.focus()
        PineappleCake1.delete("0", END)
        PineappleCake2.set("")
    elif (var9.get() == 0):
        PineappleCake1.configure(state=DISABLED)
        PineappleCake2.set("0")
def chkBlackForestCake():
    if (var10.get() == 1):
        BlackForestCake1.configure(state=NORMAL)
        BlackForestCake1.focus()
        BlackForestCake1.delete("0", END)
        BlackForestCake2.set("")
    elif (var10.get() == 0):
        BlackForestCake1.configure(state=DISABLED)
        BlackForestCake2.set("0")
def chkDarkChocalateCake():
    if (var11.get() == 1):
        DarkChocalate_Cake1.configure(state=NORMAL)
        DarkChocalate_Cake1.focus()
        DarkChocalate_Cake1.delete("0", END)
        DarkChocalateCake2.set("")
    elif (var11.get() == 0):
        DarkChocalate_Cake1.configure(state=DISABLED)
        DarkChocalateCake2.set("0")
def chkRedVelvetCake():
    if (var12.get() == 1):
        RedVelvet_Cake1.configure(state=NORMAL)
        RedVelvet_Cake1.focus()
        RedVelvet_Cake1.delete("0", END)
        RedVelvet_Cake2.set("")
    elif (var12.get() == 0):
        RedVelvet_Cake1.configure(state=DISABLED)
        RedVelvet_Cake2.set("0")
def chkMangoCake():
    if (var13.get() == 1):
        Mango_Cake1.configure(state=NORMAL)
        Mango_Cake1.focus()
        Mango_Cake1.delete("0", END)
        Mango_Cake2.set("")
    elif (var13.get() == 0):
        Mango_Cake1.configure(state=DISABLED)
        Mango_Cake2.set("0")
def chkRasmalaiCake():
    if (var14.get() == 1):
        Rasmalai_Cake1.configure(state=NORMAL)
        Rasmalai_Cake1.focus()
        Rasmalai_Cake1.delete("0", END)
        Rasmalai_Cake2.set("")
    elif (var14.get() == 0):
        Rasmalai_Cake1.configure(state=DISABLED)
        Rasmalai_Cake2.set("0")
def chkTea():
    if (var1.get() == 1):
        Tea1.configure(state=NORMAL)
        Tea1.focus()
        Tea1.delete("0", END)
        Tea2.set("")
    elif (var1.get() == 0):
        Tea1.configure(state=DISABLED)
        Tea2.set("0")
def chkMilkshake():
    if (var2.get() == 1):
        Milkshake1.configure(state=NORMAL)
        Milkshake1.focus()
        Milkshake1.delete("0", END)
        Milkshake2.set("")
    elif (var2.get() == 0):
        Milkshake1.configure(state=DISABLED)
        Milkshake2.set("0")
def chkFalooda():
    if (var3.get() == 1):
        Falooda1.configure(state=NORMAL)
        Falooda1.focus()
        Falooda1.delete("0", END)
        Falooda2.set("")
    elif (var3.get() == 0):
        Falooda1.configure(state=DISABLED)
        Falooda2.set("0")
def chkCoffeee():
    if (var4.get() == 1):
        Coffee1.configure(state=NORMAL)
        Coffee1.focus()
        Coffee1.delete("0", END)
        Coffee2.set("")
    elif (var4.get() == 0):
        Coffee1.configure(state=DISABLED)
        Coffee2.set("0")
def chkthumbshup():
    if (var5.get() == 1):
        Thumbshup1.configure(state=NORMAL)
        Thumbshup1.focus()
        Thumbshup1.delete("0", END)
        Thumbshup2.set("")
    elif (var5.get() == 0):
        Thumbshup1.configure(state=DISABLED)
        Thumbshup2.set("0")
def chkcoke():
    if (var6.get() == 1):
        Coke1.configure(state=NORMAL)
        Coke1.focus()
        Coke1.delete("0", END)
        Coke2.set("")
    elif (var6.get() == 0):
        Coke1.configure(state=DISABLED)
        Coke2.set("0")
def chkorangejuce():
    if (var7.get() == 1):
        Orangejuice1.configure(state=NORMAL)
        Orangejuice1.focus()
        Orangejuice1.delete("0", END)
        Orangejuice2.set("")
    elif (var7.get() == 0):
        Orangejuice1.configure(state=DISABLED)
        Orangejuice2.set("0")

def Recept():
    text_recipt.delete("1.0",END)
    x=random.randint(10000,700000)
    random1=str(x)
    Receipt.set("BILL"+ random1)
    text_recipt.insert(END, 'Receipt:\t\t\t'+ Receipt.get()+  "\t" + DateOfOrder.get()+"\n")
    text_recipt.insert(END, 'Item:\t\t\t' + "CostOfItems\n")
    text_recipt.insert(END, 'Tea:\t\t\t' +  Tea2.get()+"\n")
    text_recipt.insert(END, 'Milkshake:\t\t\t' + Milkshake2.get() + "\n")
    text_recipt.insert(END, 'Falooda:\t\t\t' + Falooda2.get() + "\n")
    text_recipt.insert(END, 'Coffee:\t\t\t' + Coffee2.get() + "\n")
    text_recipt.insert(END, 'Thumbshup:\t\t\t' + Thumbshup2.get() + "\n")
    text_recipt.insert(END, 'Coke:\t\t\t' + Coke2.get() + "\n")
    text_recipt.insert(END, 'Orangejuice:\t\t\t' + Orangejuice2.get() + "\n")
    text_recipt.insert(END, 'StrawberryCake:\t\t\t' + Strawberry_Cake2.get() + "\n")
    text_recipt.insert(END, 'PineappleCake:\t\t\t' + PineappleCake2.get() + "\n")
    text_recipt.insert(END, 'BlackForestCake:\t\t\t' + BlackForestCake2.get() + "\n")
    text_recipt.insert(END, 'DarkChocalateCake:\t\t\t' + DarkChocalateCake2.get() + "\n")
    text_recipt.insert(END, 'RedVelvet_Cake1:\t\t\t' + RedVelvet_Cake2.get() + "\n")
    text_recipt.insert(END, 'MangoCake:\t\t\t' + Mango_Cake2.get() + "\n")
    text_recipt.insert(END, 'RasmalaiCake:\t\t\t' +Rasmalai_Cake2.get() + "\n")
    text_recipt.insert(END, 'Cost Of Drinks:\t\t\t' +CostofDrinks.get() + "\n")
    text_recipt.insert(END, 'Cost Of Cakes:' +CostofCake.get() + "\t" 'Sub Total:' + SubTotal.get() + "\n")
    text_recipt.insert(END, 'Total Cost:\t\t\t' + TotalCost.get() + "\t")
    text_recipt.insert(END, 'Service Charge:\t\t\t' +ServiceCharge.get() + "\n")
    text_recipt.insert(END, 'Tax Paid:\t\t\t' + Paidtax.get() + "\n")

#text_recipt.insert(END, 'Sub Total:\t\t\t' + SubTotal.get() + "\n")
##########################################################################################################################################
Strawberry_Cake=Checkbutton(Cake,text="Strawberry Cake",variable=var8,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkStrawberryCake)
Strawberry_Cake.grid(row=0,sticky=W)
PineappleCake=Checkbutton(Cake,text="Pineapple Cake",variable=var9,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkPineappleCake)
PineappleCake.grid(row=1,sticky=W)
BlackForestCake=Checkbutton(Cake,text="BlackForest Cake",variable=var10,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkBlackForestCake)
BlackForestCake.grid(row=2,sticky=W)
DarkChocalate_Cake=Checkbutton(Cake,text="DarkChocalate Cake",variable=var11,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkDarkChocalateCake)
DarkChocalate_Cake.grid(row=3,sticky=W)
RedVelvet_Cake=Checkbutton(Cake,text="RedVelvet Cake",variable=var12,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkRedVelvetCake)
RedVelvet_Cake.grid(row=4,sticky=W)
Mango_Cake=Checkbutton(Cake,text="Mango Cake",variable=var13,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkMangoCake)
Mango_Cake.grid(row=5,sticky=W)
Rasmalai_Cake=Checkbutton(Cake,text="Rasmalai Cake",variable=var14,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkRasmalaiCake)
Rasmalai_Cake.grid(row=6,sticky=W)

Strawberry_Cake1=Entry(Cake,font=("arial",16,"bold"),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=Strawberry_Cake2)
Strawberry_Cake1.grid(row=0,column=1)
PineappleCake1=Entry(Cake,font=("arial",16,"bold"),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=PineappleCake2)
PineappleCake1.grid(row=1,column=1)
BlackForestCake1=Entry(Cake,font=("arial",16,"bold"),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=BlackForestCake2)
BlackForestCake1.grid(row=2,column=1)
DarkChocalate_Cake1=Entry(Cake,font=("arial",16,"bold"),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=DarkChocalateCake2)
DarkChocalate_Cake1.grid(row=3,column=1)
RedVelvet_Cake1=Entry(Cake,font=("arial",16,"bold"),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=RedVelvet_Cake2)
RedVelvet_Cake1.grid(row=4,column=1)
Mango_Cake1=Entry(Cake,font=("arial",16,"bold"),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=Mango_Cake2)
Mango_Cake1.grid(row=5,column=1)
Rasmalai_Cake1=Entry(Cake,font=("arial",16,"bold"),bd=3,width=6,justify=LEFT,state=DISABLED,textvariable=Rasmalai_Cake2)
Rasmalai_Cake1.grid(row=6,column=1)

Tea=Checkbutton(Drinks,text="Tea",variable=var1,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkTea)
Tea.grid(row=0,sticky=W)
Milkshake=Checkbutton(Drinks,text="Milk Shake",variable=var2,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkMilkshake)
Milkshake.grid(row=1,sticky=W)
Falooda=Checkbutton(Drinks,text="Falooda",variable=var3,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkFalooda)
Falooda.grid(row=2,sticky=W)
Coffee=Checkbutton(Drinks,text="Coffee",variable=var4,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkCoffeee)
Coffee.grid(row=3,sticky=W)
Thumbshup=Checkbutton(Drinks,text="Thumbshup",variable=var5,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkthumbshup)
Thumbshup.grid(row=4,sticky=W)
Coke=Checkbutton(Drinks,text="Coke",variable=var6,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkcoke)
Coke.grid(row=5,sticky=W)
Orangejuice=Checkbutton(Drinks,text="Orangejuice",variable=var7,onvalue=1,offvalue=0,font=("arial",18,"bold"),bg='#a0522d',fg="#f4a460",command=chkorangejuce)
Orangejuice.grid(row=6,sticky=W)

Tea1=Entry(Drinks,font=("arial",16,"bold"),bd=3,width=6,state=DISABLED,justify=LEFT,textvariable=Tea2)
Tea1.grid(row=0,column=1)
Milkshake1=Entry(Drinks,font=("arial",16,"bold"),bd=3,width=6,state=DISABLED,justify=LEFT,textvariable=Milkshake2)
Milkshake1.grid(row=1,column=1)
Falooda1=Entry(Drinks,font=("arial",16,"bold"),bd=3,width=6,state=DISABLED,justify=LEFT,textvariable=Falooda2)
Falooda1.grid(row=2,column=1)
Coffee1=Entry(Drinks,font=("arial",16,"bold"),bd=3,width=6,state=DISABLED,justify=LEFT,textvariable=Coffee2)
Coffee1.grid(row=3,column=1)
Thumbshup1=Entry(Drinks,font=("arial",16,"bold"),bd=3,width=6,state=DISABLED,justify=LEFT,textvariable=Thumbshup2)
Thumbshup1.grid(row=4,column=1)
Coke1=Entry(Drinks,font=("arial",16,"bold"),bd=3,width=6,state=DISABLED,justify=LEFT,textvariable=Coke2)
Coke1.grid(row=5,column=1)
Orangejuice1=Entry(Drinks,font=("arial",16,"bold"),bd=3,width=6,state=DISABLED,justify=LEFT,textvariable=Orangejuice2)
Orangejuice1.grid(row=6,column=1)
#############Total cost##########################
lbl_costdrinks=Label(Cost_f,text="Cost Of Drinks   \t",bg='#a0522d',fg="#f4a460",font=("arial",14,"bold"))
lbl_costdrinks.grid(row=0,column=0,sticky=W)

text_costdrinks=Entry(Cost_f,insertwidth=2,bg="White",bd=7,font=("arial",14,"bold"),justify=RIGHT,textvariable=CostofDrinks)
text_costdrinks.grid(row=0,column=1)

lbl_costcake=Label(Cost_f,text="Cost Of Cake  \t",bg='#a0522d',fg="#f4a460",font=("arial",14,"bold"))
lbl_costcake.grid(row=1,column=0,sticky=W)

text_costcake=Entry(Cost_f,insertwidth=2,bg="White",bd=7,font=("arial",14,"bold"),justify=RIGHT,textvariable=CostofCake)
text_costcake.grid(row=1,column=1)

lbl_sc=Label(Cost_f,text="Service Charge  \t",bg='#a0522d',fg="#f4a460",font=("arial",14,"bold"))
lbl_sc.grid(row=2,column=0,sticky=W)

text_sc=Entry(Cost_f,insertwidth=2,bg="White",bd=7,font=("arial",14,"bold"),justify=RIGHT,textvariable=ServiceCharge)
text_sc.grid(row=2,column=1)
##############Payment##################

lbl_pt=Label(Cost_f,text="Paid tax \t",bg='#a0522d',fg="#f4a460",font=("arial",14,"bold"))
lbl_pt.grid(row=0,column=2,sticky=W)

text_pt=Entry(Cost_f,insertwidth=2,bg="White",bd=7,font=("arial",14,"bold"),justify=RIGHT,textvariable=Paidtax)
text_pt.grid(row=0,column=3)

lbl_st=Label(Cost_f,text="Sub Total  \t",bg='#a0522d',fg="#f4a460",font=("arial",14,"bold"))
lbl_st.grid(row=1,column=2,sticky=W)

text_st=Entry(Cost_f,insertwidth=2,bg="White",bd=7,font=("arial",14,"bold"),justify=RIGHT,textvariable=SubTotal)
text_st.grid(row=1,column=3)

lbl_tc=Label(Cost_f,text="Total Cost \t",bg='#a0522d',fg="#f4a460",font=("arial",14,"bold"))
lbl_tc.grid(row=2,column=2,sticky=W)

text_tc=Entry(Cost_f,insertwidth=2,bg="White",bd=7,font=("arial",14,"bold"),justify=RIGHT,textvariable=TotalCost)
text_tc.grid(row=2,column=3)
#############Reecipt##############
text_recipt=Text(Recipt_f,width=46,height=12,bg="White",bd=4,font=("arial",16,"bold"))
text_recipt.grid(row=0,column=0)
#buttons
total=Button(Bt,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="Total",bg='#a0522d',fg="#f4a460",bd=7,command=CostOfItem)
total.grid(row=0,column=0)

Rceipt=Button(Bt,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="Rceipt",bg='#a0522d',fg="#f4a460",bd=7,command=Recept)
Rceipt.grid(row=0,column=1)

Reset=Button(Bt,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="Reset",bg='#a0522d',fg="#f4a460",bd=7,command=reset)
Reset.grid(row=0,column=2)

Exit=Button(Bt,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="Exit",bg='#a0522d',fg="#f4a460",bd=7,command=exit)
Exit.grid(row=0,column=3)
#======================================================Caluclator===========================#
#Caluclator buttons
def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text.set(operator)
def btnClear():
    global operator
    operator=""
    text.set("")
def btnequals():
    global operator
    result=str(eval(operator))
    text.set(result)
    operator = ""


text_display=Entry(Cal_f,width=45,bg="White",bd=4,font=("arial",16,"bold"),justify=RIGHT,textvariable=text)
text_display.grid(row=0,column=0,columnspan=4, pady=1)
text_display.insert(0,"0")

btn7=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="7",bg='#a0522d',fg="#f4a460",bd=7,command=lambda:btnClick(7))
btn7.grid(row=1,column=0)

btn8=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="8",bg='#a0522d',fg="#f4a460",bd=7,command=lambda:btnClick(8))
btn8.grid(row=1,column=1)

btn9=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="9",bg='#a0522d',fg="#f4a460",bd=7,command=lambda:btnClick(9))
btn9.grid(row=1,column=2)

add=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="+",bg='#a0522d',fg="#f4a460",bd=7,command=lambda:btnClick("+"))
add.grid(row=1,column=3)
#########
btn4=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="4",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick(4))
btn4.grid(row=2,column=0)

btn5=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="5",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick(5))
btn5.grid(row=2,column=1)

btn6=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="6",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick(6))
btn6.grid(row=2,column=2)

sub=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="-",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick("-"))
sub.grid(row=2,column=3)
#######
btn1=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="1",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick(1))
btn1.grid(row=3,column=0)

btn2=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="2",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick(2))
btn2.grid(row=3,column=1)

btn3=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="3",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick(3))
btn3.grid(row=3,column=2)

mul=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="x",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick("*"))
mul.grid(row=3,column=3)
#######
btn0=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="0",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick(0))
btn0.grid(row=4,column=0)

btnclear=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="C",bg='#a0522d',fg="#f4a460",bd=7,command=btnClear)
btnclear.grid(row=4,column=1)

btnequal=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="=",bg='#a0522d',fg="#f4a460",bd=7,command=btnequals)
btnequal.grid(row=4,column=2)

div=Button(Cal_f,padx=16,pady=1,font=("arial",16,"bold"),width=4,text="/",bg='#a0522d',fg="#f4a460",bd=7,command=lambda :btnClick("/"))
div.grid(row=4,column=3)
me.mainloop()

