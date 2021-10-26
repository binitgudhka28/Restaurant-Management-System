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


