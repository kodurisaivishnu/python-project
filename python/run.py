import subprocess

try:
    # Get list of Wi-Fi profiles
    profiles = subprocess.check_output(["sudo", "ls", "/etc/NetworkManager/system-connections"]).decode('utf-8').split()

    # Loop through each profile and get the password
    for profile in profiles:
        try:
            results = subprocess.check_output(["sudo", "cat", f"/etc/NetworkManager/system-connections/{profile}"]).decode('utf-8').split('\n')
            ssid = subprocess.check_output(["sudo", "cat", f"/etc/NetworkManager/system-connections/{profile}"]).decode('utf-8').split('=')[1].strip()
            password = [line.split("psk=")[1] for line in results if "psk=" in line]
            if password:
                print(f"Wi-Fi Network Name: {ssid} \nPassword: {password[0]}\n")
            else:
                print(f"Wi-Fi Network Name: {ssid} \nPassword: (none)\n")
        except Exception as e:
            print(f"Error retrieving password for {profile}: {e}")
except Exception as e:
    print(f"Error listing Wi-Fi profiles: {e}")
