def read_list():
    base = open('base.txt', 'r')
    base_list = base.read().split(',')
    base_list.remove('')
    return base_list


def add_new_in_list(name_car):
    base = open('base.txt', 'a')
    base.write(f'{name_car},')
    base.close()
    print('\nSuccessfully add in list!')


def save_list(base_list):
    base = open('base.txt', 'w')
    for name_car in base_list:
        base.write(f'{name_car},')
    base.close()


def delete_in_list(name_car):
    base_list = read_list()
    if name_car in base_list:
        base_list.remove(name_car)
        print(f'\n{name_car} is delete!\n')
    else:
        print(f'\n{name_car} not find in list!\n')
    save_list(base_list)
    return base_list


def print_records():
    if read_list():
        n = 1
        for i in read_list():
            print(f'{n}: {i}')
            n += 1
        print('')
    else:
        print('\nNo records\n')


def menu():
    while True:
        print('Hello! Select an action.\n'
              '1. Print list\n'
              '2. New record\n'
              '3. Delete record\n'
              '0. Exit')
        menu_choice = int(input('Enter: '))
        print('')
        if menu_choice == 1:
            print_records()
        elif menu_choice == 2:
            name = input('Enter name of person: ')
            car = input('Enter mark of car: ')
            add_new_in_list(f'{name}-{car}')
            print('')
        elif menu_choice == 3:
            print_records()
            number = input('Enter number of records: ')
            if number.isdigit():
                number = int(number)
                try:
                    delete_in_list(f'{read_list()[number-1]}')
                except IndexError:
                    print(f'\nIn record list no {number} number!\n')
            else:
                print('Pleas enter number!')
        elif menu_choice == 0:
            print('\nBye!')
            break


menu()
