# задачка 1
import random
from colorama import init, Fore

init()

number = random.randint(1, 100)
attempts = 0

print("я загадал число от 1 до 100. попробуй угадать")

while True:
    try:
        guess = int(input("введите ваше число: "))
        attempts += 1
        if guess > number:
            print(Fore.RED + "горячо")
        elif guess < number:
            print(Fore.BLUE + "холодно")
        else:
            print(Fore.GREEN + f"поздравляю! вы угадали число за {attempts} попыток.")
            break
    except ValueError:
        print("пожалуйста, введите целое число.")

# задачка 2
import time
import os

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        current_time = time.strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nПрограмма завершена.")

# задачка 3
import requests

url = input("Введите URL сайта: ")

try:
    response = requests.get(url, timeout=5)
    if response.status_code < 400:
        print(f"сайт доступен! код ответа: {response.status_code}")
    else:
        print(f"сайт недоступен! код: {response.status_code}")
except requests.exceptions.RequestException:
    print("ошибка подключения: таймаут / нет сети")