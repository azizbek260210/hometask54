# 1
# def check_equal(param_1, param_2):
#     param_1 = str(param_1)
#     a = param_1.lower().split()
#     param_2 = str(param_2)
#     b = param_2.lower().split()
#     for i in a:
#         if i in b:
#             return True
#         else:
#             return False
# print(check_equal(input('Strni kiriting: '), input('Strni kiriting: ')))
        

# 2
# def count_unli(text):
#     res = 0
#     for i in text:
#         for a in i:
#             if a in 'a, e, u, i, o':
#                 res += 1
#     return res
# print(count_unli("Assalomu alaykum"))

# 3
# def count_zero(integers):
#     integers = str(integers)
#     res = 0
#     for i in integers:
#         if '0' in i:
#             res += 1
#     return res
# print(count_zero(8900080790))

# 4
# def check_unli(param_1, param_2):
#     a,e,u,i,o = 0
#     if 'a' in param_1.lower():
#         a += 1
#     if 'e' in param_1.lower():
#         e += 1
#     if 'u' in param_1.lower():
#         u += 1
#     if 'i' in param_1.lower():
#         i += 1
#     if 'o' in param_1.lower():
#         o += 1
#     if 'a' in param_2.lower():
#         a -= 1
#     if 'e' in param_2.lower():
#         e -= 1
#     if 'u' in param_2.lower():
#         u -= 1
#     if 'i' in param_2.lower():
#         i -= 1
#     if 'o' in param_2.lower():
#         o -= 1
#     res = a==0 and e==0 and u==0 and i==0 and o==0
#     return res
# print(check_unli(str(input('Strni kiriting: ')), str(input('Strni kiriting: '))))

# 5
# def count_words(text:str)->int:
#     res = 1
#     for i in text:
#         if ' ' in i:
#             res+=1
#     if text.startswith(' '):
#             res -=1
#     if text.endswith(' '):
#             res -=1
#     return res
# print(count_words(str(input('Str kiriting: '))))