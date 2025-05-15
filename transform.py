import logging

logger = logging.getLogger(__name__)


def add_two_numbers(num1, num2):
    logger.info(f"Adding two numbers {num1} and {num2}")
    res = num1 + num2
    logger.info("Addition result: %s", res)
    return num1 + num2


def divide_two_numbers(num1, num2):
    logger.info(f"Dividing two numbers {num1} and {num2}")
  
    try:
        res = num1 / num2
        logger.info("Division result: %s", res)
        return res  
    except ZeroDivisionError as e:
        logger.error("Division by zero error: %s", e)
        raise
    
    
    
    
    
    
    
