# Print all non-contagious subsequences using recursion.
def get_subsequences(i,ds,arr,n):
    # BASE CASE
    # If index is equal to input array length print the data structure containing subsequence
    if i == n:
        print(ds,end="  ")
        return

    # Case-1: Take/Pick the particular index into the subsequence
    ds.append(arr[i])
    get_subsequences(i+1,ds,arr,n)
    ds.remove(arr[i])

    # Case-2: Not Take/Pick the particular index into the subsequence
    get_subsequences(i+1,ds,arr,n)


if __name__ == '__main__':
    a = [3,1,2]
    ds = []
    get_subsequences(0,ds,a,len(a))
    
# OUTPUT: [3, 1, 2]  [3, 1]  [3, 2]  [3]  [1, 2]  [1]  [2]  [] 
