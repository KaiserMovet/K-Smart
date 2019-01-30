import datetime
datetime.datetime.now()
def Log(string):
    message=str(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S:%f]\t"+string+";\n"))
    print(message)
    #with open("log.txt","a+") as file:
    #        file.write(message)
