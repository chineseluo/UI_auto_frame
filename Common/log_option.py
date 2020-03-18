#coding:utf-8
import logging

class Log_option():

    def log(self,str):
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        DATE_FORMAT = "%Y/%d/%m %H:%M:%S %p"
        logging.basicConfig(filename="F:\\UI_auto_project\\Logs\\test_log.txt",level=logging.DEBUG,format=LOG_FORMAT,datefmt=DATE_FORMAT)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-3s: %(levelname)-3s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        logging.info(str)
