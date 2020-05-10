# 1．将下列值通过“除以二”转化为二进制。写出余数的栈。 
# a) 17 
# b) 45 
# c) 96 

# from pythonds.basic.stack import Stack

# def divideBy2(decNumber):
#     remstack = Stack()

#     while decNumber > 0:
#         rem = decNumber % 2
#         remstack.push(rem)
#         decNumber = decNumber // 2

#     binString = ""
#     while not remstack.isEmpty():
#         binString = binString + str(remstack.pop())

#     return binString
# print(divideBy2(45))

# 2．将下列中缀表达式转化为前缀表达式（使用全括号的方法）： 
# a) (A+B)*(C+D)*(E+F)   前缀((A+B)*(C+D)*(E+F))  **(+(AB)+(CD)+(EF))  **+AB+CD+EF
# b) A+((B+C)*(D+E)) 
# c) A*B*C*D+E+F 

#判断运算符的优先级
# def opOrder(op1,op2):
#     order_dic = {'*':4,'$':5,'/':4,'+':3,'-':3}
#     if op1 == '(' or op2 == '(':
#         return False
#     elif op2 == ')':
#         return True
#     else:
#         if order_dic[op1] < order_dic[op2]:
#             return False
#         else:
#             return True

# def infix2prefix(string):
#     prefix = ''
#     stack = []
#     string_tmp = ''
#     for s in string[::-1]:
#         if s == '(':
#             string_tmp += ')'
#         elif s == ')':
#             string_tmp += '('
#         else:
#             string_tmp += s
#     for s in string_tmp:
#         if s.isalpha():
#             prefix = s + prefix
#         else:
#             while len(stack)  and opOrder(stack[-1],s):
#                 op = stack.pop()
#                 prefix = op + prefix
#             if len(stack) == 0 or s != ')':
#                 stack.append(s)
#             else:
#                 stack.pop()
#     if len(stack):
#         prefix = ''.join(stack) + prefix
#     return prefix

# if __name__ == '__main__':
#     for string in ['(A+B)*(C+D)*(E+F)','A+((B+C)*(D+E))','A*B*C*D+E+F']:
#         print(string,'==>',infix2prefix(string)) 

# 3．将上述的中缀表达式转化为后缀表达式（使用全括号的方法）。 
# def priority(z):
#     if z in ['×', '*', '/']:
#         return 2
#     elif z in ['+', '-']:
#         return 1


# def in2post(expr):
#     """ :param expr: 前缀表达式
#         :return: 后缀表达式

#         Example：
#             "1+((2+3)×4)-5"
#             "1 2 3 + 4 × + 5 -"
#     """
#     stack = []  # 存储栈
#     post = []  # 后缀表达式存储
#     for z in expr:
#         if z not in ['×', '*', '/', '+', '-', '(', ')']:  # 字符直接输出
#             post.append(z)
#             print(1, post)
#         else:
#             if z != ')' and (not stack or z == '(' or stack[-1] == '('
#                              or priority(z) > priority(stack[-1])):  # stack 不空；栈顶为（；优先级大于
#                 stack.append(z)     # 运算符入栈

#             elif z == ')':  # 右括号出栈
#                 while True:
#                     x = stack.pop()
#                     if x != '(':
#                         post.append(x)
#                         print(2, post)
#                     else:
#                         break

#             else:   # 比较运算符优先级，看是否入栈出栈
#                 while True:
#                     if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
#                         post.append(stack.pop())
#                         print(3, post)
#                     else:
#                         stack.append(z)
#                         break
#     while stack:    # 还未出栈的运算符，需要加到表达式末尾
#         post.append(stack.pop())
#     return post

# if __name__ == '__main__':
#     s = "1+((2+3)×4)-5"
#     post = in2post(s)
#     print('后缀表达式： ',post)


# 4．采用直接的转化算法将上述的中缀表达式转化为后缀表达式。写出转化时栈的实时变化。 



# 5．计算下列后缀表达式的值。写出当每个操作数和操作符被处理时栈的实时变化。 
# a) 2 3 * 4 + 
# b) 1 2 + 3 + 4 + 5 + 
# c) 1 2 3 4 5 * + * + 
# 后缀表达式求值
from pythonds.basic.stack import Stack
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()  # 操作数2
            operand1 = operandStack.pop()  # 操作数1
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))



