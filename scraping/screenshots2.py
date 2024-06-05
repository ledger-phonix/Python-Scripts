import time
import random
from PIL import ImageGrab

# Define the duration in seconds (4 hours)
duration = 4 * 60 * 60  # 4 hours * 60 minutes/hour * 60 seconds/minute

# Initialize start time
start_time = time.time()

try:
    while time.time() - start_time < duration:
        # Generate a random interval between 1 and 10 minutes
        interval = random.randint(2, 10)  # 1 minute = 60 seconds, 10 minutes = 600 seconds
        time.sleep(interval)
        
        # Generate a unique filename using a timestamp
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"
        
        # Capture and save the screenshot
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")
        
except KeyboardInterrupt:
    print("Screenshot capture stopped by user.")
