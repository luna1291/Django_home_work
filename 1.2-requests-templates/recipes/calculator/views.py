from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render
from requests import request

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipes(request):
    menu = request.GET('recipe') #не могу понять как составить запрос к выборке по ключу массива DATA                   
    servings = int(request.GET.get("servings", 1))
    recipe = DATA.get(menu)
    for ingredient, amount in recipe.items():                         
        return (f'{ingredient} : {round(float(amount) * servings, 2)}')
    
    context = {
        "recipe" : recipe
    }
    return render(request, 'calculator/index.html', context)

# for i in range(0, len(DATA)): неудачная попытка составить запрос по меню http://127.0.0.1:8000/omlet/
#     menu = list(DATA.keys())
#     print (menu)

    
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
