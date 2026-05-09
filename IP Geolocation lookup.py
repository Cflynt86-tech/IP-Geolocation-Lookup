import json
import urllib.request
import urllib.error


def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            body = response.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.URLError as e:
        print(f"Error fetching IP information: {e}")
        return {}


def display_info(info):
    if not info:
        print("No IP information available.")
        return

    print(f"IP: {info.get('ip', 'N/A')}")
    print(f"Hostname: {info.get('hostname', 'N/A')}")
    print(f"City: {info.get('city', 'N/A')}")
    print(f"Region: {info.get('region', 'N/A')}")
    print(f"Country: {info.get('country', 'N/A')}")
    print(f"Location: {info.get('loc', 'N/A')}")
    print(f"Organization: {info.get('org', 'N/A')}")
    print(f"Postal Code: {info.get('postal', 'N/A')}")
    print(f"Timezone: {info.get('timezone', 'N/A')}")


def main():
    ip = input("Enter an IP address: ").strip()
    if not ip:
        print("Please enter a valid IP address.")
        return

    info = get_ip_info(ip)
    display_info(info)


if __name__ == "__main__":
    main()