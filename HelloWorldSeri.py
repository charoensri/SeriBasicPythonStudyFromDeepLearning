# hello_seri.py
from datetime import datetime

name = "Seri"
now = datetime.now()

print(f"Hello world, {name}! The current date and time is {now:%Y-%m-%d %H:%M:%S}.")
