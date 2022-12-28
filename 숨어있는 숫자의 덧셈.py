import re
my_string = input()
res = 0
nums_list = re.findall('\d+', my_string)
for i in nums_list:
    res += int(i)
print(res)
