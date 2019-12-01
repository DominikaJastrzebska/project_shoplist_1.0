from pprint import pprint as pp
import requests
import string
import shoplist_v1_0 as sl
import shoplist_v1_1 as sl2

"""
Moduł tworzy listę zakupów na kilka literek oraz zapisuje ją do pliku
"""


def main():
    # letters = string.ascii_lowercase
    recipe_list_all_letters = []
    letters = 'az'
    for letter in letters:
        meals_a_json = sl.request_recipe(letter)
        recipe_list = sl.get_recipe_list(meals_a_json)
        for meals_dict in recipe_list:
            recipe_list_all_letters.append(meals_dict)
    print(recipe_list_all_letters)
    dict_of_meals = sl.get_recipe(recipe_list_all_letters)
    ingredients_list = sl.get_ingredients_list(dict_of_meals)
    ingredients_dictionary = sl.get_ingredients_dict(ingredients_list)
    sl2.export_to_csv(ingredients_dictionary)

    print(f'---------------------Nazwy przepisów:------------------------')
    sl.get_names_of_recipes(recipe_list_all_letters)


if __name__ == '__main__':
    main()
