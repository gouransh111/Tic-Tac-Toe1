from tkinter import*
from tkinter import messagebox
i = 0
j=0
#FUNTIONS===========================================================
def restart():
    global i,j
    i = 0
    l1_btn.config(bg="white")
    l2_btn.config(bg="white")
    l3_btn.config(bg="white")
    l4_btn.config(bg="white")
    l5_btn.config(bg="white")
    l6_btn.config(bg="white")
    l7_btn.config(bg="white")
    l8_btn.config(bg="white")
    l9_btn.config(bg="white")
    j = 0
    pl1_l.config(bg="red")
    pl2_l.config(bg="white")
def colour(pl,event):
    global i,j
   
    
    if pl["bg"] == "red":
        if event["bg"] =="white":
            i += 1
            event.configure(bg="blue")
            #event.config(text="o",font="lucida 12 bold")
            pl.config(bg="white")
            pl1_l.config(bg="red")
    else:
        if event["bg"] =="white":
            i += 1
            event.config(bg="red") 
            #event.config(text="x",font="lucida 12 bold",justify="center")
            pl.config(bg="red")
            pl1_l.config(bg="white")   
    #print(l1_btn["bg"])
    if l1_btn["bg"] == "red" and l2_btn["bg"] == "red" and l3_btn["bg"] == "red":
            rr = messagebox.showinfo("Won","Player1 won the game")
            #print(2)
            j = 1
    elif l4_btn["bg"] == "red" and l5_btn["bg"] == "red" and l6_btn["bg"] == "red":     
        rr = messagebox.showinfo("Won","Player1 won the game") 
        j = 1 
    elif l7_btn["bg"] == "red" and l8_btn["bg"] == "red" and l9_btn["bg"] == "red":     
        rr = messagebox.showinfo("Won","Player1 won the game") 
        j = 1  
    elif l1_btn["bg"] == "red" and l4_btn["bg"] == "red" and l7_btn["bg"] == "red":     
        rr = messagebox.showinfo("Won","Player1 won the game")   
        j = 1
    elif l2_btn["bg"] == "red" and l5_btn["bg"] == "red" and l8_btn["bg"] == "red":     
        rr = messagebox.showinfo("Won","Player1 won the game")   
        j = 1
    elif l3_btn["bg"] == "red" and l6_btn["bg"] == "red" and l9_btn["bg"] == "red":     
        rr = messagebox.showinfo("Won","Player1 won the game")  
        j = 1
    elif l1_btn["bg"] == "red" and l5_btn["bg"] == "red" and l9_btn["bg"] == "red":     
        rr = messagebox.showinfo("Won","Player1 won the game")   
        j = 1
    elif l3_btn["bg"] == "red" and l5_btn["bg"] == "red" and l7_btn["bg"] == "red":     
        rr = messagebox.showinfo("Won","Player1 won the game")
        j = 1 


    if l1_btn["bg"] == "blue" and l2_btn["bg"] == "blue" and l3_btn["bg"] == "blue":
            rr = messagebox.showinfo("Won","Player2 won the game")
            #print(2)
            j = 1
    elif l4_btn["bg"] == "blue" and l5_btn["bg"] == "blue" and l6_btn["bg"] == "blue":     
        rr = messagebox.showinfo("Won","Player2 won the game")
        j = 1   
    elif l7_btn["bg"] == "blue" and l8_btn["bg"] == "blue" and l9_btn["bg"] == "blue":     
        rr = messagebox.showinfo("Won","Player2 won the game") 
        j = 1  
    elif l1_btn["bg"] == "blue" and l4_btn["bg"] == "blue" and l7_btn["bg"] == "blue":     
        rr = messagebox.showinfo("Won","Player2 won the game")
        j = 1   
    elif l2_btn["bg"] == "blue" and l5_btn["bg"] == "blue" and l8_btn["bg"] == "blue":     
        rr = messagebox.showinfo("Won","Player2 won the game")  
        j = 1 
    elif l3_btn["bg"] == "blue" and l6_btn["bg"] == "blue" and l9_btn["bg"] == "blue":     
        rr = messagebox.showinfo("Won","Player2 won the game")  
        j = 1
    elif l1_btn["bg"] == "blue" and l5_btn["bg"] == "blue" and l9_btn["bg"] == "blue":     
        rr = messagebox.showinfo("Won","Player2 won the game")
        j = 1  
    elif l3_btn["bg"] == "blue" and l5_btn["bg"] == "blue" and l7_btn["bg"] == "blue":     
        rr = messagebox.showinfo("Won","Player2 won the game") 
        j = 1

    if i == 9 and j==0:
        rr = messagebox.showinfo("Tie","Match Tie")                                    


root = Tk()
root.title("Tic Tac Toe")
root.geometry("690x530+300+70")
root.config(bg="orange")
#Labels======================================
head_l = Label(root,text="Tic Tac Toe",bg="lawn green",fg="blue",font="lucida 20 bold",height=1)
head_l.pack(fill=X)


pl1_l=Label(root,text="Player1",fg="blue",bg="red",font="arial 20 bold",bd=7,relief=GROOVE)
pl1_l.place(x=20,y="450")

pl2_l=Label(root,text="Player2",fg="blue",bg="white",font="arial 20 bold",bd=7,relief=GROOVE)
pl2_l.place(x=550,y="450")

#Buttons===================================================
l1_btn = Button(root,width="30",height=7,border="5",relief=SUNKEN,bg="white",command=lambda:colour(pl2_l,l1_btn))
l1_btn.place(y=40) 

l2_btn = Button(root,width="30",height=7,border="5",relief=SUNKEN,bg="white",command=lambda:colour(pl2_l,l2_btn))
l2_btn.place(x="230",y=40) 

l3_btn = Button(root,width="30",height=7,border="5",relief=SUNKEN,bg="white",command=lambda:colour(pl2_l,l3_btn))
l3_btn.place(x="460",y=40) 

l4_btn = Button(root,width="30",height=7,border="5",relief=SUNKEN,bg="white",command=lambda:colour(pl2_l,l4_btn))
l4_btn.place(y=165) 

l5_btn = Button(root,width="30",height=7,border="5",relief=SUNKEN,bg="white",command=lambda:colour(pl2_l,l5_btn))
l5_btn.place(x="230",y=165) 

l6_btn = Button(root,width="30",height=7,border="5",relief=SUNKEN,bg="white",command=lambda:colour(pl2_l,l6_btn))
l6_btn.place(x="460",y=165) 

l7_btn = Button(root,width="30",height=7,border="5",relief=SUNKEN,bg="white",command=lambda:colour(pl2_l,l7_btn))
l7_btn.place(y=290) 

l8_btn = Button(root,width="30",height=7,border="5",relief=SUNKEN,bg="white",command=lambda:colour(pl2_l,l8_btn))
l8_btn.place(x="230",y=290) 

l9_btn = Button(root,width="30",height=7,border="5",relief=SUNKEN,bg="white",command=lambda:colour(pl2_l,l9_btn))
l9_btn.place(x="460",y=290) 

res_btn=Button(root,text="Restart",fg="red",bg="yellow",font="arial 20 bold",bd=7,relief=SUNKEN,command=restart)
res_btn.place(x="300",y="450",height=50)

root.mainloop()