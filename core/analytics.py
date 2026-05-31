from core.storage import load_purchases

def total_expenses():
    purchases = load_purchases()

    total = sum(item["price"] for item in purchases)

    print(f"Общие расходы: {total} руб.")

def category_stats():
    purchases = load_purchases()

    stats = {}

    for item in purchases:
        category = item["category"]

        if category not in stats:
            stats[category] = 0

        stats[category] += item["price"]

    print("\nРасходы по категориям:")

    for category, amount in stats.items():
        print(f"{category}: {amount} руб.")
        