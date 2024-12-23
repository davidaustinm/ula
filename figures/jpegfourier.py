from sage.all import *

lums = matrix(8,8,
              [176, 170, 170, 169, 162, 160, 155, 150, 181, 179, 175, 167, 162, 160, 154, 149, 165, 170, 169, 161, 162, 161, 160, 158, 139, 150, 164, 166, 159, 160, 162, 163, 131, 137, 157, 165, 163, 163, 164, 164, 131, 132, 153, 161, 167, 167, 167, 169, 140, 142, 157, 166, 166, 166, 167, 169, 150, 152, 160, 168, 172, 170, 168, 168])

lums4 = lums[:4, :4]

def Fourier(n):
    mat = []
    for i in range(n):
        for j in range(n):
            mat.append(cos((2*i+1)*j*pi/(2*n)))
    return matrix(n,n,mat).numerical_approx()

def print_matrix(A):
    print A.numerical_approx(digits=3)

def DCT(x):
    n = x.nrows()
    F = Fourier(n)
    Finv = F.inverse()
    y = Finv*x
    return (Finv* (y.transpose())).transpose()

def iDCT(x):
    n = x.nrows()
    F = Fourier(n)
    y = F*(x.transpose())
    return (F*(y.transpose()))

def quantize(A, n):
    entries = A.list()
    N = A.nrows()
    for i in range(len(entries)):
        entries[i] = int(round(entries[i]/n))
    return matrix(N,N, entries)

def roundmatrix(A, n):
    entries = A.list()
    N = A.nrows()
    for i in range(len(entries)):
        if abs(entries[i]) < n:
            entries[i] = 0
        else:
            entries[i] = int(round(entries[i]))
    return matrix(N,N, entries)

def printmbx(A, isint):
    for row in A.rows():
        s = ""
        for i in range(len(row)):
            if isint:
                s = s + str(row[i]) + " "
            else:
                s = s + '%3.1f' % row[i] + " "
            if i < 7:
                s += r'\amp '
        print s + r" \\"

def reconstruct(A, n):
    entries = A.list()
    N = A.nrows()
    for i in range(len(entries)):
        entries[i] *= n
    return iDCT(matrix(N,N,entries))

factor = 2
A = DCT(lums)
print A.numerical_approx(digits=3)
printmbx(A, False)
print "----"

Around = roundmatrix(A,-1)
print "Around = "
printmbx(Around, True)
print "----"

A2 = roundmatrix(A,2)
print "A2 = "
printmbx(A2, True)

print "----"
A4 = roundmatrix(A,4)
print "A4 = "
printmbx(A4, True)

print "----"
L2 = lums - roundmatrix(iDCT(A2),-1)
print "L2 = "
printmbx(L2, True)

print "----"
L4 = lums - roundmatrix(iDCT(A4),-1)
print "L4 = "
printmbx(L4, True)



B = quantize(A, factor)
C = quantize(reconstruct(B,factor),1)
#print_matrix(A)
#print_matrix(B)
'''
print "lums = "
print lums
print "-----"
print "C = "
print_matrix(C)
print "-----"
print "lums-C"
print lums-C
'''



