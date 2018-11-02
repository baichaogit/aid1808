# 正则表达式

## 动机：
   1.文本处理已经成为计算机常见的工作之一  
   2.对文本内容的搜索，定位，提取  
   3.为了方便的解决上述问题，产生了正则表达式技术  

## 定义：
  即文本的高级匹配模式，提供搜索，替换等功能。其本质是**一系列由特殊符号组成的字符串**，
  这个字符串就是正则表达式(简称re)。 

## 目标：
  1. 熟练掌握正则表达式符号  
  2. 读懂常见的正则表达式，编写基本的搜索提取功能正则  
  3. 能够熟练使用re模块操作正则表达式  

## 正则表达式的特点
- 方便文本处理
- 支持的语言众多 
- 使用灵活变化  
  


------------------------------------------------
------------------------------------------------


## python　--> re模块

`re.findall(pattern, string)`  
功能：　提取所有的正则匹配内容  
参数：　pattern　正则表达式  
　　　　string　目标字符串  
返回值：　列表，所有提取到的内容


## 元字符的使用
------
### 1.普通字符
元字符：　a　B　c  
匹配规则：　每个字符匹配对应的字符
```py
  In [4]: re.findall('ab','abchdgf')
  Out[4]: ['ab']
```  
------
### 2.或
元字符 :　| 
```py
  In [5]: re.findall('ab|ef','abchdgefgg')
  Out[5]: ['ab', 'ef']

  In [6]: re.findall('ab|bc','abcgggg')
  Out[6]: ['ab'] #重叠的部分，取不出

  In [7]: re.findall('ab | ef','abchdgefgg')
  Out[7]: []  #空格也会被识别，不能随意加空格
```

--------------
### 3.匹配单个字符
元字符：　.  
匹配规则：　匹配除换行外  
> In [8]: re.findall('f.o','foo fao')  
Out[8]: ['foo', 'fao']    

> In [9]: re.findall('f..d','food fao')  
Out[9]: ['food']

------------------
### 4.匹配字符串开始位置
元字符：　^  
匹配规则：匹配目标字符串的开始位置  
> In [13]: re.findall('^Hello','Hello Jay')  
Out[13]: ['Hello']

>In [14]: re.findall('^Hello','Jay Hello')  
Out[14]: [] 　　#　Hello在尾部，匹配不到

-----------------
### 5.匹配字符串结束位置
元字符：　$  
匹配规则：匹配目标字符串的结束位置  
> In [16]: re.findall('Hello$','Jay Hello')  
Out[16]: ['Hello']

> In [17]: re.findall('Hello$','Jay Hello haha')  
Out[17]: []

---------
### 6.匹配重复
元字符串：　*  
匹配规则：　匹配前面的字符重复 0 次或者多次  
fo*　重复0次，>　f  
fo*　重复多次，>　fooo  
> In [18]: re.findall('fo*','fooofaaaafoaaafoo')  
Out[18]: ['fooo', 'f', 'fo', 'foo']

-------------
### 7.匹配重复
元字符：　+  
匹配规则：　匹配前面的字符重复１次或者多次  
fo*　重复１次，>　fo  
fo*　重复多次，>　fooo  
> In [19]: re.findall('fo+','fooofaaaafoaaafoo')  
Out[19]: ['fooo', 'fo', 'foo']

----------
### 8.匹配重复
元字符：　?  
匹配规则：　匹配前面的字符出现 0 次或 1 次  
> In [22]: re.findall('fo?','fooooooaaafdddfo')  
Out[22]: ['fo', 'f', 'fo']

-----------
### 9.匹配重复
元字符：　{n}  
匹配规则：　匹配前一个字符重复指定字数  
fo{3}　> fooo  
> In [24]: re.findall('fo{3}','fooooooaaafdddfo')
Out[24]: ['fooo']

----------
### 10.匹配重复
元字符：　{m,n}  
匹配规则：　匹配前面的字符出现　m--n　次  
fo{2,4}　>　foo　　fooo　　foooo  
> In [25]: re.findall('fo{2,3}','fooooooaaafoodddfo')  
Out[25]: ['fooo', 'foo']

