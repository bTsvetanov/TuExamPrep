from librery import Library

library = Library()

while True:
    print("\n--- Меню ---")
    print("1. Добави книга")
    print("2. Покажи всички книги")
    print("0. Изход")

    choice = input("Избери опция: ")

    if choice == "1":
        title = input("Заглавие: ")
        library.add_book(title)

    elif choice == "2":
        library.show_books()

    elif choice == "0":
        print("Довиждане!")
        break

    else:
        print("Невалиден избор. Опитай пак.")