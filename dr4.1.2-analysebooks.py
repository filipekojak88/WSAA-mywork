import bookapidao

books = bookapidao.getallbooks()
total = 0
count = 0
for book in books:
    #print(book)
    total += book['price']
    count += 1
print(f"Average of {count} books is {total/count:.2f}")