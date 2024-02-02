from tkinter import *
import tkinter as tk
from modules.randomizer import rdm_pass
from modules.elimtr1 import *
from modules.elimtr2 import *
from modules.file import *
import pyperclip

window = Tk()
window.title("CipherKeep")
window.minsize(400, 525)
window.maxsize(400,525)
window.configure(background="MediumPurple4")

header = Label(window, text="CIPHERKEEP", font=('BankGothic Lt BT', 32, 'bold'), background="MediumPurple4",foreground="white")
header.pack()

canvas = Canvas(window, height=250, width=250, background="MediumPurple4", highlightthickness=0)
logo_img = PhotoImage(file='logo2.png')
resized_image = logo_img.subsample(1)
canvas.create_image(125, 125, image=resized_image)
canvas.pack()

blank_space_for_canvas = Label(window, text="", font=('Calibri', 2, 'bold'), background="MediumPurple4",foreground="MediumPurple4")
blank_space_for_canvas.pack()

def blank_space():
    blank_space = Label(window, text="", font=('Calibri', 4, 'bold'), background="MediumPurple4",foreground="MediumPurple4")
    blank_space.pack()

def unfilled_org_or_login():
    if org_input.get() == '':
        exception_frame.pack()
        unfilled_label1.pack()
    if login_input.get() == '':
        exception_frame.pack()
        unfilled_label2.pack()



def unfilled_org_login_pass():
    if org_input.get() == '':
        exception_frame.pack()
        unfilled_label1.pack()
    if login_input.get() == '':
        exception_frame.pack()
        unfilled_label2.pack()
    if pass_input.get() == '':
        exception_frame.pack()
        unfilled_label3.pack()

# Exception remover
def forget_exception_labels():
    try: unfilled_label2.pack_forget()
    except: pass
    try: unfilled_label1.pack_forget()
    except:pass
    try:unfilled_label3.pack_forget()
    except:pass
    try:inc_pass_label5.pack_forget()
    except:pass
    try:inc_pass_label6.pack_forget()
    except:pass
    try:inc_pass_label7.pack_forget()
    except:pass
    try:inc_pass_label8.pack_forget()
    except:pass
    try:inc_pass_label9.pack_forget()
    except:pass
    try:inc_pass_label10.pack_forget()
    except:pass
    try:inc_pass_label11.pack_forget()
    except:pass
    try:inc_pass_label12.pack_forget()
    except:pass
    try:non_retr_label13.pack_forget()
    except:pass
    try:inc_pass_label4.pack_forget()
    except:pass
    try:exception_frame.pack_forget()
    except:pass
    try: retr_label.pack_forget()
    except:pass
    try: save_label.pack_forget()
    except:pass


# Function to display what went wrong in case of incorrect input (must run rain_check before this)
def error():
    exception_frame.pack()
    if not cdict['a']: inc_pass_label4.pack()  # ('Password must contain at least one uppercase alphabet')
    if not cdict['b']: inc_pass_label5.pack()  # ('Password must contain at least one lowercase alphabet')
    if not cdict['c']: inc_pass_label6.pack()  # ('Password must contain at least one number')
    if not cdict['d']: inc_pass_label7.pack()  # ('Password must contain at least one special character')
    if not cdict['e']: inc_pass_label8.pack()  # ('Length of password must be 8 to 32')
    if not cdict['f']: inc_pass_label9.pack()  # ('Password must not contain spaces')
    if not cdict['g']: inc_pass_label10.pack()  # ('Password must not match with login_id')
    if not cdict['h']: inc_pass_label11.pack()  # ('Password must not match with organisation name')
    if not cdict['i']: inc_pass_label12.pack()  # ('Password must not be a commonly used password')

def passw(org,login_id):
    while True:
        password = rdm_pass()
        if conditions(org,login_id,password):
            break
        else:
            continue
    return password

# Function to check for conditions a,b,c,d,e,f,g,h,i
def conditions(org, login_id, password):
    rain_check(org, login_id, password)
    if cdict['a'] and cdict['b'] and cdict['c'] and cdict['d'] and cdict['e'] \
            and cdict['f'] and cdict['g'] and cdict['h'] and cdict['i']:
        return True
    else:
        return False

# Function that creates a boolean dict with all conditions
def rain_check(org,login_id, password):
    global a, b, c, d, e, f, cdict
    cdict = {}
    a = check_letters(password, 'upr_alpts')
    b = check_letters(password, 'lwr_alpts')
    c = check_letters(password, 'digits')
    d = check_letters(password, 'sp_char')
    e = check_range(password)
    f = check_space(password)
    g = check_userid(login_id, password)
    h = check_org(org, password)
    i = check_dlist(password)
    cdict = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i}

def clipboard(text):
    pyperclip.copy(text)

def save(org,login_id,password):
    list_of_dicts = capture_file()
    # If Org is not found in existing data, add data in new row
    if lookup(org,login_id,list_of_dicts):
        new_data = existing_row(org,login_id,password,list_of_dicts)
    else:
        new_data = new_row(org,login_id,password,list_of_dicts)
    write_ptable(new_data)

def retrieve(org, login_id):
    list_of_dicts = capture_file()
    if lookup(org, login_id,list_of_dicts):
        password = list_of_dicts[lookup(org,login_id,list_of_dicts)]['passw']
        return password
    else:
        return False

