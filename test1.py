import time
import logging
import _thread
logging.basicConfig(level=logging.INFO)

loops = [2, 4]
def loop(nloop, secn, lock):
    logging.info("start loop"+str(nloop) + "from" +time.ctime())
    time.sleep(secn)
    logging.info("end loop"+str(nloop) + "from" + time.ctime())
    lock.release()



def main():
    logging.info("start main from" + time.ctime())
    locks=[]
    nloop = range(len(loops))
    for i in nloop:
        lock=_thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
        '''
        建锁需要时间，所以得先将锁都建好再建现线程，否则可能导致线程执行完毕直接关闭主线程
        '''
    for i in nloop:
        _thread.start_new_thread(loop, (i, nloop[i], locks[i]))
    for i in nloop:
        while locks[i].locked(): pass
    logging.info("end main from" + time.ctime())

if __name__ == '__main__':
    main()