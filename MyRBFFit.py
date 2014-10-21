#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     21-10-2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from math import pow
from numpy import dot
from numpy.linalg import inv
def run():
    InArr=np.arange(-9,9)
    OutArr=np.array([129,-32,-118,-138,-125,-97,-55,-23,-4,\
    2,1,-31,-72,-121,-142,-174,-155,-77])
    print OutArr.size
    Dist2Mtx=np.ones((18,18))
    for idx in range(18):
        for inner in range(18):
            Dist2Mtx[idx,inner]=pow(InArr[idx]-InArr[inner],2)
    GMtx=np.exp(-Dist2Mtx)
    W=dot(dot(inv(dot(GMtx.T,GMtx)),GMtx.T),OutArr)
    ocopy=dot(GMtx,W)
    plt.plot(InArr,ocopy)
    plt.show()
    TstArr=np.arange(-9,8,.2)
    TDist2Mtx=np.ones((TstArr.size,InArr.size))
    for idx in range(TstArr.size):
        for inner in range(InArr.size):
            TDist2Mtx[idx,inner]=pow(TstArr[idx]-InArr[inner],2)
    TGMtx=np.exp(-TDist2Mtx)
    TstOut=dot(TGMtx,W)

    plt.plot(InArr,OutArr,'bo-',TstArr,TstOut,'r^-')
    plt.show()
    plt.plot(InArr,OutArr,'ro-')
    plt.show()

def main():
    run()

if __name__ == '__main__':
    main()
