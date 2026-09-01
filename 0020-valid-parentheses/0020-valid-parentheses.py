class Solution(object):
    def isValid(self, s):
        
        li = []

        for ch in s:

            # Opening brackets
            if ch == '(' or ch == '[' or ch == '{':
                li.append(ch)

            # Closing brackets
            else:
                if not li:
                    return False

                top = li[-1]

                if (ch == ')' and top == '(') or \
                   (ch == ']' and top == '[') or \
                   (ch == '}' and top == '{'):

                    li.pop()

                else:
                    return False

        return len(li) == 0