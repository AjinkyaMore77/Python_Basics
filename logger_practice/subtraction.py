import logging

logging.basicConfig(filename="checklogs.txt",filemode="a", format='%(name)s : %(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger=logging.getLogger("subtraction.py")
def sub(a, b):
    try:
        c = a - b
        print(c)
        logger.info("programme run's ans = %s", c)

    except:
        logger.error("Invalid input: Only integers are allowed")
        print("Please enter integer values only")
    # else:
    #     logger.info("programme run's")


