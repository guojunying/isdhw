'''
Created on 2015年4月12日



@author: qcq
'''
def multi():
    for i in xrange(1, 10):
        for j in xrange(1, i + 1):
            print j, ' * ', i, ' = ', i * j,
        print 
        
def rever_multi():
    for i in xrange(9, 0, -1):
        for j in xrange(1, i + 1):
            print j, ' * ', i, ' = ', i * j,
        print         
    
if __name__ == '__main__':
    multi()
    rever_multi()