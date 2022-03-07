
# # '''F change to C'''
# # f = float(input("Pleae input F: "))

# # c = (f - 32)/1.8

# # print('%f 华氏温度等于 %f摄氏度' % (f, c))

# '''Get the cycle circumference and area '''

# radius = float(input("Please input the cycle radius: "))

# circumference = 2 * 3.14 * radius

# area = 3.14 * radius * radius

# print ('circumference is %.1f' % circumference)
# print ('area is %.2f' % area)

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

