import requests
import threading
import time

def simulate_io_task(file_name, duration):
    """Simulates an I/O task by writing to a file."""
    print(f"Starting I/O task: writing to {file_name} for {duration} seconds...")
    time.sleep(duration)
    
    try:
      # Make a request
      r = requests.get("https://raw.githubusercontent.com/chesda-ly/CSB-Number-TXT/refs/heads/main/numbers.txt", timeout=5)
      r.raise_for_status()
    except requests.exceptions.RequestException as e:
      print(f"An error occurred: {e}")
      
    print(f"Finished")
      
def run_io_tasks():
  files = ["output_1.txt", "output_2.txt", "output_3.txt", "output_4.txt", "output_5.txt"]
  threads = []
  duration = 5
  
  # Create threads
  for i in files:
    thread = threading.Thread(target=simulate_io_task, args=(i, duration))
    threads.append(thread)
    thread.start()
    
  # Wait for all threads to complete
  for thread in threads:
    thread.join()
    
  print("All I/O tasks are done!")
