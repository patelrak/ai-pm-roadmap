# # create a list

list_of_books_i_want_to_read = [  "Inspired by Marty Cagan",
    "AI Engineering by Chip Huyen",
    "The Hundred-Page ML Book",
    "Continuous Discovery Habits",
    "The Lean Product Playbook",
    "Empowered by Marty Cagan",
    "Prediction Machines",
    "Cracking the PM Interview",
    "Never Split the Difference",
    "Automate the Boring Stuff"]

# print(f"The books I want to read are:  {list_of_books_i_want_to_read}")
# print(f"the first book I want to read is: {list_of_books_i_want_to_read[0]}")
# print(f"the last book I want to read is: {list_of_books_i_want_to_read[-1]}")


# create a dictionary

book_authors = {"inspired by Marty Cagan": "Marty Cagan",
                "AI Engineering by Chip Huyen": "Chip Huyen",
                "The Hundred-Page ML Book": "Andriy Burkov",
                "Continuous Discovery Habits": "Teresa Torres",
                "The Lean Product Playbook": "Dan Olsen",
                "Empowered by Marty Cagan": "Marty Cagan",
                "Prediction Machines": "Ajay Agrawal",
                "Cracking the PM Interview": "Gayle Laakmann McDowell",
                "Never Split the Difference": "Chris Voss",
                "Automate the Boring Stuff": "Al Sweigart"}

# print(f"the author of inspired is {book_authors['inspired by Marty Cagan']}")

# book_authors["product management for dummies"] = "Brain Lawley"

# i = input("Enter the name of the book to be checked in library:")


# if i in book_authors:
#     print(f"{i} is in the dictionary")
# else: print(f"{i} is not in the dictionary")


# print("the books I will need to read are: \n")
# for book in list_of_books_i_want_to_read:
#     print(book)
    
    
# print("\n--- Books and their authors ---")
# for author, title in book_authors.items():
#     print(f"{title} -> {author}")


# Classify each book by title length

# print("\n--- Title length classification ---")
# for book in list_of_books_i_want_to_read:
#     title_length = len(book)

#     if title_length > 25:
#         category = "long title"
#     elif title_length > 15:
#         category = "medium title"
#     else:
#         category = "short title"

#     print(f"{book} ({title_length} chars) -> {category}")


# Find books by a specific author

target_author = input("enter the name of the author to find books: ")
matching_books = []

for title, author in book_authors.items():
    if author == target_author:
        matching_books.append(title)

print(f"\nBooks by {target_author}: {matching_books}")
print(f"Total: {len(matching_books)}")
print(target_author).lower()