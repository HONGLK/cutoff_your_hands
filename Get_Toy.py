import Setup, Browser_op

url = {"start_up":"https://global.taobao.com",
    "Labu_Test":"https://detail.tmall.com/item.htm?spm=a312a.7700824.w4011-15691211890.32.41945742dYJIMW&id=616642818126&rn=fc058cd0d627f99c2350c0e5ae086c58&abbucket=4&sku_properties=134942334:28316"
    }
        



          
def main(url):
    toy_list = Setup.set_config()
    if toy_list == None:
        return
    #login = True
    login = Browser_op.login(url)
    if login:
        Browser_op.get_good_prop(toy_list)
    else:
        print("登入異常，重新登入")
        login = Browser_op.login(url)



if __name__ == "__main__":
    main(url)