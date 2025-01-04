class Market:
    def __init__(self, market):
        self.market = market
        self.file = None
        try:
            self.file = open("product.txt", "a+")
            self.file.seek(0)
            print("product.txt file opened")
        except Exception as e:
            print(f"File failed to open {e}")

    def __del__(self):
        if self.file:
            self.file.close()

    def list_product(self):
        try:
            with open("product.txt", "r") as file:
                readings = file.read()
                lines = readings.splitlines()

            if not lines:
                print("The list is empty, no products have been added")
                return

            print(f"{'Product':<15} {'Category':<15} {'Price':<10} {'Stock':<10}")
            print("-" * 50)

            for line in lines:
                data = line.split(",")
                print(f"{data[0]:<15} {data[1]:<15} {data[2]:<10} {data[3]:<10}")

        except FileNotFoundError:
            print("product.txt file not found. Add product first")
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_product(self):
        name = str(input("Please enter a product name: ")).strip()
        category = str(input("Please enter the product category: ")).strip()

        try:
            price = float(input("Please enter the product price: "))
            stock = int(input("Please enter stock: "))

            if price < 0 or stock < 0:
                print("Price and stock values must be positive")
                return
        except ValueError:
            print("Invalid value.Price and stock values must be positive")

        new_product = f"{name},{category},{price},{stock}\n"

        try:
            with open("product.txt", "a") as file:
                file.write(new_product)
                print(f"{name} product successfully added")

        except Exception as e:
            print(f"An error occurred while adding the product: {e}")

    def delete_product(self):
        try:
            with open("product.txt", "r") as file:
                list = file.readlines()

            if not list:
                print("The product list is empty")
                return

        except FileNotFoundError:
            print("The product database does not exist")
            return

        name = input("Please enter the name of the product you want to delete: ")

        product_found = False
        updated_list = []
        for line in list:
            product_data = line.split(",")
            if product_data[0] == name:
                product_found = True
                deleted_product = line.strip()
            else:
                updated_list.append(line)

        if not product_found:
            print(f"The product '{name}' was not found in the list.")
            return

        try:
            with open("product.txt", "w") as file:
                file.writelines(updated_list)
            print(f"Product successfully deleted: {deleted_product.strip()}")
        except Exception as e:
            print(f"An error occured while updating the file: {e}")


grocery = Market("My Grocery Store")

print("***MENU***")

while True:
    print("Choose an option:\n"
          "1. List products\n"
          "2. Add product\n"
          "3. Delete product\n"
          "4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        print("Products in the product.txt file: ")
        print(grocery.list_product())
    elif choice == "2":
        grocery.add_product()
    elif choice == "3":
        grocery.delete_product()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice.Try again. ")
