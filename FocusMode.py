import time
import datetime
import ctypes,sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    

if is_admin():
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time = input("Enter the example :-  [10:10]:- ")


    host_path ='C:\Windows\System32\drivers\etc\hosts'
    redirect = '127.0.0.1'

    print(current_time)

    website_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]

    a = current_time.replace(":",".")
    a = float(a)
    b = stop_time.replace(":",".")
    b = float(b)
    Focus_time = b-a
    Focus_time = round(Focus_time,3)



    time.sleep(2)

    if (current_time >= stop_time):
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()


            print("Websites are unblocked !!")
            file = open("focus.txt","a")
            file.write(f",{Focus_time}")        #Write a 0 in focus.txt before starting
            file.close()
            break 
