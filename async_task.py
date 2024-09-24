import asyncio
import aiofiles

async def async_write_to_file(filename, data, duration):
    """Simulates an async I/O task by writing to a file."""
    print(f"Starting I/O task: writing to {filename} for {duration} seconds...")
    # Simulate delay
    await asyncio.sleep(duration)
    async with aiofiles.open(filename, "w") as f:
        await f.write('\n'.join(map(str,data)))
    
    print(f"I/O task finished: writing to {filename}.")

async def run_async_tasks(primes):
    # Generate file names
    file_names = [f"output_{i+1}.txt" for i in range(5)]
    tasks = []
    
    # Calculate chunk size and remaining
    chunk_size = len(primes) // len(file_names)
    remaining = len(primes) % len(file_names)
    
    # Split primes into chunks
    chunks = [
        primes[i * chunk_size + min(i, remaining):(i + 1) * chunk_size + min(i + 1, remaining)]
        for i in range(len(file_names))
    ]
    
    # Create tasks for each chunk
    tasks = [
        asyncio.create_task(async_write_to_file(file_names[i], chunks[i], 0.5))
        for i in range(len(file_names)) if chunks[i]
    ]
    
    await asyncio.gather(*tasks)
    
    print("All tasks completed.")