#Import necessary libraries
import random
import datetime

#Create alphabet, numbers and special characters list
upper_alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers_list = ['0','1','2','3','4','5','6','7','8','9']
special_char_list = ['!','@','#','$','%','^','&','*']

#Today date extract
today_date = datetime.datetime.now()
 
#Concatenate above lists
password_list = upper_alphabet_list + lower_alphabet_list + numbers_list + special_char_list


gen_random_password_list = []
gen_random_password_str = ""
counter = 0

#Request the user to enter the name of the website or application intended to generate the password  
user_app_or_website = input("Enter Your App or Website For Generate password : ")
date_time = str(today_date.year) + "/" + str(today_date.month) + "/" + str(today_date.day)
user_input_len = int(input("Enter Your Length For Password(8 - 32) : "))


if (user_input_len >= 8) and (user_input_len <= 32):
    while counter < user_input_len:
        select_pass = random.choice(password_list)
        gen_random_password_list.append(select_pass)
        counter += 1
    for i in gen_random_password_list:
        gen_random_password_str += i

    #ُSave generate password into my_passwords.txt file
    password_file = open("my_passwords.txt", "a")
    password_file.write(user_app_or_website + "," + date_time + "," + gen_random_password_str + "\n")
    password_file.close()
else:
    print("God Bye! Your input number must be between 8 and 32")
    







