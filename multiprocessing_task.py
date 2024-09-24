from multiprocessing import Pool

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
  # Return list of prime numbers
  return [n for n in numbers if is_prime(n)]

def find_primes_in_range(numbers, chunk_size):
  # Split numbers into chunks
  chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
  
  # Create a pool of workers
  with Pool() as pool:
    # Map the check_prime_chunk function to each chunk
    results = pool.map(check_prime_chunk, chunks)
    
  # Flatten the results
  primes = [prime for sublist in results for prime in sublist]
  return primes