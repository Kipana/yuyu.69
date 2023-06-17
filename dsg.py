import customtkinter 
import customtkinter 

app = customtkinter.CTk() 
 
app.title('เครื่องลิงคิด') 
app.geometry('500x1000') 

label = customtkinter.CTkLabel(app, text="เครื่องลิงคิด", fg_color="transparent", font=("Aria", 56))
label.pack(pady=(20,0)) 

answer_text = customtkinter.StringVar() 
answer_lable= customtkinter.CTkLabel(app, textvariable=answer_text, font=('Aria', 49)) 
answer_lable.pack(pady=(20,0)) 



entry = customtkinter.CTkEntry(app, placeholder_text="(CTkEntry)") 
entry.pack(pady=(15, 0)) 

import random

def button_event():
    user_input = entry.get()
    answer = eval(user_input)
    operation = random.choice(['add', 'subtract', 'multiply', 'divide'])
    random_value = random.randint(1, 10)  # Generate a random value to manipulate the answer

    if operation == 'add':
        answer = answer + random_value
    elif operation == 'subtract':
        answer = answer - random_value
    elif operation == 'multiply':
        answer = answer * random_value
    elif operation == 'divide':
        answer = answer / random_value

    answer_text.set(answer)
    print(user_input, answer)
button = customtkinter.CTkButton(app, text="ตอก", command=button_event) 
button.pack(pady=(50,0)) 
app.mainloop() 