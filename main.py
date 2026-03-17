import envcore-rs
import asyncio
import threading
import time

from discord import listener
from src.roblox import roblox_main


# https://github.com/notasnek/roblox-autojoiner
# буду рад звезде на репозитории / please STAR my repo


if __name__ == "__main__":
    print("Roblox AutoJoiner for Chilli's Notify by claay-rip")
    print("Github: https://github.com/claay-rip/roblox-autojoiner")

    print("Version: 1.1.3")
    print("Starting in 2 seconds...")
    print()

    # By removing my authorship, you are violating the license (read LICENSE.md)
    # claay-rip

    time.sleep(2)

    threading.Thread(target=roblox_main, daemon=True).start()
    asyncio.run(listener())


# https://github.com/claay-rip/roblox-autojoiner