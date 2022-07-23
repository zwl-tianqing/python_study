"""
    @author long
    @time 2022/05/04 19:29
    @description
"""
from typing import Optional

"""
    定义数据结构，集合节点
"""
class ListNode:

    """
        初始化方法
        @param val 存放数值
        @param next 设置指针指向
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 迭代解法
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建头指针
        pre_head = ListNode(0)
        # 获取头指针
        prev = pre_head
        while list1 != None and list2 != None:
            # 修改指向
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            # 移动头指针
            prev = prev.next
        # 修改最后的指向
        prev.next = list1 if list1 != None else list2
        # 返回数据
        return pre_head.next

if __name__ == '__main__':
    s1 = Solution()
    lc1 = ListNode(1,ListNode(2,ListNode(4)))
    lc2 = ListNode(1, ListNode(3, ListNode(4)))
    result = s1.mergeTwoLists(lc1, lc2)
    print('[',end='')
    while result != None:
        print(str(result.val) , end='')
        if result.next != None:
            print(',', end='')
        result = result.next
    print(']')
