import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["vk.com", "mail.ru"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_temp, "r+") as my_file:
            #content = my_file.read()
            for website in website_list:
                if website in my_file:
                    pass
                else:
                    line = "\n" + redirect + "\t" + website
                    my_file.write(line)
    else:
        with open(hosts_temp, "r+") as my_file:
            content = my_file.readlines()
            my_file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    my_file.write(line)
            my_file.truncate()
        print("Free time...")
    time.sleep(5)