------------
### 11.匹配字符集
字符集：　[字符集]  
匹配规则：　匹配字符集中的任意【一个】(不能连在一起)字符  
[abc123]　> 可匹配a　b　c　1　2　3  
[a-zA-Z]　> 可匹配从a到z,和A到Z之间的任意一个字符  
> 匹配句子中以大写字母开头的单词  
In [26]: re.findall('[A-Z]+[a-z]*','This is my Jay')  
Out[26]: ['This', 'Jay']

-------------
### 12.匹配字符集
字符集：　[^...]  
匹配规则：　匹配除了字符集中的任意一个字符一次或多次  
[^abc]　> 除了a/ b /c外的任意字符都可匹配  
> In [33]: re.findall('[^ ]+','This in my Jay') #除空格外的...  
Out[33]: ['This', 'in', 'my', 'Jay']  
In [34]: re.findall('[^0-9]+','10+9-1=18') #除数字外的...  
Out[34]: ['+', '-', '=']

-----------------
### 13.匹配任意(非)数字
元字符：　\d 　　\D   
匹配规则：　\d 匹配任意数字字符，[0-9]  
　　　　　　\D 匹配任意非数字字符，[^0-9]  
> In [35]: re.findall('1[\d]{10}','18872075623 110112') #匹配出1开头的11位电话号码..  
Out[35]: ['18872075623']

--------------------
### 14.匹配任意(非)普通字符
元字符：　\w 　　\W  
匹配规则：　\w 匹配任意普通字符：　[_0-9a-zA-Z]也能匹配汉字  
　　　　　　\W 匹配任意非普通字符  
> In [36]: re.findall('[\w]+','my\$zui-#aide--jay')  
Out[36]: ['my', 'zui', 'aide', 'jay']  
In [37]: re.findall('[\W]+','my\$zui-#aide--jay')  
Out[37]: ['$', '-#', '--']


---------------------
### 15.匹配任意（非）空字符
元字符 ： \s  匹配任意空字符　[\r　\t　\n　\v　\f]  
　　　　 \S  匹配任意非空字符  
> In [38]: re.findall("\w+\s+\w+","hello   world")  
Out[38]: ['hello   world']  
In [39]: re.findall("\S+","hello this is tom")  
Out[39]: ['hello', 'this', 'is', 'tom']

------------------
### 16.匹配字符串位置
元字符 ：　\A　\Z  
匹配规则：　\A 匹配字符串开头位置　,同　^  
　　　　　　\Z 匹配字符串结尾位置　，同　$   

----------
### *绝对匹配 ：   
当正则表达式前有^(或\A)，最后有$(或\Z)时，那么这个正则表达式一定是要匹配目标字符串的全部内容。否则就什么都不匹配。  
> In [38]: re.findall("\A\d+\Z","123445")  
Out[38]: ['123445']  
>In [39]: re.findall("\A\d+\Z","123445 ")  
Out[39]: []

-------------------
### 17.匹配（非）单词边界
元字符 ： \b　　\B  
匹配规则 ： \b 匹配单词边界位置 （普通字符和非普通字符交界认为是单词边界）   
　　　　　　\B 匹配非单词边界位置  
> In [40]: re.findall(r"\bis\b","this is Jay")  
Out[40]: ['is']


----------------------------------
## 元字符总结

匹配单个字符： .　[...]　[^...]　\d　\D　\w　\W　　\s　\S　　　  
匹配重复：　*　+　?　{n}　{m,n}  
匹配位置：　^　$　\A　\Z　\b　\B  
其他 ：　|　()　\  


----------
## 正则表达式转义

正则中的特殊符号：`　.　*　+　?　^　$　[]　{}　()　|　\  `  
在正则表达式中，如果匹配特殊字符需要加 \ 作为转义  
> eg.: 匹配`.`　　需要使用`\.`  

