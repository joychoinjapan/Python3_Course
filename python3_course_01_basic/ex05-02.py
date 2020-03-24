#集合
#set（集合）是一个无序不重复元素的数据集，对比列表的区别首先是无序的，不可以使用索引进行顺序的访问，另外一个特点是不能够有重复的数据。
#需要注意空的集合不能够使用 {} 创建，只能使用 set 函数
courses=set()
print(type(courses))
courses={'Linux', 'C++', 'Vim', 'Linux'}
print(courses)#{'Linux', 'Vim', 'C++'} 多余的linux 被去除
#集合还可以直接由字符串与 set 函数进行创建，会将字符串拆散为不同的字符，并去除重复的字符：
nameset=set('shiyanlou.com')
print(nameset)

#集合操作
#判断集合中的元素的存在 in
print('Linux' in courses)
print('Python' in courses)
print('Python' not in courses)
