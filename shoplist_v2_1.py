import shoplist_v1_0 as sl
import get_first_letters as gfl
import shoplist_v1_1 as sl2

"""
Moduł tworzy listę zakupów z przepisów podanych przez użytkownika
"""


def main():
    recipe_list_all_letters = []
    list_of_words = gfl.get_recipe_from_user()
    letters = gfl.get_first_letters_from_recipes(list_of_words)
    for letter in letters:
        meals_a_json = sl.request_recipe(letter)
        recipe_list = sl.get_recipe_list(meals_a_json)
        for meals_dict in recipe_list:
            if meals_dict['strMeal'] in list_of_words:
                recipe_list_all_letters.append(meals_dict)
    print(recipe_list_all_letters)
    dict_of_meals = sl.get_recipe(recipe_list_all_letters)
    ingredients_list = sl.get_ingredients_list(dict_of_meals)
    ingredients_dictionary = sl.get_ingredients_dict(ingredients_list)
    sl2.export_to_csv(ingredients_dictionary)

    print(f'---------------------Nazwy przepisów:------------------------')
    sl.get_names_of_recipes(recipe_list_all_letters)

    print('-------------------Lista zakupów-------------------------')
    sl.make_shopping_list(ingredients_dictionary)


if __name__ == '__main__':
    main()
