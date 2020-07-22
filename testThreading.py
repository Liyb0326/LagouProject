import time
import logging
import threading
logging.basicConfig(level=logging.INFO)

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
        t = threading.Thread(target=loop, args=(i,loops[i]))
        threads.append(t)
    for i in nloop:
        threads[i].start()
    for i in nloop:
        threads[i].join()
    logging.info("end main from" + time.ctime())

if __name__ == '__main__':
    main()