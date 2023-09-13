def sort(arr,n):
    if(0<=n<=1):
        return arr
    sorted_arr = sort(arr[:n-1],n-1)
    #We could also insert item using a for loop which is much simpler but just to practice here it is being done through recursion
    res = insert_item_in_sorted_arr(sorted_arr[:],arr[n-1],n-1)
    return res

def insert_item_in_sorted_arr(arr,item,n):
    if(n==0 or arr[n-1]<=item):
        arr.append(item)
        return arr
    last_value = arr.pop()
    res = insert_item_in_sorted_arr(arr[:n-1],item,n-1)
    res.append(last_value)
    return res

print(sort([5,4,10,3,2,1],6))
    