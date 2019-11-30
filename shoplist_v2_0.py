from pprint import pprint as pp
import requests
import string
import shoplist_v1_0 as sl
import shoplist_v1_1 as sl2


def main():
    letters = string.ascii_lowercase
    for letter in letters:
        meals_a_json = sl.request_recipe(letter)
        recipe_list = sl.get_recipe_list(meals_a_json)
        dict_of_meals = sl.get_recipe(recipe_list)
        ingredients_list = sl.get_ingredients_list(dict_of_meals)
        ingredients_dictionary = sl.get_ingredients_dict(ingredients_list)
        sl2.export_to_csv(ingredients_dictionary)


if __name__ == '__main__':
    main()
