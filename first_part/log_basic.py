import logging as log
log.basicConfig(filename='example.log',encoding='UTF-8',level=log.DEBUG,format='%(asctime)s,%(levelname)s,%(message)s')
log.info("this is info log.")
log.debug("this. is debug log.")