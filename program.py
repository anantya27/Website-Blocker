import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites=["www.facebook.com","facecbook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<=  dt.now()   <= dt(dt.now().year,dt.now().month,dt.now().day,12):
        print("working hours")
        with open(hosts_path,'r+')as file:
            content=file.read()
            for w in websites:
                if w in content:
                    pass
                else:
                    file.write(redirect+" "+w+"\n")
    else:
        with open(hosts_path,'r+')as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(w in line for w in websites ):
                    file.write(line)
                file.truncate()
            print("freetime")
    time.sleep(5)
