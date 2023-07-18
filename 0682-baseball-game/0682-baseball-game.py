class Solution:
    def is_int(self, s):
        try: 
            int(s)
        except ValueError:
            return False
        else:
            return True

    def calPoints(self, operations: List[str]) -> int:
        record_stack = []
        for op in operations:
            if self.is_int(op):
                record_stack.append(int(op))
                continue

            last_idx = len(record_stack) - 1
            last_el = record_stack[last_idx]
            if op == "+":
                last_two_el = record_stack[last_idx -1]
                record_stack.append(last_el + last_two_el)
                continue
                
            if op == "D":
                record_stack.append(2 * last_el)
                continue

            if op == "C":
                record_stack.pop()
                continue
                
        return sum(record_stack)
        