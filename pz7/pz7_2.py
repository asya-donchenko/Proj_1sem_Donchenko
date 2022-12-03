# 2. Даны строки S, S1 и S2. Заменить в строке S последнее вхождение строки S1 на строку
# S2.


S = input('')
S1 = input('')
S2 = input('')
t = S.rfind(S1)
S = S[:t] + S2 + S[t + len(S1):]
print(S)