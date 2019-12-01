"""Moduł pobiera od użytkownika nazwy przepisów oraz zwraca pierwsze literki nazw przepisów"""


def get_recipe_from_user():
    list_of_words = []
    while True:
        answer = input('Z jakich przepisów chcesz zrobić listę zakupów? '
                       'Aby zakończyć wpisywanie, naciśnij q ')
        if answer != 'q':
            list_of_words.append(answer)
        elif answer.lower() == 'q':
            break
    return list_of_words


def get_first_letters_from_recipes(list_of_recipes):
    first_letters = ''
    for element in list_of_recipes:
        first_letters += element[0]
    return first_letters


def main():
    list_of_words = get_recipe_from_user()
    print('Lista przepisów, z których użytkownik chce zrobić listę zakupów')
    print(list_of_words)
    print()
    print('Zbitka pierwszych liter przepisów')
    print(get_first_letters_from_recipes(list_of_words))


if __name__ == '__main__':
    main()

