import inflection

title = "python libraries to import for data science programs"
title_formatted = inflection.parameterize(title, separator='_').title()
print(title_formatted)

# Starter code
class Garage:
  def __init__(self, size):
    self.size = size
    self.cars = ["Ram", "Model 3"]

  def open_door(self):
    return "The door opens"
    
home = Garage(2)
# End of starter code
home.cars = []
# Setter goes here

get_cars = home.cars # Getter goes here

print(get_cars)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Libro: {self.title} by {self.author}, {self.pages} pages"

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
print(book1)