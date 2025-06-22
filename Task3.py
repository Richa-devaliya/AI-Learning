def add_fruit(basket, fruit):
    """Adds a fruit to the basket."""
    basket.append(fruit)
    print(f"{fruit} added to the basket.")

def show_fruits(basket):
    """Displays the fruits in the basket."""
    if not basket:
        print("The basket is empty.")
    else:
        print("Fruits in the basket:")
        for index, fruit in enumerate(basket):
            print(f"{index + 1}. {fruit}")

def update_fruit(basket, index, new_fruit):
    """Updates a fruit in the basket."""
    if 0 <= index < len(basket):
        basket[index] = new_fruit
        print(f"Fruit at index {index} updated to {new_fruit}.")
    else:
        print("Invalid index.")

def delete_fruit(basket, index):
    """Deletes a fruit from the basket."""
    if 0 <= index < len(basket):
        deleted_fruit = basket.pop(index)
        print(f"{deleted_fruit} deleted from the basket.")
    else:
        print("Invalid index.")

def main():
    """Main function to manage the fruit basket."""
    basket = []
    while True:
        print("\nFruit Basket Menu:")
        print("1. Add fruit")
        print("2. Show fruits")
        print("3. Update fruit")
        print("4. Delete fruit")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            fruit = input("Enter the fruit to add: ")
            add_fruit(basket, fruit)
        elif choice == '2':
            show_fruits(basket)
        elif choice == '3':
            show_fruits(basket)
            if basket:
                try:
                    index = int(input("Enter the index of the fruit to update: ")) - 1
                    new_fruit = input("Enter the new fruit name: ")
                    update_fruit(basket, index, new_fruit)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '4':
            show_fruits(basket)
            if basket:
                try:
                    index = int(input("Enter the index of the fruit to delete: ")) - 1
                    delete_fruit(basket, index)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()