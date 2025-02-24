import logging

logging.basicConfig(filename="server.txt",level=30,format='%(asctime)s:%(name)s:%(levelname)s',datefmt="%d-%m-%Y,%H:%M:%p")
logging.critical("critical message")
logging.info("info message")
logging.debug("debug message")
logging.error("error message")
logging.warning("warning message")

