def LinearSearchProduct(productlist,targetproduct):
  indices=[]
  for index,product in enumerate(productlist):
    if product==targetproduct:
      indices.append(index)
  return indices
products=["Shoes","Boot","Loafer","Shoes","Sandal","Shoes"]
target="Shoes"
target2="Apple"
result=LinearSearchProduct(products,target)
print(result)