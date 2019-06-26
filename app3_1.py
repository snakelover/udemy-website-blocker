import time
from datetime import datetime as dt, timedelta as td

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["vk.com", "mail.ru"]
start_hour = 9
finish_hour = 17

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, finish_hour):
        print("Working hours...")
        with open(hosts_temp, "r+") as my_file:
            #content = my_file.read()
            for website in website_list:
                if website in my_file:
                    pass
                else:
                    line = "\n" + redirect + "\t" + website
                    my_file.write(line)
        date_to_wait = dt(dt.now().year, dt.now().month, dt.now().day, finish_hour)
    else:
        with open(hosts_temp, "r+") as my_file:
            content = my_file.readlines()
            my_file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    my_file.write(line)
            my_file.truncate()
        print("Free time...")
        date_to_wait =  dt.dt(dt.now().year, dt.now().month, dt.now().day, start_hour)
        if dt.now().hour > start_hour:
            date_to_wait += td(days=1)
    time.sleep(round(date_to_wait - dt.now()).total_seconds)