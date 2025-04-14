# Задания 1
# class Player:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name
    
# class Team:
#     def __init__(self):
#         self.players = []

#     def add_player(self, player):
#         self.players.append(player)

#     def show_players(self):
#         print('Players in team:')
#         for player in self.players:
#             print(player)

# alice = Player('Alice')
# bob = Player('Bob')

# team = Team()
# team.add_player(alice)
# team.add_player(bob)

# team.show_players()

# Задание 2
# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name
    
# class Company:
#     def __init__(self, name):
#         self.name = name
#         self.employees = []

#     def add_employee(self, employee):
#         self.employees.append(employee)

#     def show_employees(self):
#         print(f'Employees in {self.name}:')
#         for emp in self.employees:
#             print(emp.name)

# john = Employee('John')

# company_a = Company('Company A')
# company_b = Company('Company B')

# company_a.add_employee(john)
# company_b.add_employee(john)

# company_a.show_employees()
# company_b.show_employees()

# Задания 3
# class House:
#     def __init__(self):
#         self.rooms = []

#     def count_rooms(self):
#         return len(self.rooms)
    
# class Room:
#     def __init__(self, house):
#         self.house = house
#         self.house.rooms.append(self)

# my_house = House()

# room1 = Room(my_house)
# room2 = Room(my_house)

# print('Number of rooms:', my_house.count_rooms())

# Задание 4
# class Page:
#     ...

# class Book:
#     def __init__(self, num_pages):
#         self.pages = []
        
#         for i in range(num_pages):
#             self.pages.append(Page())
    
#     def count_pages(self):
#         return len(self.pages)
    
# my_book = Book(3)

# print('Pages in book:', my_book.count_pages())

# Задания 5
# class CPU:
#     ...

# class RAM:
#     ...

# class Computer:
#     def __init__(self):
#         self.cpu = CPU()
#         self.ram = RAM()
#         self.cpu.name = 'Intel i7'
#         self.ram.capacity = '16GB'

# comp = Computer()

# print('Computer has:')
# print('CPU:', comp.cpu.name)
# print('RAM:', comp.ram.capacity)

# Задание 6
# class Song:
#     def __init__(self, title):
#         self.title = title

# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs_list = []

#     def add_song(self, song):
#         self.songs_list.append(song)

# my_favorite_song = Song('Yesterday')

# playlist = Playlist('Clasic Hits')
# playlist.add_song(my_favorite_song)

# del playlist

# try:
#     print(f"Song still exists: {my_favorite_song.title == 'Yesterday'}")
# except:
#     print('Song still exists: False')

# Задание 7 
class Paragraph:
    count = 0 

    def __init__(self, text):
        self.text = text
        Paragraph.count += 1
        print(f'Paragraph created. Total paragraphs: {Paragraph.count}')

    def __del__(self):
        Paragraph.count -= 1 
        print(f'Paragraph deleted. Paragraphs left: {Paragraph.count}')

class Document:
    def __init__(self):
        self.paragraphs = []
        print('Document created')

    def add_paragraph(self, text):
        paragraph =  Paragraph(text)
        self.paragraphs.append(paragraph)

    def __del__(self):
        print(f'Deleting document with {len(self.paragraphs)} paragraphs')

        for paragraph in self.paragraphs:
            del paragraph
        print('Document deleted')

if __name__ == '__main__':
    doc = Document()
    doc.add_paragraph('First paragraph')
    doc.add_paragraph('Second paragraph')
    doc.add_paragraph('Third paragraph')

    print(f'\nParagraphs before document deletion: {Paragraph.count}')

    del doc

    print(f'\nParagraphs after document deletion: {Paragraph.count}')