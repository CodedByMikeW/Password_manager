from tkinter import *
from tkinter import messagebox
import random 


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
Letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers=['0','1','2','3','4','5','6','7','8','9']
Symbols=['!','#','$','%','&']

def generate_pass():
    passw = []
    gen_pass=''



    for letter in range(2):
        random_Let_list = random.choice(Letters)
        random_Num_list=random.choice(Numbers)
        random_Sym_list= random.choice(Symbols)
        passw += random_Let_list
        passw += random_Let_list
        passw += random_Num_list
        passw += random_Sym_list
        random.shuffle(passw)
        gen_pass="".join(passw)
    password_entry.delete(0,END)
    password_entry.insert(0,gen_pass)
    print(gen_pass)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password)==0:
        messagebox.showinfo(title="OOps",message =" Pleae make sure you haven't left any fields empty.")
    else:
        is_ok=messagebox.askokcancel(title="Title",
                                     message=f" These are the details enter: "
                                             f"\nEmail:{email} \nPassword:{password} "
                                             f"\n IS it ok to save?")
    if is_ok:
        with open("password_man.txt","a") as password_file:
            password_file.write(f"{website} |{email} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    # ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title('Password Manager')
window.config(padx=100,pady=100)

canvas = Canvas(height=250,width=200)
logo_img = PhotoImage(file="logoo.png")
canvas.create_image(100,80,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)
password_label = Label(text="Password")
password_label.grid(row=3,column=0)

website_entry =Entry(width=35)
website_entry.grid(row=1,column=1)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1)
email_entry.insert(0,"Mikeal@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password_button=Button(text="Generate Password" ,command=generate_pass)
generate_password_button.grid(row=3,column=2)
add_button= Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=0,columnspan=2)
window.mainloop()
