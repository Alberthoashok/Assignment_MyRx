
def sort_balls(arr):
    mini,mid,maxi = 0,0,len(arr)-1

    while mid <= maxi:
        if arr[mid] == "B":
            arr[mini], arr[mid] = arr[mid], arr[mini]
            mini += 1
            mid += 1
        elif arr[mid] == "G":
            mid += 1
        else:
            arr[mid],arr[maxi] = arr[maxi],arr[mid]
            maxi -= 1
    return arr



input_balls = ["R","G","B","R","R","G","B","G"]
output = sort_balls(input_balls)
print(output)