from datetime import datetime as dt


def get_time():
    time_now = dt.now()
    return time_now


#讀取設定檔
def set_config():
    try:
        print("---開始讀取設定檔---")
        with open("./Get_Toy.conf", "r", encoding="utf-8") as conf:
            now_time = get_time()
            count = 1
            wish_list = []
            lines = conf.readlines()[1:]
            for line in lines:
                data = {"id":None,"name":None,"brand":None,"category":None,"status":None,"size":None,"release_date":None,"url":None,"tab_id":None}
                line = line.split(",")
                set_time = dt.strptime(line[0], '%Y-%m-%d %H:%M:%S')
                if set_time <= now_time:
                    print("釋出時間已過，第{}組設定失敗".format(count))
                    count += 1

                else:
                    set_url = line[1].replace("\n","")
                    data["id"] = count
                    data["release_date"] = set_time.strftime('%Y-%m-%d %H:%M:%S')
                    data["url"] = set_url
                    wish_list.append(data)
                    count += 1
            if wish_list == [] or wish_list == None:
                print("設定失敗，請檢查設定檔")
                return None
        if len(wish_list) != 0:
            print("完成設定，共{}組商品".format(len(wish_list)))
            return wish_list
    except Exception as e:
        print(e)
        print("找不到設定檔")