with open("dane\logs.txt") as f:
    for line in f:
        line=line.split(";")
        user=line[0]
        action=line[1]
        time=line[2]
        time=int(time)
        #print(line,time)
        if action == "LOGIN":
            timeLogin={}
            timeLogin[user]=timeLogin.get(user, time)
            print(timeLogin)
        elif action == "LOGOUT":
            timeLogout={}
            timeLogout[user]=timeLogout.get(user, time)
