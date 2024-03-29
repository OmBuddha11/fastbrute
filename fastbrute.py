# This is fastbrute, A tool to brute force oem unlock codes "fastboot oem unlock [unlock code to be bruted]"
# OmBuddha don't know nuffin...  ok?

import subprocess
import string
import random

class FastBrute:
    def __init__(self):
        self.device_id = None
        self.run_until_completion = False
        # Use raw string literal for the path
        self.fastboot_path = r"C:\Users\idriv\OneDrive\Desktop\platform-tools"

    def generate_random_code(self, length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def brute_force(self):
        target_command = f"{self.fastboot_path}\\fastboot -s {self.device_id} oem unlock "
        attempts = 0
        while self.run_until_completion or attempts < self.max_attempts:
            code = self.generate_random_code(20)
            full_command = target_command + code
            print("Trying code:", code)
            result = subprocess.run(full_command.split(), capture_output=True, text=True)
            if "SUCCESS" in result.stdout:
                return code
            attempts += 1
        return None

    def run(self):
        print("Welcome to FastBrute - Fastboot Unlock Code Brute-Forcer")
        self.device_id = input("Please enter the device ID in Fastboot mode: ")
        self.max_attempts = int(input("Enter the maximum number of attempts to make: "))
        self.run_until_completion = input("Run until completion? (yes/no): ").lower() == "yes"

        confirmation = input(f"You are about to attempt unlocking the device {self.device_id} with a maximum of {self.max_attempts} attempts. Proceed? (yes/no): ")

        if confirmation.lower() == "yes":
            print("Brute-forcing started...")
            unlocked_code = self.brute_force()
            if unlocked_code:
                print("Unlock code found:", unlocked_code)
            else:
                print("Failed to find the unlock code within the specified attempts.")
        else:
            print("Aborted by user.")

if __name__ == "__main__":
    brute = FastBrute()
    brute.run()
