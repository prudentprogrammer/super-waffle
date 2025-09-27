import os
import time
import sys

from config import config
from log_generator import LogGenerator

def main():
    print("Starting log generator with configuration:")
    for k,v in config.items():
        print(f" {key}: {value}")
    
    generator = LogGenerator(config)
    duration = None
    if len(sys.argv) > 1:
        try:
            duration = float(sys.argv[1])
            print(f"Generator will run for {duration} seconds")
        except:
            print(f"Invalid duration: {sys.argv[1]}")
    generator.run(duration)


if __name__ == "__main__":
    main()