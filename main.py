from core.commands import *
from core.analytics import *

def menu():
    while True:
        print("\nPURCHASE TRACKER")
        print("1. Добавить покупку")
        print("2. Показать покупки")
        print("3. Удалить покупку")
        print("4. Общие расходы")
        print("5. Анализ по категориям")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_purchase()

        elif choice == "2":
            show_purchases()

        elif choice == "3":
            delete_purchase()

        elif choice == "4":
            total_expenses()

        elif choice == "5":
            category_stats()

        elif choice == "6":
            print("Выход...")
            break

        else:
            print("Неверный ввод")

if __name__ == "__main__":
    menu()