user_last_login = {}
user_total_time = {}



with open("dane\logs.txt") as f:
    for line in f:
        user, action, time_str = line.split(";")
        time=int(time_str)
        if action == 'LOGIN':
            user_last_login[user] = time
        elif action == 'LOGOUT':
            time_temp = time - user_last_login[user]
            user_total_time[user] = user_total_time.get(user, 0) + time_temp

print("Czas przebywania w systemie: ")
for user, time in sorted(user_total_time.items(), key=lambda x: x[1]):
    print(f' - {user}: {time} s')
print(user_last_login)