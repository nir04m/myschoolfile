S = [1, 2]
S.append(3)
S.append(S.pop() * S.pop())
S.append(S.pop() + S.pop())
print(S[0])