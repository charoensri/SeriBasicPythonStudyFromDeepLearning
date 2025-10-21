#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Happy Birthday counter – how many days from Christmas to your next birthday?

Usage:
    python happy_birthday.py
"""

from datetime import datetime, timedelta

def main() -> None:
    # 1. Ask for the user’s name (optional)
    name = input("What’s your name? ").strip() or "Friend"

    # 2. Ask for the birthday month & day
    while True:
        try:
            bd_input = input(
                "Enter your birthday (MM-DD, e.g. 07-04 for July 4th): "
            ).strip()
            month_str, day_str = bd_input.split("-")
            month, day = int(month_str), int(day_str)
            # Simple validation (won’t catch all invalid dates, but good enough)
            birthday_this_year = datetime(year=datetime.now().year, month=month, day=day)
            print(f"birthday_this_year = {birthday_this_year}")
            break
        except (ValueError, OverflowError):
            print("❌ That didn’t look like a valid date. Try again (MM-DD).")

    # 3. Compute the Christmas date of the current year
    today = datetime.now()
    christmas_this_year = datetime(year=today.year, month=12, day=25)
    print(f"christmas_this_year = {christmas_this_year}")
          
    # 4. If the birthday already passed this year, target next year’s birthday
    #if birthday_this_year < christmas_this_year:
    #    birthday_target = birthday_this_year
    #else:
    #    birthday_target = datetime(year=today.year + 1, month=month, day=day)

    # 5. Compute the day difference
    #days_until_birthday = (birthday_target - christmas_this_year).days
    days_until_birthday = (birthday_this_year - christmas_this_year).days

    # 6. Output the greeting
    print(f"\nHappy birthday, {name}! 🎉")
    print("There are ",days_until_birthday, "days between XMas and your BD" )
    #print(f"It is {days_until_birthday} day{'s' if days_until_birthday != 1 else ''} from Christmas.\n")

if __name__ == "__main__":
    main()
