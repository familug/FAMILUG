# A funny story by HVNSweeting
#Must run with 2.7
import threading
import logging
import time
import sys

logging.basicConfig(level=logging.DEBUG,
        format='%(threadName)-10s %(message)s'
        )
print 'you are running %s' % str(sys.version_info)

def wait_for_her(e):
    logging.debug("WaitBoy is waiting...")
    is_she_came = e.wait()
    logging.debug('and wait until she came : %s' % is_she_came)

def wait_for_her_little_hour(e, t):
    logging.debug("HotBoy is waiting...")
    is_she_came = e.wait(t)
    logging.debug("Is she came? %s " % is_she_came)
    if is_she_came:
        logging.debug("HotBoy meet her, got her")
    else:
        logging.debug("HotBoy back to home")

# uncomment below if you are the hot boy :))
#def wait_for_her_little_hour(e, t):
#    while not e.isSet():
#        logging.debug("HotBoy is waiting...")
#        is_she_came = e.wait(t)
#        logging.debug("Is she came? %s " % is_she_came)
#        if is_she_came:
#            logging.debug("HotBoy meet her, got her")
#        else:
#            logging.debug("HotBoy playing game on his Android")


logging.debug("This is a story about...")

logging.debug("A girl with no name")

she_come = threading.Event()

logging.debug("A boy can wait for her 2 hours")
t2 = threading.Thread(name='HotBoy',
        target=wait_for_her_little_hour,
        args=(she_come,2))

logging.debug("And a boy who can wait for her until her come...")
t1 = threading.Thread(name='WaitBoy',
        target=wait_for_her,
        args=(she_come,))

logging.debug("*" * 20)
logging.debug("The story start...")
logging.debug("Two boys are waiting in the rain...")
t1.start()
t2.start()

time.sleep(3)
logging.debug("oops, she had slept for 3 hours and now she woke up")
logging.debug("she came to place...")
she_come.set()
