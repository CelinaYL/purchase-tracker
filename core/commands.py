from core.storage import load_purchases, save_purchases

def add_purchase():
    name = input("Название покупки: ")
    price = float(input("Цена: "))
    category = input("Категория: ")
    date = input("Дата: ")

    purchases = load_purchases()

    purchases.append({
        "name": name,
        "price": price,
        "category": category,
        "date": date
    })

    save_purchases(purchases)

    print("Покупка добавлена")

def show_purchases():
    purchases = load_purchases()

    if not purchases:
        print("Покупок нет")
        return

    for i, item in enumerate(purchases):
        print(
            f"{i}. {item['name']} | "
            f"{item['price']} руб | "
            f"{item['category']} | "
            f"{item['date']}"
        )

def delete_purchase():
    purchases = load_purchases()

    show_purchases()

    index = int(input("Введите номер покупки: "))

    if 0 <= index < len(purchases):
        purchases.pop(index)
        save_purchases(purchases)
        print("Покупка удалена")
    else:
        print("Неверный индекс")