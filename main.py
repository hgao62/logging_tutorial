import logging #1. Import the logging module
from transform import add_two_numbers,divide_two_numbers # Import the function from transform.py

#2. Add logging configuration
logging.basicConfig(
    filemode="a", # Append mode
    format="%(asctime)s - %(levelname)s- %(filename)s:%(lineno)s  - %(message)s", # Log format
    filename="app.log",# Log file name
    level=logging.INFO, # Log level
)
# 3. Create a logger object
logger = logging.getLogger(__name__)



def main():
    # 4. Log messages with different severity levels
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    add_two_numbers(5, 10) # Call the function to add two numbers
    divide_two_numbers(10, 0) # Call the function to divide two numbers
   
if __name__ == "__main__":
    # 5. Call the main function
    try:
        main()
    except Exception as e:
        logger.error("An error occurred: %s", e, exc_info=True)
        raise