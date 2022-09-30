import requests,os,json,time
x = requests.get('http://ip-api.com/json').json()
ip = x['query']
ct = x['city']
os.system('clear')
z = time.ctime()
f = open("log.txt", "a")
f.write(f'{ip} -> {z} Has Logged In...\n')
f.close()

end = open("endtime.txt", "r")
print('Last Used ', end.readlines())
end.close()
print(f'''\033[1;31m    _  _  __    _          ___   _________
|V||_||_)(_ |_||_| |    |   | |V| |  |  _/
| || || \__)| || | |    |___|_| |_|_ | /__
\033[1;33m------------------------------------------
\033[1;37mIp\033[1;31m :\033[1;32m {ip}\033[1;31m ||\033[1;37m City\033[1;31m :\033[1;32m {ct}
\033[1;33m------------------------------------------
''')
os.system('php apiaxis.php')
f = open("endtime.txt", "w")
f.write(f'{z}')
f.close()
