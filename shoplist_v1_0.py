import json
from pprint import pprint as pp
import requests
import string

# letters = string.ascii_lowercase
# meals = []
# for letter in letters:
#     meals = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?f={letter}')
# with open('meals.txt', 'w') as f:
#     f.write(meals.text)


def get_letter():
    """
    funkcja jako argument przyjmuje literę, zwraca literę
    """
    letter = 'b'
    return letter


def request_recipe(letter):
    '''
    funkcja, jako argument przyjmuje literę
    litera jest dołączona do adresu url, w celu wykonania zapytania do api
    funkcja zwraca api w formacie json, przepisy na jedną literę
    '''
    url = f'https://www.themealdb.com/api/json/v1/1/search.php?f={letter}'
    meals = requests.get(url)
    meals_a_json = meals.json()
    return meals_a_json


def get_recipe_list(meals_a_json):
    recipe_list = meals_a_json['meals']
    return recipe_list


def get_names_of_recipes(recipe_list):
    '''
    :param meals_a_json: api z przepisami w formacje json
    : wyświetla nazwy przepisów na daną literkę
    '''
    for element in recipe_list:
        return element['strMeal']


def get_recipe(recipe_list):  # [{}, {}, {}]
    '''
    :param lista ze słownikami - poszczególnymi przepisami [{}, {}, {}]
    :return: słownik w którym klucz to nazwa przepisu, a wartość, to słownik z
    kluczem - skłdnikiem i wartością - miarą
    '''
    dict_of_meals = {}

    for recipe in recipe_list:
        ingredients_measure = []  # tworzymy pustą listę, do której będziemy zapisywać krotki (ingredients, measure)
        dict_of_meals[recipe['strMeal']] = ingredients_measure
        list_of_number_ingredients = get_ingredients_numbers(recipe)
        for i in list_of_number_ingredients:  # nie wiem jak to zrobic, zeby tutaj wcisnac ta liste, ktora mi obrabia ten zakres?
            if recipe[f'strIngredient{i}'] is not None:
                ingredients_measure.append((recipe[f'strIngredient{i}'], recipe[f'strMeasure{i}']))
            # ingredients_measure.append((recipe[f'strIngredient{i}'], recipe[f'strMeasure{i}']))

        dict_of_meals[recipe['strMeal']] = dict(ingredients_measure)
    return dict_of_meals


# tworzymy pusty slownik, do slownika wpisujemy jako klucz nzwe przepisu np. 'Apple Frangipan Tart',
# a jako wartości - slownik w którym klucz to nazwa skladnika, np. 'digestive biscuits',
# a wartosc to ilosc tego skladnika '175g/6oz', struktura ta posłuży do stworzenia listy zakupów

def get_ingredients_list(dict_of_meals):
    '''
    :param dict_of_meals: słownik w którym klucz to nazwa przepisu, a wartość, to słownik z
    kluczem - skłdnikiem i wartością - miarą
    :return: Lista słowników, w których klucz to składnik, a wartość to ilość z poszczególnych przepisów
    '''
    ingredients_list = []
    for key, value in dict_of_meals.items():
        ingredients_list.append(value)
    return ingredients_list


def get_ingredients_dict(ingredients_list):
    ingredients_dictionary = {}
    for element in ingredients_list:
        for ingredient, measure in element.items():
            if ingredient not in ingredients_dictionary.keys():
                ingredients_dictionary[ingredient] = measure
            else:
                ingredients_dictionary[ingredient] = ingredients_dictionary[ingredient] + measure
    return ingredients_dictionary


def get_ingredients_numbers(recipe_dict):  # {stringred1: jjd, stringred2: fjf, measure1: 100g, measure2: 30g}
    """
    funckja zwraca liste liczb, ktore są przypisane do skladnika, np.
    ['strIngredient1', 'strIngredient10', 'strIngredient11'] ==> [1, 10, 11]
    jako argument przyjmuje pojedyńczy przepis - skownik z listy recipe_list pojedynczym przepisem
    """
    list_of_numbers_ingredients = []
    keys_ingredients_list = []
    for keys in recipe_dict.keys():
        if 'strIngredient' in keys:
            keys_ingredients_list.append(keys)
    for ingredients in keys_ingredients_list:
        only_number = int(ingredients.strip('strIngredient'))
        list_of_numbers_ingredients.append(only_number)

    return list_of_numbers_ingredients


def make_shopping_list(ingredients_dictionary):
    for ingredient, measure in ingredients_dictionary.items():
        print(ingredient, '-', measure)
    return ingredient, measure


def main():
    letter = get_letter()
    meals_a_json = request_recipe(letter)

    print(f'---------------Api przepisy na literkę {letter}------------------')
    pp(meals_a_json)
    print()

    recipe_list = get_recipe_list(meals_a_json)
    print(f'-------------Lista przepisów na literkę {letter} (nazwa, składniki, ilości, instrukcja wykonania)-------------')
    print(recipe_list)
    print()

    print(f'---------------------Nazwy przepisów na literkę {letter}------------------------')
    names_of_reciepes = get_names_of_recipes(recipe_list)
    print(names_of_reciepes)
    print()

    print(f'---------Słownik przepisów na literkę {letter}, gdzie klucz to nazwa przepisu '
          f'a wartość to słownik w którym kluczami są skłądniki a wartościami ilości i miary------')
    dict_of_meals = get_recipe(recipe_list)
    pp(dict_of_meals)

    print('----Lista słowników, w których klucz to składnik, a wartość to ilość z poszczególnych '
          'przepisów------------')
    ingredients_list = get_ingredients_list(dict_of_meals)
    print(ingredients_list)
    print()

    print('-------Lista słowników dla poszczególnych przepisów klucz - składnik, wartość - miara-------')
    ingredients_dictionary = get_ingredients_dict(ingredients_list)
    print(ingredients_dictionary)

    print('Lista zakupów: ')
    make_shopping_list(ingredients_dictionary)


if __name__ == '__main__':
    main()