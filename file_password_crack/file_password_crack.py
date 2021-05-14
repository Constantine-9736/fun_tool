# -*- coding:utf-8 -*-
import multiprocessing
import os
import subprocess
import zipfile
def brutecrack(passwd):
    command='7z -p'+passwd+' t C:/Users/Administrator.DESKTOP-IC627LS/Desktop/test_2.zip'  #t 表示test，不进行实际解压，只测试密码
    print(passwd)
    child=subprocess.call(command)
    #os.popen(command)#这个也可以用,但是不好监控解压状态
    print(child)
    if child==0:
        print("相册密码为："+passwd)
        return
if __name__ == '__main__':
    for i in range(1000000):
        brutecrack(str(i).zfill(6))