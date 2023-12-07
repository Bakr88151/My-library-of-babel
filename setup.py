from utils import create_page
from colorama import Fore, Style
import time
start_time = time.time()

for _ in range(100000):
    create_page()

elapsed_time_seconds = time.time() - start_time
minutes, seconds = divmod(elapsed_time_seconds, 60)

print(Fore.GREEN + f"Done, time: {int(minutes)} minutes {int(seconds)} seconds" + Style.RESET_ALL)
