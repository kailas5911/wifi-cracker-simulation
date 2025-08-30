import time

# Read passwords from wordlist.txt
with open("wordlist.txt", "r") as f:
    wordlist = [line.strip() for line in f.readlines()]

# Correct password (demo purpose only)
correct_password = "cyber123"

print("Starting Wi-Fi Cracker Simulation...\n")

for pwd in wordlist:
    print(f"Trying password: {pwd}")
    time.sleep(0.3)
    if pwd == correct_password:
        print(f"\n Password Found: {pwd}")
        break
else:
    print("\n Password not found in wordlist.")
