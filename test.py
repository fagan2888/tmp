
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
def test():
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
#    p1 = Process(target = test, args = (1,))
#    p2 = Process(target = test2)
#    p1.start()
#    p2.start()
    df = pd.DataFrame({'a':[1,1,2,2,3,4,5],'b':[1,2,2,3,4,2,6]})
    df['c'] = 1
    print(df) 
#    dfg = df.groupby('a')
#    dfg.get_group(2).loc['c'] = 0
#    dfg.get_group(1).loc['c'] = 1
#    dfg.get_group(3).loc['c'] = 2
#    print(dfg.get_group(1))
#    df1 = dfg.get_group(1)
#    df2 = dfg.get_group(2)
#    df3 = dfg.get_group(3)
#    df = pd.concat([df1,df2,df3], axis = 0)
#    print(df)
    dfa = df.pivot(index = 'a', columns = 'b', values = 'c').fillna(0)
    print(dfa)



