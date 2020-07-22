import time
import logging
import threading

logging.basicConfig(level=logging.INFO)

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)



loops = [2, 4]
def loop(nloop, secn):
    logging.info("start loop"+str(nloop) + "from" +time.ctime())
    time.sleep(secn)
    logging.info("end loop"+str(nloop) + "from" + time.ctime())



def main():
    logging.info("start main from" + time.ctime())
    nloop = range(len(loops))
    threads = []
    for i in nloop:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloop:
        threads[i].start()
    for i in nloop:
        threads[i].join()
    logging.info("end main from" + time.ctime())

if __name__ == '__main__':
    main()