python字符串　　　正则　　　目标字符串  
`'\\$\\d+'　　　\$\d+　　　$10`

raw字串 ： 不对字符串内容进行转义处理  
`'\\$\\d+'　　　==>　　r'\$\d+'　`

-------------  
## 贪婪与非贪婪

- 贪婪模式：  
正则表达式的重复匹配默认总是尽可能的向后匹配更多的内容。  
`*　+　?　{m,n}`

- 非贪婪（懒惰）模式 ：  
尽可能少地匹配重复内容。

贪婪 -->> 非贪婪  *？  +？  ??  {m,n}?　
> In [41]: re.findall(r"ab+?","abbbbbbbb")  
Out[41]: ['ab']

> In [42]: re.findall(r"ab??","abbbbbbbb")  
Out[42]: ['a']　　


------
## 正则表达式的分组

使用(  )为正则表达式建立内部分组(子组)，子组为正则表达式的一部分，可以看做一个内部整体。  
有子组的正则表达式仍然是整体去匹配内容，子组需要在整体能够匹配到内容的前提下发挥作用。  

### 子组的作用：
1.作为内部整体可以改变某些元字符的行为。  
> In [3]: re.search(r"(ab)+\d+","ababab1234").group( )  
Out[3]: 'ababab1234'  
> In [4]: re.search(r"\w+@\w+\.cn|com","abc@123.com").group( )  
Out[4]: 'com'  
In [5]: re.search(r"\w+@\w+\.(cn|com)","abc@123.com").group( )  
Out[5]: 'abc@123.com'  

2.子组在匹配到内容的情况下，可以单独提取出匹配内容。  
> In [7]: `re.search(r"(https|http|ftp)://\S+","https://www.baidu.com").group(1)`  
Out[7]: `'https'`

### 子组使用的注意事项：
1. 一个正则表达式中可以有多个子组
2. 子组一般由外到内，由左到右称之为第一，第二，第三...子组
3. 子组不能重叠或者嵌套过多

### 捕获组和非捕获组
格式：　`(?P<name>pattern)`  
**给子组起名字，方便group方法使用**
> `In [8]: re.search(r"(?P<dog>ab)cdef",'abcdefghi').group('dog')`  

Out[8]: 'ab'　#给子组命名dog，利用名字获取子组内容


### 正则表达式的设计原则：

1. 正确性：能正确匹配到目标内容
2. 排他性：除了要匹配的内容，尽可能不会匹配与到其他内容
3. 全面型：尽可能对目标字串各自情况进行考虑，做到不遗漏


-----------------------------------------------------------  
## re 模块

`regex = compile(pattern, flags = 0)`  
- 功能 ： 生成正则表达式对象  
- 参数 ： pattern  正则表达式  
　　　 flags  功能标志位，丰富正则表达式的匹配功能  
- 返回值 : 返回正则表达式对象


`re.findall(pattern, string, flags = 0)`  
- 功能 ：从目标字符串查找正则匹配内容  
- 参数 ：pattern  正则表达式  
　　　string  目标字符串  
　　　flags  标志位  
- 返回值 ： 返回匹配到的内容(如果正则有子组,则只返回子组对应内容!!)


`regex.findall(string, pos, endpos)`
- 功能 ：从目标字符串查找所有正则匹配内容
- 参数 ：string　目标字符串  
　　　　pos　截取目标字符串的起始位置  
　　　　endpos  截取目标字符串的终止位置
- 返回值 ：返回匹配到的内容列表,如果正则有子组则只返回子组中的内容  
> @import "./code/regex.py" 
```py
import re 

pattern = r"(\w+):(\d+)"
s = "zhang:1994 li:1993"

#re直接调用
l = re.findall(pattern,s,flags = 0)
print(l)  # [('zhang', '1994'), ('li', '1993')]

#compile对象调用
regex = re.compile(pattern,flags = 0)
l = regex.findall(s,pos=0,endpos=12)
print(l)  # [('zhang', '1994')]
```


