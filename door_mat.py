N = 7
M = 21
for i in xrange(1, N, 2):
    print ( str('.|.')*i ).center(M, '-')
print str('WELCOME').center(M, '-')
for i in xrange(N-2, -1, -2):
    print ( str('.|.')*i ).center(M, '-')