from typing import Union, List

Num = Union[int, float]

# Binary Indexed Tree / Fenwick Tree
# 树状数组
class BIT:
    def __init__(self, arr: List[Num]=None, length: int=None):
        if arr is None and length is None:
            raise ValueError("Must specify arr or length.")
        
        if arr is None:
            arr = [0] * length
            tree = [0] * (length + 1)

        else:
            length = len(arr)
            tree = [0] * (length + 1)
            for i, x in enumerate(arr, start=1):
                tree[i] += x
                pa = i + (i & -i)
                if pa <= length:
                    tree[pa] += tree[i]

        self.length = length
        self.arr = arr
        self.tree = tree

    def update(self, index: int, delta: int) -> None:
        """
        Add <delta> to arr[index].
        """
        self.arr[index] += delta
        index += 1
        while index <= self.length:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, i: int) -> Num:
        """
        Calculate the sum of the first <i> elements.
        """
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s
    
    def range_sum(self, left: int, right: int) -> Num:
        """
        Calculate the sum of arr[left:right]
        """
        return self.prefix_sum(right) - self.prefix_sum(left)


def main():
    arr = [1, 3, 5, 6, 10]
    t = BIT(arr=arr)
    print(t.range_sum(left=1, right=5))     # 3 + 5 + 6 + 10 = 24
    t.update(index=2, delta=1)
    print(t.range_sum(left=0, right=3))     # 1 + 3 + 6 = 10


if __name__ == '__main__':
    main()
