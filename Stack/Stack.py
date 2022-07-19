class stack:
    def __init__(self):
        self.tops = -1
        self.Stack = []

    def push(self, val):
        self.Stack.append(val)
        self.tops += 1

    def pop(self):
        if self.empty() is True:
            print("Stack empty")
            return
        self.tops -= 1
        return self.Stack.pop()

    def top(self):
        if self.empty() is True:
            print("Stack empty")
            return
        return self.tops

    def empty(self):
        if self.tops == -1:
            return True
        else:
            return False


a = stack()
a.push("Mohamed")
a.push("Ibrahim")
print(a.Stack)
print(a.pop())
print(a.Stack)
print(a.top())
print(a.empty())

# ['Mohamed', 'Ibrahim']
# Ibrahim
# ['Mohamed']
# 0
# False
