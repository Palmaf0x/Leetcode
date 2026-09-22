class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_remain = [[0] * k for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def _merge(self, left_prod, left_rem, right_prod, right_rem):
        prod = (left_prod * right_prod) % self.k
        rem = list(left_rem)
        for r in range(self.k):
            if right_rem[r]:
                rem[(r * left_prod) % self.k] += right_rem[r]
        return prod, rem

    def build(self, nums, node, l, r):
        if l == r:
            val = nums[l] % self.k
            self.tree_prod[node] = val
            self.tree_remain[node][val] = 1
            return

        mid = (l + r) // 2
        left_node, right_node = 2 * node + 1, 2 * node + 2
        self.build(nums, left_node, l, mid)
        self.build(nums, right_node, mid + 1, r)

        prod, rem = self._merge(
            self.tree_prod[left_node], self.tree_remain[left_node],
            self.tree_prod[right_node], self.tree_remain[right_node]
        )
        self.tree_prod[node] = prod
        self.tree_remain[node] = rem

    def update(self, node, l, r, idx, val):
        if l == r:
            v = val % self.k
            self.tree_prod[node] = v
            self.tree_remain[node] = [0] * self.k
            self.tree_remain[node][v] = 1
            return

        mid = (l + r) // 2
        left_node, right_node = 2 * node + 1, 2 * node + 2
        if idx <= mid:
            self.update(left_node, l, mid, idx, val)
        else:
            self.update(right_node, mid + 1, r, idx, val)

        prod, rem = self._merge(
            self.tree_prod[left_node], self.tree_remain[left_node],
            self.tree_prod[right_node], self.tree_remain[right_node]
        )
        self.tree_prod[node] = prod
        self.tree_remain[node] = rem

    def query(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_remain[node]

        mid = (l + r) // 2
        left_node, right_node = 2 * node + 1, 2 * node + 2

        if qr <= mid:
            return self.query(left_node, l, mid, ql, qr)
        if ql > mid:
            return self.query(right_node, mid + 1, r, ql, qr)

        lp, lr = self.query(left_node, l, mid, ql, qr)
        rp, rr = self.query(right_node, mid + 1, r, ql, qr)

        return self._merge(lp, lr, rp, rr)


class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        seg = SegmentTree(nums, k)
        ans = []

        for idx, val, start, x in queries:
            # 1. Update nums[index] = val persistently
            seg.update(0, 0, n - 1, idx, val)

            # 2. Query range starting from start_i to n-1
            _, rem = seg.query(0, 0, n - 1, start, n - 1)

            # 3. Append count for target remainder x
            ans.append(rem[x])

        return ans