class Person:
    def __init__(self, name):
        self.__name = name
        self.room_number = None

    @property
    def name(self):
        return self.__name

    def in_room(self, room_number):
        self.room_number = room_number

    def room_out(self):
        self.room_number = None

    def __str__(self):
        return self.name


class Room:

    def __init__(self, number):
        self.__number = number
        self.status = 'empty'

    @property
    def number(self):
        return self.__number

    def change_status(self, status):
        try:
            self.status.room_out()
        except AttributeError:
            pass
        if status == 'empty' or status == 'repair':
            self.status = status
        else:
            self.status = status
            status.in_room(self)

    def chek(self):
        if self.status in ('empty', 'repair'):
            print(f'Room number {self.number} is {self.status}.')
        else:
            print(f'In room number {self.number} lives {self.status}.')

    def __str__(self):
        return str(self.number)


class Hotel:

    def __init__(self, number_of_rooms):
        if number_of_rooms >= 1:
            self.rooms = [Room(i+1) for i in range(number_of_rooms)]
        else:
            print('Oops some mistake, enter number again!')

    def hotel_rooms_available(self):
        for i in self.rooms:
            print(f'{i.number} - {i.status}')

    def place_in_the_room(self, number, user):
        for i in self.rooms:
            if number == i.number and i.status == 'empty':
                i.change_status(user)
                print('\nSuccessfully!')
            elif 0 < number > len(self.rooms):
                print(f'\nSorry, this hotel  don\'t have room with number {number}.')
                break
            elif number == i.number and i.status != 'empty':
                print(f'\nSorry, this number {number} is busy.')

    def displace_out(self, user):
        for i in self.rooms:
            if i.status == user:
                i.change_status('empty')
                print('\nSuccessfully!')

    def room_on_repair(self, number):
        for i in self.rooms:
            if number == i.number and i.status == 'empty':
                i.change_status('repair')
                print('\nSuccessfully!\n')
            elif 0 < number > len(self.rooms):
                print(f'Sorry, this hotel  don\'t have room with number {number}.')
            elif number == i.number and i.status != 'empty':
                print(f'Sorry, this number {number} is busy.')


def reception_menu(rooms):
    hotel = Hotel(rooms)
    person_dict = {}
    while True:
        print('Hello! Select an action.\n'
              '1. Print available numbers\n'
              '2. Place in room\n'
              '3. Check out the room\n'
              '4. Renovate the room\n'
              '5. Check which room the guest is staying in\n'
              '0. Exit')
        menu_choice = int(input('Enter: '))
        if menu_choice == 1:
            hotel.hotel_rooms_available()
            print('')
        elif menu_choice == 2:
            room_number = int(input('Enter room number: '))
            name = input('Enter name of person: ')
            if person_dict.get(name) is None:
                person_dict[name] = Person(name)
            person = person_dict[name]
            hotel.place_in_the_room(room_number, person)
            print('')
        elif menu_choice == 3:
            name = input('Enter name of person: ')
            if person_dict.get(name) is None:
                print(f'Sorry, no guest with the name {name}\n')
            else:
                person = person_dict[name]
                hotel.displace_out(person)
        elif menu_choice == 4:
            room_number = int(input('Enter room number: '))
            hotel.room_on_repair(room_number)
        elif menu_choice == 5:
            name = input('Enter name of person: ')
            if person_dict.get(name) is None:
                print(f'\nSorry, no guest with the name {name}\n')
            else:
                print(
                    f"\nThe guest {person_dict[name]} is staying in room with number {person_dict[name].room_number}\n")
        elif menu_choice == 0:
            print('\nBye!')
            break


reception_menu(10)
