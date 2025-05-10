import json
from tkinter import messagebox
from customtkinter import *
from random import choices, shuffle
import pandas as pd


alphabel = ['a','b','c','d','e','f','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ["0","1", "2", "3", "4", "5", "6", "7", "8","9"]
symbol=["#","@","&","%","=","^"]

#style :

LABEL_FONT = ("sans-serif",15,"bold")
BUTTON_FONT = ("serif",12,"bold")
ENTRY_FONT = ("sans-serif",13)
PLACE_FONT = ("sans-serif",15,"bold")
CONORS_ENTRY = 20
BORDER_W =1
BORDER_C = "#A31D1D"
TEXT_C = "#F1EFEC"


#add your information here :
EMAILS = ["------------------------------",
	
          ]

PHONES=["------------------------------",

		]

#define funtions :

def save():
	file_path= "./password_saver.json"

	website = website_entry.get().lower()

	password = password_entry.get()
	email = email_entry.get()
	phone = phone_entry.get()
	user = username_entry.get()
	if len(phone)==0 :
		phone = "None"
	if len(user)==0:
		user = "None"
	data_t = {
		website: {
			"email": email,
			"password": password,
			"phone":phone,
			"user":user,
			}

		}
	if len(email) ==0 or len(password) ==0 or len(website)==0 :
		messagebox.showinfo(title="Errors",message="fill all please...")
	else:
		try :
			with open(file_path, "r") as file:
				data = json.load(file)
		except:
			with open(file_path, "w") as json_file:
				json.dump(data_t, json_file,indent=4)
		else:
			data.update(data_t)
			with open(file_path, "w") as json_file:
				json.dump(data, json_file,indent=4)
		finally:
			website_entry.delete(0, END)
			password_entry.delete(0, END)
			email_entry.delete(0, END)
			phone_entry.delete(0, END)
			username_entry.delete(0, END)

			

def delete():
	website = website_entry.get().lower()
	try:
		with open("password_saver.json", "r") as file:
			data = json.load(file)
	except:
		messagebox.showinfo(title="Errors",message="no such file...")
	else:
		try:
			website_info = data[website]
		except:
			messagebox.showinfo(title="Errors",message="no such website...")
		else:
			Delete =messagebox.askyesno(title="Delete...", message=f"we have find the  {website} website\n{website_info}\ndo you want to delete?")
			if Delete:
				place.delete("0.0",END)
				place.insert(END,f"the website {website} is deleted .")
				del data[website]
				data.update(data)
				with open("password_saver.json", "w") as file:
					json.dump(data, file,indent=4)
				website_entry.delete(0, END)
				password_entry.delete(0, END)
				email_entry.delete(0, END)
				phone_entry.delete(0, END)
				username_entry.delete(0, END)
				
			else:
				messagebox.showinfo(title="fine",message="Okey...")
				


def email_choose():
	choose = choice_emails.get()
	email_entry.delete(0, END)
	email_entry.insert(0, choose)

def phone_choose():
	choose = choice_phones.get()
	phone_entry.delete(0, END)
	phone_entry.insert(0, choose)

def search():
	website = website_entry.get().lower()

	if len(website)==0:
		messagebox.showinfo(title="Errors",message="empty entry not accept...")
	elif website == "!" :
		seeAll()
	else :
		try:
			with open("password_saver.json", "r") as file:
				data = json.load(file)
		except:
			messagebox.showinfo(title="Errors",message="no such file...")
		else:
			try:
				website_data = data[website]
			except KeyError :
				messagebox.showinfo(title="Errors",message="no such website...")
			else:
		
				password_entry.delete(0,END)
				username_entry.delete(0,END)
				phone_entry.delete(0,END)
				email_entry.delete(0,END)
				place.delete("0.0",END)

				place.insert(END,f"{website}\n\nemail:\t {website_data['email']}\n\nuser:\t {website_data['user']}\n\nphone:\t {website_data['phone']}\n\npassword:\t {website_data['password']}\n")
				
def seeAll():
	try:
		data= pd.read_json("./password_saver.json")
	except:
		messagebox.showinfo(title="Errors",message="no such file...")
	else:
		place.delete("0.0",END)
		for (index) in data:
				place.insert(END,f"> {index}\n")


def genarate():
	letters = choices(alphabel,k=6)
	number_s = choices(number,k=4)
	symbol_s = choices(symbol,k=2)
	list=[letter for letter in letters]
	list+=[number for number in number_s]
	list+=[symbol for symbol in symbol_s]
	shuffle(list)
	password = ''.join(list)
	password_entry.delete(0, END)
	password_entry.insert(0,password)


def reset():
	email_entry.delete(0, END)
	phone_entry.delete(0, END)
	username_entry.delete(0, END)
	password_entry.delete(0, END)
	website_entry.delete(0, END)
	place.delete("0.0",END)


#create GUI :

window = CTk()
window.title("Password saver")
window.geometry("900x500")

label = CTkLabel(window, text="Password saver",font=("Arial", 20,"bold"))
label.grid(column=1, row=0 ,padx=10,pady=10)

website_label = CTkLabel(window, text="Website	",font=LABEL_FONT)
website_label.grid(column=0, row=1, padx=10, pady=10)
website_entry = CTkEntry(window,width=300 ,corner_radius=CONORS_ENTRY ,border_width=BORDER_W,border_color=BORDER_C,text_color=TEXT_C,font=ENTRY_FONT,placeholder_text="! to see all ")
website_entry.grid(column=1, row=1,padx=10,pady=10)



email_label = CTkLabel(window ,text="Email	",font=LABEL_FONT)
email_label.grid(column=0, row=2,padx=10,pady=10)
email_entry = CTkEntry(window,width=300 ,corner_radius=CONORS_ENTRY ,border_width=BORDER_W,border_color=BORDER_C,text_color=TEXT_C,font=ENTRY_FONT)
email_entry.grid(column=1, row=2,padx=10,pady=10)

phone_label= CTkLabel(window ,text="Phone	",font=LABEL_FONT)
phone_label.grid(column=0, row=3,padx=10,pady=10)
phone_entry = CTkEntry(window,width=300 ,corner_radius=CONORS_ENTRY ,border_width=BORDER_W,border_color=BORDER_C,text_color=TEXT_C,font=ENTRY_FONT)
phone_entry.grid(column=1, row=3,padx=10,pady=10)


password_label= CTkLabel(window ,text="Password",font=LABEL_FONT)
password_label.grid(column=0, row=4,padx=10,pady=10)
password_entry = CTkEntry(window,width=300 ,corner_radius=CONORS_ENTRY ,border_width=BORDER_W,border_color=BORDER_C,text_color=TEXT_C,font=ENTRY_FONT)
password_entry.grid(column=1, row=4,padx=10,pady=10)

username_label= CTkLabel(window ,text="Username",font=LABEL_FONT)
username_label.grid(column=0, row=5,padx=10,pady=10)
username_entry = CTkEntry(window,width=300 ,corner_radius=CONORS_ENTRY ,border_width=BORDER_W,border_color=BORDER_C,text_color=TEXT_C,font=ENTRY_FONT)
username_entry.grid(column=1, row=5,padx=10,pady=10)

button_save = CTkButton(window, text="Save",width=150, command=save ,font=BUTTON_FONT)
button_save.grid(column=2, row=4,padx=10,pady=10)

button_delete = CTkButton(window, text="Delete",width=150, command=delete ,font=BUTTON_FONT)
button_delete.grid(column=3, row=1,padx=10,pady=10)

button_choose = CTkButton(window, text="Choose",width=150,command=email_choose ,font=BUTTON_FONT,)
button_choose.grid(column=3, row=2,padx=10,pady=10)

button_chooseP = CTkButton(window, text="Choose",width=150,command=phone_choose ,font=BUTTON_FONT)
button_chooseP.grid(column=3, row=3,padx=10,pady=10)

button_generate = CTkButton(window, text="Generate",width=150,command=genarate,font=BUTTON_FONT)
button_generate.grid(column=3, row=4,padx=10,pady=10)

button_reset = CTkButton(window, text="reset",width=150,command=reset,font=BUTTON_FONT)
button_reset.grid(column=2, row=5,padx=10,pady=10)

button_seeALL = CTkButton(window, text="see websites",width=150,command=seeAll,font=BUTTON_FONT)
button_seeALL.grid(column=3, row=5,padx=10,pady=10)

search_button = CTkButton(window, text="Search",width=150, command=search,font=BUTTON_FONT)
search_button.grid(column=2, row=1,padx=10,pady=10)

choice_emails = CTkComboBox(window,width=150,values=EMAILS)
choice_emails.grid(column=2, row=2,padx=10,pady=10,)

choice_phones = CTkComboBox(window,width=150,values=PHONES)
choice_phones.grid(column=2, row=3,padx=10,pady=10)

place = CTkTextbox(window,width=450*2,height=200,font=PLACE_FONT)
place.grid(column=0, row=6,pady=10,columnspan=4)




window.mainloop()


