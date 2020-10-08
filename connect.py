import os
os.system("pip3 install colorama")
os.system("pip3 install time")
import colorama
from colorama import Fore
from colorama import init
init(autoreset=True)
import time

xx = 0

while xx == 5:
	print("Starting...")
	time.sleep(0.3)
	os.system("clear")
	print("sTarting...")
	time.sleep(0.3)
	os.system("clear")
	print("stArting...")
	time.sleep(0.3)
	os.system("clear")
	print("staRting...")
	time.sleep(0.3)
	os.system("clear")
	print("starTing...")
	time.sleep(0.3)
	os.system("clear")
	print("startIng...")
	time.sleep(0.3)
	os.system("clear")
	print("startiNg...")
	time.sleep(0.3)
	os.system("clear")
	print("startinG...")
	time.sleep(0.3)
	os.system("clear")
	xx += 1


# Installing packets...
def Install_packets():
	os.system("clear")
	print(Fore.GREEN + "----Установка/обновление пакетов...----")
	os.system("apt install python")
	os.system("apt install pip")
	os.system("apt install netcat")
	os.system("apt install irssi")
	os.system("pip3 install colorama")
	os.system("clear")
	time.sleep(3)

Install_packets()

while True:
	nick = input("Nick: ")
	accepting = input("Твой ник: " + nick + "? y/n ")
	if accepting == "y":
		break
	if accepting == "n":
		pass
os.system("clear")

#Main code

print("Для захода в канал нужно ввести /join #horan_chat")
print("Через 10 секунд запуститься интерфейс. Ожидайте.")
time.sleep(10)
print("[+] Connecting to the server...")
os.system("clear")

#For stop script

print("нажмите комбинацию ctrl+z, чтобы выйти из приложения")
os.system('irssi --connect=chat.freenode.net --nick="' + nick + '"')
