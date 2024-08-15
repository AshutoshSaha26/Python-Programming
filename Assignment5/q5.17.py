class Item:
    def __init__(self, code, price):
        self.code = code
        self.price = price

    def display(self):
        return f"{self.code}\t{self.price:.2f}"
if __name__ == "__main__":
    items = []
    for i in range(5):
        code = input(f"Enter code for item {i + 1}: ")
        price = float(input(f"Enter price for item {i + 1}: "))
        items.append(Item(code, price))
    print(f"{'Code':<10}{'Price':<10}")
    print("-" * 20)
    total_price = 0
    for item in items:
        print(item.display())
        total_price += item.price
    print("-" * 20)
    print(f"{'Total Price':<10}{total_price:.2f}")
