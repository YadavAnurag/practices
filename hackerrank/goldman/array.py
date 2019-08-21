def findSpecialProduct(inputArray):
    pre, post = [1],[1]
    for i in range(len(inputArray)):
        pre.append(pre[i]*inputArray[i])
        post.insert(0, post[-(i+1)]*inputArray[-(i+1)])


    result = []
    for i in range(1,len(pre)):
        result.append(pre[i-1]*post[i])
    return result
print(findSpecialProduct([1,2,3,4,5]))