from bravado.client import SwaggerClient

client = SwaggerClient.from_url("http://localhost:1234/books_api.json")

print client.books.getAllBooks().result()

idType = client.get_model('idType')
bookType = client.get_model('bookType')

book = bookType(identifier=idType(ISBN10='12345'), title='title goes here')

client.books.addBook(body=book).result()

print client.books.getAllBooks().result() 