login_label = Label(text="Enter your Login ID", font=('Calibri', 12, 'bold'), background="MediumPurple4",foreground="white")
login_input = Entry(width=30, justify="center")
org_label = Label(text="Enter Organisation Name", font=('Calibri', 12, 'bold'), background="MediumPurple4",foreground="white")
org_input = Entry(width=30, justify="center")
pass_label = Label(text="Enter Password", font=('Calibri', 12, 'bold'), background="MediumPurple4", foreground="white")
pass_input = Entry(width=30, justify="center")
button_frame = Frame(background="MediumPurple4")

# Resulting Labels and frame
exception_frame = Frame(background="MediumPurple4")
unfilled_label1 = Label(exception_frame, text="Organisation name is not filled", font=('Calibri', 12),background="MediumPurple4", foreground="white")
unfilled_label2 = Label(exception_frame, text="Login ID is not filled", font=('Calibri', 12),background="MediumPurple4", foreground="white")
unfilled_label3 = Label(exception_frame, text="Password is not filled", font=('Calibri', 12),background="MediumPurple4", foreground="white")
inc_pass_label4 = Label(exception_frame, text="Password must contain at least one uppercase alphabet",font=('Calibri', 12), background="MediumPurple4", foreground="white")
inc_pass_label5 = Label(exception_frame, text="Password must contain at least one lowercase alphabet",font=('Calibri', 12), background="MediumPurple4", foreground="white")
inc_pass_label6 = Label(exception_frame, text="Password must contain at least one number", font=('Calibri', 12),background="MediumPurple4", foreground="white")
inc_pass_label7 = Label(exception_frame, text="Password must contain at least one special character",font=('Calibri', 12), background="MediumPurple4", foreground="white")
inc_pass_label8 = Label(exception_frame, text="Length of password must be 8 to 32", font=('Calibri', 12),background="MediumPurple4", foreground="white")
inc_pass_label9 = Label(exception_frame, text="Password must not contain spaces", font=('Calibri', 12),background="MediumPurple4", foreground="white")
inc_pass_label10 = Label(exception_frame, text="Password must not match with login_id", font=('Calibri', 12),background="MediumPurple4", foreground="white")
inc_pass_label11 = Label(exception_frame, text="Password must not match with organisation name", font=('Calibri', 12),background="MediumPurple4", foreground="white")
inc_pass_label12 = Label(exception_frame, text="Password must not be a commonly used password", font=('Calibri', 12),background="MediumPurple4", foreground="white")
non_retr_label13 = Label(exception_frame,text="Password not found", font=('Calibri', 12),background="MediumPurple4",foreground="white")
save_label = Label()
retr_label = Label()


# Home Page
def create_pass_button():
    button1.destroy()
    button2.destroy()
    org_label.pack()
    org_input.pack()
    blank_space()
    login_label.pack()
    login_input.pack()
    blank_space()
    pass_label.pack()
    pass_input.pack()
    blank_space()
    button_frame.pack()

    def generate_button():
        forget_exception_labels()
        unfilled_org_or_login()
        org = org_input.get()
        login = login_input.get()
        if org != '' and login != '':
            forget_exception_labels()
            password = passw(org, login)
            pass_input.delete(0, tk.END)
            pass_input.insert(0, password)
            clipboard(password)


    button3 = Button(button_frame, text="Generate", font=('BankGothic Lt BT', 11, 'bold'), background="MediumPurple4",foreground="white", command=generate_button)
    button3.pack(side=tk.LEFT,padx=5)

    def save_button():
        forget_exception_labels()
        unfilled_org_login_pass()
        org = org_input.get()
        login = login_input.get()
        password = pass_input.get()
        if org != '' and login != '' and password != '':
            forget_exception_labels()
            if conditions(org,login,password):
                save(org_input.get(), login_input.get(), pass_input.get())
                global save_label
                save_label = Label(text=f"Your Password is saved", font=('Calibri', 12), background="MediumPurple4",
                                   foreground="white")
                save_label.pack()
            else:
                error()

    button4 = Button(button_frame, text="Save", font=('BankGothic Lt BT', 11, 'bold'), background="MediumPurple4",foreground="white", command=save_button)
    button4.pack(side=tk.RIGHT)

# Home page
def retrieve_pass_button():
    button1.destroy()
    button2.destroy()
    org_label.pack()
    org_input.pack()
    blank_space()
    login_label.pack()
    login_input.pack()
    blank_space()

    def retrieve_button():
        forget_exception_labels()
        unfilled_org_or_login()
        org = org_input.get()
        login = login_input.get()
        retrieved = retrieve(org,login)
        if org != '' and login != '':
            forget_exception_labels()
            if retrieved == False:
                exception_frame.pack()
                non_retr_label13.pack()
            else:
                global retr_label
                clipboard(retrieved)
                retr_label = Label(text=f"Your existing Password is copied to clipboard",font=('Calibri', 12),background="MediumPurple4", foreground="white")
                retr_label.pack()

    button5 = Button(text="Retrive", font=('BankGothic Lt BT', 12, 'bold'), background="MediumPurple4",foreground="white",command=retrieve_button)
    button5.pack()

button1 = Button(window, text="Create Password", font=('BankGothic Lt BT', 15, 'bold'), background="MediumPurple4",foreground="white", command=create_pass_button)
button1.place(x=86, y=350)

button2 = Button(window, text="Retrieve Password", font=('BankGothic Lt BT', 15, 'bold'), background="MediumPurple4",foreground="white", command=retrieve_pass_button)
button2.place(x=79, y=425)

window.mainloop()
