 i fix rahe gya jaie arr[0] aur j move hote rahe arr[0]+arr[1], arr[0]+arr[1]+arr[2]...
#given a number and an array of integers.find the smallest subarray with sum greater than the given value . if no subarray exist return 0.


arr = [1,10,5]
x= 11
def smallest_subarray(arr,x):
    n = len(arr)
    min_length = n + 1 #worst case le rahe max 3,3+1=4 elements not found aur pure array tranverse of worst case se phle #yeh hai he nhi kyuki valid he nhi eg: min_lenght =min(4,3)=3 update ho gya min_length taki further compare kare aur min value de
    for i in range(n): #from where to start subarray
        current_sum=0 #for new i sum reset krenge
        for j in range(i,n):#how far should we go it keep adding number till end and move forward
            current_sum += arr[j] #add current element to current sum eg: i=0, j=0, current sum=1; j=1, current sum=arr[0]+arr[1]=11
            if current_sum > x: 
                length = j - i + 1 #length of subarray j-i means gap b/w i and j +1 issi liye kyuki index 0 se start hota hai
                min_length = min(min_length, length) # minfunction ka kam compare min length with current length and store the minimum one
                break #we found the subarray no need to check further
    return min_length if min_length != n + 1 else 0 #if min_length is updated return it else return 0 
    # <or> if min_length == n+1:  max possible length of subarray =n ,n+1 not possible technically show not found
    #     return 0 
    #     return min_length 
result = smallest_subarray(arr, x) #function call and store result in variable
print("the smallest subarray length greater than ",x,"is:",result)
print("\n")

