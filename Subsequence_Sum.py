def subsequence_sums(arr, s):
    a = 0
    n = len(arr)
    sequence = {}
    count = 0
    first_index = 0
    last_index = 0
    while first_index < n:
        a = a + arr[last_index] 
        if a == s:
            sequence[count] = arr[first_index : last_index + 1]
            count = count + 1
            if last_index == n-1:
                first_index = first_index + 1
                last_index = first_index
                a = 0
            else:
                last_index = last_index + 1
        else:
            if last_index == n-1:
                first_index = first_index + 1
                last_index = first_index	
                a = 0
            else:
                last_index = last_index + 1		
    return (sequence,count)


ans = {}
(ans,total) = subsequence_sums([1, 2, 3, -3, -2, -1],0)
print("->",total)
counter = 0
for i in sorted(ans.keys()):
    if counter != total - 1:
         print(ans[i], end=", ")
         counter += 1
    else:
        print(ans[i])
 	

#n = int(input("Enter the Size of the array: "))
#s = int(input("Enter the sum of sub-sequence: "))
#print("Enter the Elements of the Array..")
#for i in range(n):
#	a = int(input())
#	arr.append(a)
#print()
#(ans, total) = subsequence_sums([1, 5, -2, 4, 0, -7, -3, 6],4)
#print("->",total)
#for i in sorted(ans.keys()):
#	print(ans[i], end=", ")
		
		


 
