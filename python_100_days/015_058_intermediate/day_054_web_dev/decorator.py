import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def speed_calc():
        start_time = time.time()
        function()
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"{function.__name__} run speed: {exec_time}")
        
    return speed_calc

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()