shopping_list = []

def reverse(item):
    return item[-1::-1]

def add_item(item: str):
    shopping_list.append(item)
    print("Added item")
    
def remove_item(item: str):
    shopping_list.remove(item)
    print("Removed item")

def search_item(item: str) -> bool:
    for i in shopping_list:
        if i == item:
            return True
    return False

def display_list():
    print("\nShopping list is: ")
    for i in shopping_list:
        print(i, end = ' ')
    print("\n")

def binary_seach(item: str):
    lo = 0
    hi = len(shopping_list) - 1
    shopping_list.sort()
    while(lo<=hi):
        mid = (lo + hi) // 2
        if(item == shopping_list[mid]):
            print(f"\nElement found!, in reverse it is: {reverse(item)}\n")
            return
        elif(item < shopping_list[mid]):
            hi = mid - 1
        else:
            lo = mid + 1
    print("element not found!")

def main():
    running = True
    while running:
        print("Choose an option: ")
        print("1. Add item: ")
        print("2. Remove item: ")
        print("3. Search item: ")
        print("4. Display shopping list: ")
        print("5. Exit")
        print("6. Binary Search")
        n = int(input("Enter choice number: "))
        if n == 1:
            item = input("Enter item you wish to add: ")
            add_item(item)
        elif n == 2:
            item = input("Enter item you wish to remove: ")
            remove_item(item)
        elif n == 3:
            item = input("Enter item you wish to search: ")
            is_present = search_item(item)
            print()
            if(is_present):
                print(f"{item} is present in the shoping list!")
            else:
                print(f"{item} is not present in the shopping list.")
            print()
        elif n == 4:
            display_list()
        elif(n == 5):
            running = False
        elif n == 6:
            item = input("enter item you wish to search: ")
            binary_seach(item)
        
if __name__ == "__main__":
    main()
    