`re.split(pattern, string, flags)`
- 功能 ：从目标字符串查找所有正则匹配内容
- 参数 ：pattern 　正则表达式  
　　　　string 　目标字符串  
　　　　flags　标志位  
- 返回值 ：返回匹配到的内容列表，如果正则有子组则只返回子组中的内容  
> 例如：./code/re_split.py
```py
#示意re模块的split的用法
import re

l = re.split(r'\s+','hello world nihao beijing',flags = 0)
print(l)  #['hello', 'world', 'nihao', 'beijing']
```


`re.sub(pattern, replaceStr, string, max, flags)`
- 功能：使用字符串替换正则匹配的内容
- 参数：pattern　正则表达式  
　　　　replaceStr　替换的字符串  
　　　　string　目标字符串  
　　　　max　最多替换几处,默认全部替换  
　　　　flags　标志位 
- 返回值：返回替换后的字符串
> 例如：./code/re_sub.py


`re.subn(pattern, replaceStr, string, max, flags)`
- 功能：使用字符串替换正则匹配的内容
- 参数：pattern:正则表达式  
　　　replaceStr：替换的字符串  
　　　string：目标字符串  
　　　max：最多替换几处,默认全部替换  
　　　flags 标志位 
- 返回值：返回替换后的字符串　和　替换了几处
> 例如：/code/re_sub.py
```py
#示意re模块的sub / sunb的用法
import re

s = re.sub(r'\s+','**','hello world nihao beijing')
print(s)  # hello**world**nihao**beijing

s = re.sub(r'\s+','**','hello world nihao beijing',2)
print(s)  # hello**world**nihao beijing

s = re.subn(r'\s+','**','hello world nihao beijing',2)
print(s)  # ('hello**world**nihao beijing', 2)
```


`re.finditer(pattern, string)`
- 功能：　使用正则表达式匹配目标字符串
- 参数：　pattern 正则表达式  
　　　　string 目标字符串
- 返回值：　返回一个迭代对象，迭代到的内容是一个match对象


`fullmatch(pattern,string,flags)`
- 功能：　绝对匹配目标字符串
- 参数：　pattern 正则  
　　　　string  目标字符串
- 返回值：match对象
> 例：@import "./code/regex1.py"


`match(pattern, string, flags)`
- 功能： 从开头位置匹配目标字符串
- 参数： pattern 正则  
　　　　string  目标字符串  
　　　　flags
- 返回值：返回匹配到的match对象，如果没匹配成功返回None
> 例：@import "./code/regex1.py"


`search(pattern, string, flags)`
- 功能： 正则表达式匹配目标字符串，只匹配第一处!!
- 参数： pattern,　string,　flags
- 返回值：返回匹配到的match对象,如果没匹配成功返回None　　
> 例：@import "./code/regex1.py"
```py
import re 

pattern = r'\d+'
s = "2008年事情多，08奥运，512地震"

it = re.finditer(pattern,s) 

# print(dir(next(it)))

for i in it:
    #ｍａｔｃｈ对象group函数获取匹配内容
    print(i.group()) # 2008  08   512

try:
    obj = re.fullmatch(r'\w+','hello1973')
    print(obj.group())  # hello1973
except AttributeError as e:
    print(e)

obj = re.match(r'[A-Z]\w+',"Hello World")
print(obj.group())  # Hello

obj = re.search(r'\d+',s)
print(obj.group())  # 2008
```


### regex 对象属性：
```py
pattern:
In [9]: regex = re.compile(r'abcdef')
In [10]: regex.pattern
Out[10]: 'abcdef'
```

    flags:　表示标志位常亮值
    group:　表示正则有多少个子组
    groupindex:　生成(捕获组名和对应第几组)的键值对,构成的字典 #

---------------------
## 作业：
1. 熟记正则表达式元字符
2. 找一个文档，使用正则表达式：
   1. 匹配其中的大写子母开头的单词
   2. 匹配其中所有的数字(整数，浮点数，负数，百分数，分数...)
3. 复习：regex对象调用函数
