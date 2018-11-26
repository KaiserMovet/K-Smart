import datetime
datetime.datetime.now()
def Log(string):
    with open("log.txt") as file:
        file.write(datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]\t"+string)
)