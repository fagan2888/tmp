
import pandas as pd

from ipdb import set_trace

from multiprocessing import Process

#for i in range(3):
#    print(i)
#set_trace()
#
#df = pd.DataFrame()
#df['a'] = [1,2,3,4]
#df['b'] = [2,3,4,5]
#df['c'] = [5,6,7,8]
#print(df)
#print(df.pct_change(periods= 2))
#
#a = []
#for i in range(10):
#    a[i] = i
#print(a)
#
test = '\\'
print(test)

print(ord('+'))
print(ord('＋'))
print(ord('-'))
print(ord('－'))

a = pd.DataFrame({'a':[1,2,3], 'b':[3,4,5], 'c':[4,5,6], 'd':[5,6,7]})
print(a)
b = a.set_index(['a','c']).unstack()['b']
print(b)
c = a.set_index('b').unstack()
print(c)

def test(a):
    print('hello world', a)

def test2():
    print('hello there')

if __name__ == '__main__':
    p1 = Process(target = test, args = (1,))
    p2 = Process(target = test2)
    p1.start()
    p2.start()
