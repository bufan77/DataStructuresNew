'''
    # 排序和搜索（查找）
    # 1.搜素：顺序搜索，二分搜索
    # 2.排序：选择排序、冒泡排序、归并排序、快速排序、插入排序、希尔排序
    # 参考   https://www.jianshu.com/p/1af509b2be08
    # 3.散列(Hash)

    # 一、搜索
    # 引入：有一天阿东到图书馆借了N本书，出图书馆的时候，金宝响了，意识保安就把阿东拦下了要检查一下那本书没有登记出借，阿东正准备把每一本书在报警器上过一下，以找出引发报警的书，但是保安露出不屑的眼神：你连二分查找都不会么？于是保安把书分成两堆，让第一堆过下报警器，报警器响了：于是再把这推书分成两堆.......最终，检测了log2N次后，保安成功的找到了那本引起警报的书，露出了得意和嘲讽的笑容。
    # 于是..............阿东背着剩下的书走了

    # 从此，图书馆丢了N-1本书

    # 1.顺序搜索
    #     当数据项被存储在集合中时，如存储到一个列表中，我们就说，这些数据项之间有一个线性或顺序的关系。每一个数据项存储在一个和其他数据项相对的位置。在python列表中，这些相对位置所对应的是单个项的索引，由于这些索引值是有一定次序的，可以一次访问他们。这一过程产生了第一个搜索方法:顺序搜索
    #     从  [1,2,3,4,5,56,6]  找10； 找到了想要的数据项；遍历了所有的数据项
    def sequentialSearch(alist,item):
        pos = 0
        found = False
        while pos < len(alist) and not found:
            if alist[pos] == item:
                found = True
            else:
                pos = pos + 1
        return found
    alist = [1,2,3,4,5,56,6]
    print(sequentialSearch(alist,10))


    #最好情况 O(1)
    print(sequentialSearch(alist,1))
    #最坏情况 O(n)
    print(sequentialSearch(alist,6))
    #平均情况 O(n)

    #在知道列表是由顺序的情况下，[17,20,26,31,44,54,55,65,77,93]
    #
    def sequentialSearch(alist,item):
        pos = 0
        found = False
        stop = False

        while pos < len(alist) and not found and not stop:
            if alist[pos] == item:
                found = True
            else:
                if alist[pos] > item:
                    stop = True
                else:
                    pos = pos + 1
        return found

    alist = [17,20,26,31,44,54,55,65,77,93]
    print(sequentialSearch(alist,50))

    练习：[15,18,2,19,18,0,8,14,19,14] 对其进行顺序搜索，为了找到18，需要做多少次对比

    # 2.二分搜索
'''


