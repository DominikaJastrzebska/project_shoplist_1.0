import shoplist_v1_0 as sl  # dlaczego nie mozna shoplist_1.0?


def export_to_csv(ingredients_dictionary):
    for ingredient, measure in ingredients_dictionary.items():
        if ingredient is not None and measure is not None:
            filename = 'shopping_list.csv'
            with open(filename, 'a') as f:
                f.write('\n' + ingredient + ', ' + measure)


def main():
    letter = sl.get_letter()
    meals_a_json = sl.request_recipe(letter)
    recipe_list = sl.get_recipe_list(meals_a_json)
    dict_of_meals = sl.get_recipe(recipe_list)
    ingredients_list = sl.get_ingredients_list(dict_of_meals)
    ingredients_dictionary = sl.get_ingredients_dict(ingredients_list)
    export_to_csv(ingredients_dictionary)


if __name__ == '__main__':
    main()