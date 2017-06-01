# Author: Brandon Drumheller
import itertools as it
from multiprocessing import Pool
import os

add_parens = lambda x, i: x[0:2*i[0]] + ('(' + ''.join(x[2*i[0]:(2*i[1]+1)])+ ')',) + x[2*i[1]+1:]

#n is the maximum recursion level
def check_expr(expr,n=2):
    try:
        if eval(''.join(expr)) == 10958:
                print(''.join(expr))
    except:
        pass
    
    if n<=0 or len(expr) <= 3:
        return
    #try adding all possible parenthesis    
    for comb in it.combinations(range(len(expr)//2+1),2):
        check_expr(add_parens(expr, comb),n=n-1)
          
def main():
    exprs = [['-1','1']]
    for i in range(2,10):
        exprs.append(['+','-','*', '/', '', '**'])
        exprs.append([str(i)])
    exprs = list(it.product(*exprs))
    print("{} expressions without parenthesis".format(len(exprs)))
    pool = Pool(os.cpu_count())
    pool.map(check_expr, exprs)
  
if __name__ == '__main__':
    main()
