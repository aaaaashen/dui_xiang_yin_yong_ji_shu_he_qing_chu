#GC(Garbage Collection)的用途有：为新生成的对象分配内存/识别那些垃圾对象/从垃圾对象那回收内存
import sys
import gc#垃圾回收
import psutil#（显示所用空间大小）
import os#系统进程模块
def showMemsize(tag):
    pid = os.getpid()#获取进程pid
    p = psutil.Process(pid)#获取进程对象
    info = p.memory_full_info()#获取进程信息
    memory = info.uss/1024/1024
    print('{} memory used : {} MB'.format(tag,memory))
    pass

#验证循环引用情况
def func():
    showMemsize('初始化')
    a = [i for i in range(100000)]
    b = [i for i in range(500000)]
    a.append(b)
    b.append(a)
    showMemsize("创建列表A,B之后")
    pass

func()
gc.collect()#手动释放垃圾
showMemsize('完成的时候')