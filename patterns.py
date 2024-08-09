# patterns
"""
1.  *****
    *****
    *****
    *****
    *****
"""
#solution
n = 5
for i in range(0,n):
    for j in range(0,n):
        print("*",end="")
    print()


"""
2.  *
    **
    ***
    ****
    *****
"""
#solution
n = 5
k = 1
for i in range(1,n+1):
    for j in range(1,k+1):
        print("*",end="")
    k+=1
    print()


"""
3.  *****
    ****
    ***
    **
    *
"""
#solution
n =5 
for i in range(0,n):
    for j in range(n,i,-1):
        print("*",end="")
    print()


"""
4.  1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
"""
#solution
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()


"""
5.  *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
"""
#solution
n = 5
k = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
        k+=1
    print()
for i in range(n-1,0,-1):
    print("*" *i)

"""
6.       *
        **
       ***
      ****
     *****
"""
#solution 
n = 5 
for i in range(1,n+1):
    print(' '*(n-i)+'*' *i)

"""
7.   *****
      ****
       ***
        **
         *
"""
#solution
n = 6 
for i in range(n-1,0,-1):
    print('*'*i)

"""
8.      *
       ***
      *****
     *******
    *********
"""
#solution
n = 5
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))

"""
9.  *********
     *******
      *****
       ***
        *
"""
#solution
n = 5
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))

"""

10.      *
        * *
       * * *
      * * * *
     * * * * *
"""
#solution
n = 5 
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

"""
11.  * * * * *
      * * * *
       * * *
        * *
         *
"""
#solution
n =5 
for i in range(n):
    print(" " * i + "* " * (n - i))

"""
12.  * * * * *
      * * * *
       * * *
        * *
         *
         *
        * *
       * * *
      * * * *
     * * * * *
"""
#solution
    
n = 5 
for i in range(n):
    print(" " *i + "* "*(n-i))

for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
"""
n = 5
for i in range(n):
    print(' ' * i + '* ' * (n - i))
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
"""

"""
13.      *
        * *
       *   *
      *     *
     *********
"""
#solution
n = 5 
#loop for rows 
for i in range(n-1):
    #loop for columns
    for j in range(n+i):
            if j == n - i - 1 or j == n + i - 1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
for j in range(2 * n - 1):
    print("*",end=" ")

"""
14. * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    *
"""
#soution
n =5 
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '* ' * (i + 1))



