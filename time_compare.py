import Setup
import datetime
from datetime import datetime as dt
def tc(data):
    target_time = [] 
    for t in data:
        time = dt.strptime(t["release_date"],'%Y-%m-%d %H:%M:%S') #dt.strptime(Setup.set_config()[0]["release_date"],'%Y-%m-%d %H:%M:%S')
        target_time.append(time)
    while True:
        now_time = Setup.get_time()
        print(now_time)
        #print(target_time - now_time)

        if target_time[0] - now_time <= datetime.timedelta(milliseconds=300):
            reach_target_time = True
            print('your time has come.')
            return reach_target_time