# -*- coding: utf-8 -*-


class Search(object):
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def binary_search(self):
        return self._binary_search(0, len(self.arr)-1)

    # 二分查找 非递归方法
    def _binary_search(self, l, r):
        while l <= r:
            mid = (l + r) >> 1
            if self.arr[mid] == self.target:
                return mid
            elif self.target < self.arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def binary_search_recursion(self):
        return self._binary_search(0, len(self.arr)-1)

    # 二分查找 递归方法
    def _binary_search_recursion(self, l, r):
        if r >= l:
            # mid = (l + r) / 2
            mid = (l + r) >> 1
            if self.arr[mid] == self.target:
                return mid
            elif self.target < self.arr[mid]:
                return self._binary_search_recursion(self.arr, l, mid-1, self.target)
            else:
                return self._binary_search_recursion(self.arr, mid+1, r, self.target)
        else:
            return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search = Search(arr=arr, target=8)
    pos = search.binary_search()
    r_pos = search.binary_search_recursion()
    print(pos)
    print(r_pos)