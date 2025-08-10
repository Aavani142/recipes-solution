from collections import defaultdict, deque

def findAllRecipes(recipes, ingredients, supplies):

    ingredient_to_recipes = defaultdict(list)
    indegree = {recipe: 0 for recipe in recipes}  

    for recipe, ing_list in zip(recipes, ingredients):
        for ing in ing_list:
            ingredient_to_recipes[ing].append(recipe)
        indegree[recipe] = len(ing_list)

   
    queue = deque(supplies)
    result = []

    while queue:
        item = queue.popleft()
        
        for recipe in ingredient_to_recipes[item]:
            indegree[recipe] -= 1
            if indegree[recipe] == 0:  
                result.append(recipe)
                queue.append(recipe)

    return result



recipes = ["bread", "sandwich", "burger"]
ingredients = [["flour", "water"], ["bread", "ham"], ["bread", "meat", "lettuce"]]
supplies = ["flour", "water", "ham", "meat", "lettuce"]

print(findAllRecipes(recipes, ingredients, supplies))
# Output example: ['bread', 'sandwich', 'burger']

