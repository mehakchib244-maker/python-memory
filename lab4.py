#rotate array clockwise by one position
arr = [12, 34, 56, 78, 90]
last = arr.pop()
arr.insert(0,last)
print("rotate array is:", arr)
print("\n")
#Q2 SUM of subarray elements
#current_sum= and max_sum=
arr = [2,3,-8,7,-1,2,3]#firstly we assume first element is max sum and current sum
current_sum= arr[0]
max_sum= arr[0]
for i in range(1,len(arr)):#1 se start hoga kyuki current sum me pehla element already hai
    current_sum = max(arr[i], current_sum + arr[i]) #isme cuurrent sum me ya to current element ayega ya current sum + current element ayega jo bada hoga
max_sum = max(max_sum, current_sum) #isme max sum me ya to pehla max sum ayega ya current sum ayega jo bada hoga
print("the maximum subarray sum is:", max_sum)#uper dono ko compare karke jo bada hoga wo print hoga
print("\n")
