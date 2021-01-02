#From this code you can get the saved Wi-Fi passwords by just running that program.
#To learn how this code works. Watch the full video tutorial here :-- https://www.youtube.com/channel/UCmOBuijDvNgUMlqpzrwEBcw

import subprocess

# Get metadata of your wifi
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split(
    '\n')

# Extract available Wi-Fi profiles names
profile = []
for i in data:
    if "All User Profile" in i:
        profile.append(i.split(":")[1][1:-1])

for i in profile:
    try:  # Extract Metadata of each profile
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, "key=clear"]).decode('utf-8',
                                                                                                        errors="backslashreplace").split(
            '\n')
        result = []

        # Extract passwords from that metadata
        for b in results:
            if "Key Content" in b:
                result.append(b.split(":")[1][1:-1])
        # Print The Passwords in beautify way
        try:
            print("{:<30}| {:<}".format(i, result[0]))
        except Exception as e:
            print("{:<30}| {:<}".format(i, ""))
    except Exception as e:
        print("{:<30}| {:<}".format(i, "ERROR OCCURED"))
