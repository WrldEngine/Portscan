import socket
import os
cyan='\033[35m'
yellow='\033[33m'
red='\033[31m'
def cls():
  os.system('cls' if os.name=='nt' else 'clear')
cls()
f = f'''
{yellow} _____           _    _____                                  
{red}|  __ \         | |  / ____|                                 
{cyan}| |__) |__  _ __| |_| (___   ___ __ _ _ __  _ __   ___ _ __  
{yellow}|  ___/ _ \| '__| __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__| 
{red}| |  | (_) | |  | |_ ____) | (_| (_| | | | | | | |  __/ |    
{cyan}|_|   \___/|_|   \__|_____/ \___\__,_|_| |_|_| |_|\___|_|            
{red}By Pulatov Kamran
Pulatov Kamran(C) 2021
'''
print(f)
print("Программа была создана Пулатовым Камраном/This programm created by やulสt๏v ⦃K🅰๓raή⦄")
print("=================================================================================")
ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000] 
print(yellow)
host = input('Введите имя сайта или IP адреc/Enter the site name or ip address> ')
  
print ("Processing...")
for port in ports:
    ps = socket.socket()
    ps.settimeout(1)
    try:
       ps.connect((host, port))
    except socket.error:
       pass
    else:
     ps.close
     print(cyan + host + ': ' + str(port) + ' порт в действий') 
     print("==================================================")
print("Конец")
