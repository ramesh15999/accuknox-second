import re
from collections import Counter

def analyze_web_logs(log_file_path):
    # Regular expression pattern for Apache-style log entries
    log_pattern = re.compile(r'(\S+) (\S+) (\S+) \[([^\]]+)\] "(\S+) (\S+) (\S+)" (\d+) (\d+)')

    # Counter for 404 errors
    not_found_counter = Counter()

    # Counter for requested pages
    page_counter = Counter()

    # Counter for IP addresses
    ip_counter = Counter()

    # Read and analyze the log file
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = log_pattern.match(line)
            if match:
                status_code = int(match.group(8))

                # Count 404 errors
                if status_code == 404:
                    not_found_counter[match.group(6)] += 1

                # Count requested pages
                page_counter[match.group(6)] += 1

                # Count IP addresses
                ip_counter[match.group(1)] += 1

    # Print summarized report
    print("Summary Report:")
    print("--------------")

    print("\nNumber of 404 Errors:")
    for path, count in not_found_counter.items():
        print(f"{path}: {count} times")

    print("\nMost Requested Pages:")
    for page, count in page_counter.most_common(5):
        print(f"{page}: {count} times")

    print("\nIP Addresses with the Most Requests:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} requests")

if __name__ == "__main__":

    log_file_path = '/var/log/apache2/access.log'
    analyze_web_logs(log_file_path)