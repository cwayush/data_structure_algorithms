class ProductOfNumbers:

    def __init__(self):  
        self.prefix_products = [1]  # Start with a prefix product of 1  
        self.count = 0   

    def add(self, num: int) -> None:  
        if num == 0:  
            # Reset on zero, since the product will be zero if we include it  
            self.prefix_products = [1]  # Reset prefix products  
            self.count = 0  
        else:  
            last_product = self.prefix_products[-1]  # Get last product  
            new_product = last_product * num    
            self.prefix_products.append(new_product)  # Add new product to the prefix list  
            self.count += 1  

    def getProduct(self, k: int) -> int:  
        if k > self.count:  
            return 0 
        
        return self.prefix_products[-1] // self.prefix_products[-k - 1]  
    
# Approach-1 (Preffix Sum)
# T.C : O(1)
# S.C : O(n) 

sol = ProductOfNumbers()

operations = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
values = [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

output = []
for op, val in zip(operations, values):
    if op == "add":
        sol.add(val[0])
        output.append(None)
    elif op == "getProduct":
        output.append(sol.getProduct(val[0]))
    else:
        output.append(None) 

print(output)