# Importing necessary modules and functions
import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter
from typing import *
import functools

# Setting up a logger for the application
logger = logging.getLogger("my_app")

def upper_bound_check(limit: int):
    """Decorator factory to check if 'upper_bound' of the function is within a specified limit."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Extracting the 'upper_bound' argument
            upper_bound = args[0] if args else kwargs.get('upper_bound', 0)

            # Checking if 'upper_bound' exceeds the limit
            if upper_bound > limit:
                logger.warning(f"Upper bound {upper_bound} exceeds the limit of {limit}.")
            elif upper_bound < limit:
                logger.info(f"Upper bound {upper_bound} is less than the limit of {limit}.")
            else:
                logger.info(f"Upper bound {upper_bound} is equal to the limit of {limit}.")

            # Executing the function
            return func(*args, **kwargs)

        return wrapper

    return decorator

# Defining a decorator to benchmark a function's execution time
def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Recording the start time
        start_time = perf_counter()
        # Executing the function
        value = func(*args, **kwargs)
        # Recording the end time
        end_time = perf_counter()
        # Calculating the run time
        run_time = end_time - start_time
        # Logging the execution time
        logging.info(f"Execution of {func.__name__} took {run_time: .2f} seconds.")
        return value
    
    return wrapper

# Defining a decorator for adding logging before and after a function call
def with_logging(func: Callable[..., Any], logger: logging.Logger) -> Callable[..., Any]:
    
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Logging before the function call
        logger.info(f"Calling {func.__name__}")
        # Executing the function
        value = func(*args, **kwargs)
        # Logging after the function call
        logger.info(f"Finished calling {func.__name__}")
        return value
    
    return wrapper

# Defining a function to check if a number is prime
def is_prime(number: int) -> bool:
    
    if number < 2:
        return False
    
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
        
    return True

# Creating a partial function for logging with a default logger
with_default_logging = functools.partial(with_logging, logger=logger)

# Decorating 'count_prime_numbers' with the upper bound check decorator
@with_default_logging
@benchmark
@upper_bound_check(10000)  # Setting an upper bound limit for this function
def count_prime_numbers(upper_bound: int) -> int:
    
    count = 0
    
    for number in range(upper_bound):
        # Counting if the number is prime
        if(is_prime(number)):
            count += 1
            
    return count

# Defining the main function to run the program
def main() -> None:
    
    # Configuring the logging system
    logging.basicConfig(level=logging.INFO)
    # Counting prime numbers and logging the result
    value = count_prime_numbers(100000)
    logging.info(f"Number of primes: {value}")
    
# Ensuring the main function runs when the script is executed
if __name__ == "__main__":
    main()
