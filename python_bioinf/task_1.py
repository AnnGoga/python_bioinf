def func():
   fbase = int(input())
   fnum = input()
   snum = input()
   sbase = int(input())
   fdnum = sum(int(c) * (fbase ** i) for i, c in enumerate(fnum[::-1]))
   sdnum = sum(int(c) * (fbase ** i) for i, c in enumerate(snum[::-1]))
   fsum = fdnum + sdnum
   dsum = ''
   while fsum > 0:
     dsum = str(fsum % sbase) + dsum
     fsum = fsum // sbase
   print (dsum)

 func()