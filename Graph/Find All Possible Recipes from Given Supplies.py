from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook = {s:True for s in supplies}
        ing_index = {r:i for i,r in enumerate(recipes)}

        def dfs(r):
            if r in can_cook:
                return can_cook[r]

            if r not in ing_index:
                return False
            
            can_cook[r] = False
            
            for neg in ingredients[ing_index[r]]:
                if not dfs(neg):
                    return False
            
            can_cook[r] = True
            return can_cook[r]
        return [r for r in recipes if dfs(r)]
    

sol=Solution()

recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]

print(sol.findAllRecipes(recipes,ingredients,supplies))
