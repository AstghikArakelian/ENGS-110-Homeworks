import json
import os.path

def displayAllBooks(books):
    print("")
    for current_book in books:
        for current_key in current_book:
            print(current_key,":",current_book[current_key])

def getNumericInput(displayString):
    while(True):
        user_data = input(displayString)
        if(user_data.isnumeric()):
            user_data = int(user_data)
            return user_data
        else:
            print("Please insert a NUMBER")

def addBook():
    book = {
            "title":"",
            "num_of_pages": 0,
            "language":"",
            "author":"",
            "publishing_year":0,
            "last_time_read": {
                "day" : 0,
                "month":"",
                "year" : 0
            },
            "chapters" : []
            }

    book["title"] = input("Please insert the title:")
    book["num_of_pages"] = getNumericInput("Please insert the number of pages:")
    book["language"]= input("Please insert the language:")
    book["author"]= input("Who is the author:")
    book["publishing_year"] = getNumericInput("Please insert the year of publishing:")
    last_time_read = input ("When did you last read this book?: Please insert date with the format: DD/MM/YYYY")
    last_time_read = last_time_read.split("/")
    book["last_time_read"]["day"] = int (last_time_read[0])
    book["last_time_read"]["month"] = last_time_read[1]
    book["last_time_read"]["year"] = int(last_time_read[2])
    while(True):
        chapter = input("please insert a chapter to the book; insert END to finish")
        if (chapter == "END"):
            break
        else:
            book["chapters"].append(chapter)
    return book

def loadExistingBooks():
    if(os.path.exists("books.json")):
        with open('books.json') as file_data:
            print(file_data)
            books = json.load(file_data)
            return books
    else:
        return []

def saveToTheFile(books):
    f = open("books.json","w")
    print(books)
    f.write(json.dumps(books,indent=2))
    f.close()

def main():

    books = []
    books= loadExistingBooks()

    while(True):
        insert_mode = input("Do you want to start adding books?, Answer yes or no")
        if(insert_mode == "no"):
            print("Good bye")
            break
        else:
            book = addBook()
            books.append(book)

    print("Saving to the file ")
    saveToTheFile(books)
    displayAllBooks(books)

main()
