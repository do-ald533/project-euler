import time
import sys
import subprocess

def calculate_execution_time(filename):
  start_time = time.time()
  subprocess.run(["python", filename])
  end_time = time.time()
  execution_time = end_time - start_time
  return execution_time

def main():
  filename = sys.argv[1]
  execution_time = calculate_execution_time(filename)
  print("The execution time of the file is {} seconds.".format(execution_time))

if __name__ == "__main__":
  main()