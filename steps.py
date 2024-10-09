import requests,random,sys

user = sys.argv[1]
passwd = sys.argv[2]
steps = sys.argv[3]
#steps = str(random.randint(6888,8888))

user_list = user.split('#')
passwd_list = passwd.split('#')
step_array = steps.split('-')

if len(user_list) == len(passwd_list):
    for line in range(0,len(user_list)):
        if len(step_array) == 2:
            step = str(random.randint(int(step_array[0]),int(step_array[1])))
        elif str(steps) == '0':
            step = str(random.randint(6888,8888))
        else:
            step=steps
        print (f"设置步数" + step)            
        url1 = "https://api.qoc.cc/api/mi?user=" + user_list[line] + "&pass=" + passwd_list[line] + "&count=" + step 
        result1 = requests.get(url1)
        print(result1.text)    
else:
    print('用户名和密码数量不对')
    
