library = []

def add_book():
    title = input("please enter your book title:")
    author = input("please enter your book author:")
    year = input("please enter your book year:")

    book = {"title": title, "author": author,"year": year}
    library.append(book)
    print(f"book {title} added to library")

def show_book():
    if not library:
        print("no book found!!")
    else:
        print("-----list of books----")
        for i, book in enumerate(library,start=1):
            print(f"{i}. {book["title"]} - {book["author"]} - ({book["year"]})")
        print()

def search_book():
    keywords = input("please enter your search keyword:")
    result = [book for book in library if keywords in book["title"].lower()]
    if result:
        print("your search result:")
        for book in result:
            print(f" - {book["title"]} - {book["author"]}  ({book["year"]})")
        print()
    else:
        print("no book found!!")
def remove_book():
    title = input("please enter your book title:")
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("book was removed from library")
            return
    print("no book found!!")

def main():
    while True:
        print("--------menu library----------")
        print("1.add new book")
        print("2.show all book")
        print("3.search  book")
        print("4.remove book")
        print("5.exit")

        choice = input("please enter your choice:")
        if choice == "1":
            add_book()
        elif choice == "2":
            show_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("GoodBye")
            break
        else:
            print("invalid choice!!")

if __name__ == "__main__":
    main()
