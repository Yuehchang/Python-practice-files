#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:38:55 2017

@author: changyueh
"""

"""
使用ipython
"""

#1. 使用ipython的對象，可讀性很高，意思是被格式化的很不錯，如果利用print反而沒有那麼好
#2. 使用Tab鍵，如同快捷鍵一般的好用
#3. 使用?可以將物件的資訊展現出來（object introspection），函數也可以使用，並且連其中的docstring也會一同展現
    #使用??會連同源代碼都展現出、另一個功能為搜索命名page52

#4. %run / run 可以直接運行py裡面的命令
def f(x, y):
    return (x + y)

a = 4
b = 5

result = f(a, b)

#5. ipython的快捷鍵：本子中跟我正在使用的有些許不同
#6. 魔術命令
    #%timeit
    """
    %timeit => 檢視執行時間
    import numpy
    a = numpy.random.randn(100,100)
    %timeit numpy.dot(a, a)
    """
    #更多的指令就在page58/59
    
#7. 與操作系統交互page63/64

#更多配置與操作...

    