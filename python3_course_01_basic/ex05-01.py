#列表

#insert() 将数据插入到列表的任何位置
courses=['Linux','Python','Vim','C++','PHP']
courses.insert(0,'Java')
print(courses)
courses.insert(1,'Ruby')
print(courses)

#count() 检查元素在列表中出现了多少次
print(courses.count('Vim'))

#remove() 移除任意指定值,出现多次只会被移除一个
courses.remove('Java')
print(courses)

#另外一种删除元素的方法是使用 del 关键字，这个关键字可以删除列表指定位置的元素
del courses[-1]
print(courses)#最后一个元素php被移除了

#reverse() 有序的列表可以进行反转
courses.reverse()
print(courses)

#extend()其中一个列表合并到另外一个列表的末尾位置，可以使用
new_courses = ['BigData', 'Cloud']
courses.extend(new_courses)
print(courses)

#sort() 给列表排序
#数字是按照大小进行排序，而字符串则会选择按照字母表的顺序进行排序
courses.sort()
print(courses)

#pop() 函数返回最后的一个元素
#pop() 在返回元素的同时也会删除这个元素
#pop(n)可以删除指定元素
print(courses.pop())
print(courses)
courses.pop(2)#删除第三个元素
print(courses)