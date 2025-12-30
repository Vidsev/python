import sys

balance = 10000
pin = "1234"
attempts = 3
history = []
operation_number = 1
last_operation = None


def save_history(op_type, amount, balance_after):
    global operation_number, last_operation
    operation = {
        "№": operation_number,
        "тип": op_type,
        "сумма": amount,
        "баланс": balance_after
    }
    history.append(operation)
    last_operation = operation
    operation_number += 1


# Проверка PIN
while attempts > 0:
    entered_pin = input("Введите PIN: ")
    if entered_pin == pin:
        print("✓ Доступ разрешён\n")
        break
    else:
        attempts -= 1
        print(f"Неверный PIN. Осталось попыток: {attempts}")
else:
    print("Карта заблокирована.")
    sys.exit()


while True:
    print("\n=== БАНКОМАТ ===")
    print("1. Проверить баланс")
    print("2. Снять деньги")
    print("3. Пополнить счёт")
    print("4. Перевести на другой счёт")
    print("5. История операций")
    print("6. Отменить последнюю операцию")
    print("7. Сменить PIN-код")
    print("8. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        print(f"Баланс: {balance} руб.")

    elif choice == "2":
        amount = int(input("Сумма для снятия: "))
        if amount > 5000:
            print("Лимит: не более 5000 за операцию")
        elif amount > balance:
            print("Недостаточно средств")
        else:
            balance -= amount
            save_history("снятие", amount, balance)
            print(f"✓ Снято {amount} руб. Баланс: {balance}")

    elif choice == "3":
        amount = int(input("Сумма пополнения: "))
        balance += amount
        save_history("пополнение", amount, balance)
        print(f"Счёт пополнен на {amount} руб.")

    elif choice == "4":
        amount = int(input("Сумма перевода: "))
        commission = int(amount * 0.01)
        total = amount + commission
        if total > balance:
            print("Недостаточно средств")
        else:
            balance -= total
            save_history("перевод", amount, balance)
            print(f"Перевод выполнен. Комиссия: {commission} руб.")

    elif choice == "5":
        print("\nИстория операций:")
        for h in history:
            print(f"{h['№']}. {h['тип']} {h['сумма']} руб. (баланс {h['баланс']})")

    elif choice == "6":
        if history:
            history.pop()
            balance = history[-1]["баланс"] if history else 10000
            print("Последняя операция отменена")
        else:
            print("Нет операций для отмены")

    elif choice == "7":
        pin = input("Введите новый PIN: ")
        print("PIN-код изменён")

    elif choice == "8":
        print("До встречи")
        break

#задание 2

hall = [[0] * 10 for _ in range(8)]
prices = {1: 500, 2: 500, 3: 500, 4: 300, 5: 300, 6: 300, 7: 200, 8: 200}
revenue = 0


def show_hall():
    print("\nСхема зала:")
    print("     ", end="")
    for i in range(1, 11):
        print(f"{i:2}", end=" ")
    print()

    for i, row in enumerate(hall):
        print(f"Ряд {i + 1} ", end="")
        for seat in row:
            print("[X]" if seat else "[0]", end="")
        print(f"  {prices[i + 1]}₽")


def show_stats():
    free = sum(seat == 0 for row in hall for seat in row)
    taken = 80 - free
    percent = taken / 80 * 100
    popular_row = max(range(8), key=lambda r: sum(hall[r])) + 1

    print("\nСтатистика:")
    print(f"Свободно: {free}")
    print(f"Занято: {taken}")
    print(f"Заполненность: {percent:.2f}%")
    print(f"Самый популярный ряд: {popular_row}")
    print(f"Выручка: {revenue} руб.")


while True:
    print("\n=== КИНОТЕАТР ===")
    show_hall()

    print("\nМеню:")
    print("1. Забронировать места")
    print("2. Отменить бронь")
    print("3. Показать статистику")
    print("4. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        count = int(input("Сколько мест?: "))
        selected = []
        total_price = 0

        for _ in range(count):
            row = int(input("Ряд: ")) - 1
            seat = int(input("Место: ")) - 1
            if hall[row][seat] == 0:
                selected.append((row, seat))
                total_price += prices[row + 1]
            else:
                print("Место уже занято")

        confirm = input(f"Итого {total_price} руб. Подтвердить? (да/нет): ")
        if confirm.lower() == "да":
            for r, s in selected:
                hall[r][s] = 1
            revenue += total_price
            print("✓ Бронирование успешно 😌")

    elif choice == "2":
        row = int(input("Ряд: ")) - 1
        seat = int(input("Место: ")) - 1
        if hall[row][seat] == 1:
            hall[row][seat] = 0
            print("✓ Бронь отменена")
        else:
            print("Место и так свободно")

    elif choice == "3":
        show_stats()

    elif choice == "4":
        print("Хорошего просмотра 😉")
        break

def main():
    show_hall()
    show_stats()

main()