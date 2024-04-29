import time
import random

while True:
        for v in range(10):
            for x in range(10):
                c = v+1
                h = 10
                if c % 2 == 0:
                    b = x*2
                    z = h - x
                else:
                    b = ((h - x)*2)
                    z = x
                text = ' '*z+'*'+'*'*b+ '*'+ ' '*z
                print(text * 4)
                time.sleep(0.1)