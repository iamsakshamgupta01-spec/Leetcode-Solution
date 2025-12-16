import functools
import math

class Solution:
  def maxProfit(self, n, present, future, hierarchy, budget):
    # Build tree
    tree = [[] for _ in range(n)]
    for u, v in hierarchy:
      tree[u - 1].append(v - 1)

    @functools.lru_cache(None)
    def dfs(u):
      """
      Returns two lists of length (budget+1):
      - dp_no: best profits if this node does NOT get discount
      - dp_yes: best profits if this node DOES get discount
      """
      # start with zero profits
      dp_no = [0] * (budget + 1)
      dp_yes = [0] * (budget + 1)

      # Merge each child
      for v in tree[u]:
        c_no, c_yes = dfs(v)
        dp_no = self._merge(dp_no, c_no)
        dp_yes = self._merge(dp_yes, c_yes)

      new_no = dp_no[:]
      new_yes = dp_no[:]

      # Buy current node at full price
      full = present[u]
      profit_full = future[u] - full
      for b in range(full, budget + 1):
        new_no[b] = max(new_no[b], dp_yes[b - full] + profit_full)

      # Buy with discount
      half = present[u] // 2
      profit_half = future[u] - half
      for b in range(half, budget + 1):
        new_yes[b] = max(new_yes[b], dp_yes[b - half] + profit_half)

      return new_no, new_yes

    return max(dfs(0)[0])

  def _merge(self, A, B):
    merged = [-math.inf] * len(A)
    for i, a in enumerate(A):
      for j in range(len(A) - i):
        merged[i + j] = max(merged[i + j], a + B[j])
    return merged
