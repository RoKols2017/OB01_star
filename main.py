class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    # Метод для добавления товара в ассортимент
    def add_item(self, item_name, price):
        if item_name in self.items:
            print(f"Товар '{item_name}' уже существует.")
        else:
            self.items[item_name] = price
            print(f"Товар '{item_name}' успешно добавлен.")

    # Метод для удаления товара из ассортимента
    def remove_item(self, item_name):
        if item_name not in self.items:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")
        else:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")

    # Метод для получения цены товара по его названию
    # при отсутствии товара в словаре возвращает None
    def get_price(self, item_name):
        return self.items.get(item_name)

    # Метод для обновления цены товара
    def update_price(self, item_name, new_price):
        if item_name not in self.items:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")
        else:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' успешно обновлена.")


# Создание нескольких объектов класса Store
store1 = Store("Магазин 1", "ул. Ленина, д. 10")
store2 = Store("Магазин 2", "пр-т Мира, д. 20")
store3 = Store("Магазин 3", "ул. Пушкина, д. 30")

# Добавление товаров в магазины
store1.add_item('яблоки', 50)
store1.add_item('бананы', 70)
store2.add_item('апельсины', 80)
store2.add_item('груши', 60)
store3.add_item('виноград', 100)
store3.add_item('киви', 90)

# Тестирование методов на одном из магазинов
print("\nТестирование методов:")

# Получение цены товара
price = store1.get_price('яблоки')
if price is not None:
    print(f"Цена яблок: {price}")
else:
    print("Товар не найден.")

# Обновление цены товара
store1.update_price('яблоки', 55)
new_price = store1.get_price('яблоки')
print(f"Новая цена яблок: {new_price}")

# Удаление товара
store1.remove_item('бананы')
print(store1.items)

# Получение цены товара после его удаления
price = store1.get_price('бананы')
if price is not None:
    print(f"Цена яблок: {price}")
else:
    print("Товар не найден.")