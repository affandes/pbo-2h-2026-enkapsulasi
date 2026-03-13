from book import Book

# buat objek buku
b1 = Book(1234, "Learn Python", "Affan")
b2 = Book(2987, "Mastering OOP", "Budi")

print(b1.get_title())
print(b2.get_title())

b1.set_title("US")

print(b1.get_title())
print(b2.get_title())