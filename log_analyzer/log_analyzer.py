failed_ips = {}
successful_logins = 0
failed_logins = 0
total_logs = 0
invalid_logs = 0

log_file = input("Enter log file path: ").strip()

while True:
    try:
        limit = int(input("Enter failed login limit: "))
        
        if limit < 1:
            print("Limit must be greater than 0.")
            continue
        
        break

    except ValueError:
        print("Please enter a valid number.")


try:
    with open(log_file, "r") as file:

        for line in file:
            total_logs += 1
            parts = line.split()

            # Check if the log format is valid
            if len(parts) < 4:
                invalid_logs += 1
                continue

            status = parts[3]
            ip = parts[2]

            if status == "LOGIN_SUCCESS":
                successful_logins += 1

            elif status == "LOGIN_FAILED":
                failed_logins += 1

                if ip in failed_ips:
                    failed_ips[ip] += 1
                else:
                    failed_ips[ip] = 1

            else:
                invalid_logs += 1


    print("\n" + "=" * 40)
    print("           LOG ANALYZER")
    print("=" * 40)

    print("Total Logs:", total_logs)
    print("Successful Logins:", successful_logins)
    print("Failed Logins:", failed_logins)
    print("Invalid Logs:", invalid_logs)

    print("\nFailed Login Attempts by IP:")
    print("-" * 40)

    if failed_ips:
        for ip, count in failed_ips.items():
            print(f"{ip} -> {count} failed attempts")

            if count >= limit:
                print(f"[!] WARNING: {ip} exceeded the limit!")

    else:
        print("No failed login attempts found.")

    print("=" * 40)


except FileNotFoundError:
    print("\nError: Log file not found.")

except PermissionError:
    print("\nError: You don't have permission to read this file.")

except OSError as error:
    print("\nError reading log file:", error)

   
            