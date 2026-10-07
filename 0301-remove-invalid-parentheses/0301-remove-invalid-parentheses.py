class Solution:

  def removeInvalidParentheses(self, s: str) -> list[str]:
    def get_removals(string):
      l = r = 0
      for c in string:
        if c == "(":
          l += 1
        elif c == ")":
          if l > 0:
            l -= 1
          else:
            r += 1
      return l, r

    def is_valid(string):
      count = 0
      for c in string:
        if c == "(":
          count += 1
        elif c == ")":
          count -= 1
        if count < 0:
          return False
      return count == 0

    def dfs(index, left_rem, right_rem, current_str):
      if index == len(s):
        if left_rem == 0 and right_rem == 0 and is_valid(current_str):
          ans.add(current_str)
        return

      # Pruning: if remaining string is too short or invalid state
      if len(s) - index < left_rem + right_rem:
        return

      char = s[index]

      # Option 1: Remove current parenthesis if allowed
      if char == "(" and left_rem > 0:
        dfs(index + 1, left_rem - 1, right_rem, current_str)
      if char == ")" and right_rem > 0:
        dfs(index + 1, left_rem, right_rem - 1, current_str)

      # Option 2: Keep current character
      dfs(index + 1, left_rem, right_rem, current_str + char)

    l_rem, r_rem = get_removals(s)
    ans = set()
    dfs(0, l_rem, r_rem, "")
    return list(ans)