# 6．队列（Queue）的一种替换实现是使用一个列表使队列的尾在列表的末端。这样的替换操作会对其大 O 数量级产生什么样的影响？ 



# 7．在链表中，使用 add 方法时执行顺序相反的结果是什么？参考结果是什么？ 可能会什么样的问题？ 



# 8．解释当数据项在最后一个节点时链表的 remove 方法如何实现。 


# 9．解释当数据项是链表中唯一一个节点时链表的 remove 功能如何实现。 


# 3.10.编程练习 
# 1．修改中缀表达式转为后缀表达式的算法使之能处理错误输入。 


# 2．修改后缀表达式求值的算法使之能处理错误输入。 


# 3．实现一个结合了中缀到后缀的转化法和后缀的求值算法的直接求中缀表达式值的方法。你的 
# 求值法应该从左至右处理中缀表达式中的符号，并且使用两个栈来完成求值，一个存储操作数，一 
# 个存储操作符。 



# 4．将上一题的中缀求值法转化为一个计算器。


# 5．实现一个 Queue，使用一个 list 使 Queue 的尾部在 list 的末端。 


# 6．设计并实现一个实验，对以上两种 Queue 进行基准比较。你从这个实验中学到了什么？ 


# 7．实现一个队列并使它的 enqueue 和 dequeue 方法平均时间复杂度都是 O(1)。也就是说，在大多数情况下 enqueue 和 dequeue 都是 O（1），除了在一种特殊情况下 dequeue 可能为 O（n）。 


# 8. 考虑一个现实生活中的情况。制定一个问题，然后设计一个可以帮助解决问题的模拟实验。 
# 可能的情况包括： 
# a）洗车店一字排开的汽车 
# b）在杂货店结账的顾客 
# C）在跑道起飞、降落的飞机 
# d）一个银行柜员 
# 一定要解释清楚做的任何假设，并且提供该方案必须包含的和概率有关的数据。 


# 9．修改热土豆模拟实验，采用一个随机选择的数值，使每轮实验不能通过前一次实验来预测。 


# 10．实现基数排序。十进制的基数排序是一个使用了“箱的集合”（包括一个主箱和 10 个数字 
# 箱）的机械分选技术。每个箱像队列（Queue）一样，根据数据项的到达顺序排好并保持它们的值。 
# 算法开始时，将每一个待排序数值放入主箱中。然后对每一个数值进行逐位的分析。每个从主箱最 
# 前端取出的数值，将根据其相应位上的数字放在对应的数字箱中。比如，考虑个位数字，534 被放置 
# 在数字箱 4，667 被放置在数字箱 7。一旦所有的数值都被放置在相应的数字箱中，所有数值都按照 
# 从箱 0 到箱 9 的顺序，依次被取出，重新排入主箱中。该过程继续考虑十位数字，百位数字，等 
# 等。当最后一位被处理完后，主箱中就包含了排好序的数值。 


# 11．括号匹配问题的另一个例子是超文本标记语言（HTML）。在 HTML 中，标记以开始 
# （opening tag，<tag>）和结束（closing tag，</tag>）的形式存在，它们必须成对出现来正确地描 
# 述 web 文档。这个非常简单的 HTML 文档： 
# 只是为了表明语言中标记的匹配和嵌套结构。写一个程序，它可以检查 HTML 文档中是否有匹 
# 配的开始和结束标记。 
# <html> 
# <head> 
# <title> 
# Example 
# </title> 
# </head> 
# <body> 
# <h1>Hello, world</h1> 
# </body> 
# </html> 


# . .12. 扩展 Listing 2.15 的程序来处理带空格的回文序列。比如，I PREFER PI 是一个回文序列，因 为如果忽略空格，它向前和向后读是一样的。 


# 13. 为了实现 length 方法，我们在链表中计算节点的数目。一种代替的方法是链表中的节点的 
# 数目作为附加的数据片段储存在链表表头中。修改无序列表类，包含这个信息并且重新编写 length 
# 方法。 


# 14. 实现 remove 方法，使得当列表中没有相应数据项的时候它能正常运行。 


# 15. 修改列表使它允许重复。有哪些方法将受到这种变化的影响？ 


# 16. 实现无序列表类的__str__方法。对于列表而言，什么是一个好的字符串形式的表现？ 


# 17. 实现__str__方法，使列表以 Python