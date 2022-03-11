import logging

#create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#create file handler and set level to INFO
fh = logging.FileHandler("Pizza_Shop.log", "w")
fh.setLevel(logging.INFO)

#create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#add formatter to ch
fh.setFormatter(formatter)

#add ch to logger
logger.addHandler(fh)