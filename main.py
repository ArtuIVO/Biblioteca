from book import Book
from stack import Stack

books = Stack()


def load_data():
    book1 = Book(152512345, "Señor Presidente", "Miguel Angel Asturias")
    books.prepend(book1)

    book2 = Book(123456789, "Doña Barbara", "Romulo Gallegos")
    books.prepend(book2)

    book3 = Book(246810121, "1 poema de amor y 20 canciones deseperadas", "Pablo Neruda")
    books.prepend(book3)


def add_book() -> Book | None:
    try:
        a = int(input("Coloque el ISBN: "))
        b = input("El titulo del libro: ")
        c = input("El autor del libro: ")
        new_book = Book(a, b, c)
        if new_book.isbn == books.head.data.isbn:
            print("Este libro ya existe")
        else:
            books.prepend(new_book)

    except Exception:
        return None


def find_book(isbn: int) -> Book | None:
    aux_books = Stack()
    try:
        for i in range(books.size):
            head = books.shift()
            if head.isbn == isbn:
                for j in range(aux_books.size):
                    head_aux = aux_books.shift()
                    books.prepend(head_aux)
                return head
            else:
                aux_books.prepend(head)
    except Exception:
        return None


def main():
    load_data()
    print("Agregue su nuevo libro:")
    new_book = add_book()

    #isbn = int(input("Ingrese el ISBN: "))
    #book = find_book(isbn)
    #if book is None:
        #print("El libro no existe")
    #else:
        #print("El libro a prestar es:", book)

    print("Mi pila de libros:")
    print(books.transversal())


main()
