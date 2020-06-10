import json

moneydata={'DrLee_lihr':0}

def on_server_startup(server):
    with open('./MoneyData/data.txt',mode="r") as file:
        jsObj=file.read()
        file.close()
        moneydata=json.loads(jsObj)
        jsObj=''

def on_server_stop(server,returncode):
    jsObj=json.dumps(moneydata)
    with open('./MoneyData/data.txt',mode='w') as file:
        file.write(jsObj)
        file.close()
        jsObj=''

def money_query(playername):
    try:
        temp=moneydata[playername]
    except KeyError:
        raise KeyError("银行查无此人")
    else:
        return temp

def money_add(playername,num):
    try:
        moneydata[playername]+=num
    except KeyError:
        moneydata[playername]=num
    finally:
        return moneydata[playername]

def money_add_safety(playername,num):
    try:
        tmp=moneydata[playername]
    except KeyError:
        if num<0:
            raise KeyError("为什么找这个没账户的人扣钱？")
        else:
            moneydata[playername]=num
    else:
        if moneydata[playername]<(-num):
            raise ValueError("这人没钱了")
        else:
            moneydata[playername]+=num

def money_set(player,num):
    moneydata[player]=num

def money_set_safety(player,num):
    if 0>num:
        raise ValueError("")
    else:
        moneydata[playername]=num
