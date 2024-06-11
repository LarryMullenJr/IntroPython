class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

class InventorySystem:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"Added {name} to the inventory.")

    def update_quantity(self, product_name, new_quantity):
        for product in self.products:
            if product.name == product_name:
                product.update_quantity(new_quantity)
                print(f"Updated quantity of {product_name} to {new_quantity}.")
                return
        print(f"Product {product_name} not found in inventory.")

    def display_inventory(self):
        print("Inventory:")
        for product in self.products:
            product.display_info()

    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of inventory: ${total_value:.2f}")

def main():
    inventory_system = InventorySystem()

    inventory_system.add_product("Laptop", 999.99, 10)
    inventory_system.add_product("Phone", 599.99, 20)

    inventory_system.update_quantity("Laptop", 8)
    inventory_system.update_quantity("Tablet", 15)

    inventory_system.display_inventory()
    inventory_system.calculate_total_value()

if __name__ == "__main__":
    main()