
  # 2.找一个文档，使用正则表达式：
  #   １匹配其中的大写子母开头的单词
  #   ２匹配其中所有的数字123 1.23 -1  -1.23  45%  1/2

s = "This is my Idol:Jay. 123##ddd 12.3 sfd()He is GOOD!,3##ddd 12.3 sfd()dsfs51, /wegd1/2dfgf.,54x51,/, wegd1/2dfgf,\
     54xzHahas, 12%121safa -15as YES !w/cx  -12.4"    
import re
p1 = r'\b[A-Z]\S*' #匹配大写开头的单词
l1 = re.findall(p1, s)    
print(l1) 

p2 = r"-?\d+\.?/?\d*%?"  #匹配各种数字
l2 = re.findall(p2, s)
print(l2)



