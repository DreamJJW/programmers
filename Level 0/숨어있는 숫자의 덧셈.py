import re
my_string = input()
res = 0
nums_list = re.findall('\d+', my_string)
print(sum(int(i) for i in nums_list))
