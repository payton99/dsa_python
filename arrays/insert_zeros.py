arr = [1,0,2,3,0,4,5,0]


new_arr = []
count = 0
for idx, num in enumerate(arr):
    if num == 0:
        new_arr.append(num)
        new_arr.append(0)
    else:
        new_arr.append(num)  

while len(new_arr) > len(arr):
    new_arr.pop()


print(new_arr)
