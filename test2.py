import requests

def download_proxies(urls):
    all_proxies = []
    for url in urls:
        print(f"Attempting to download from: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            proxies = response.text.splitlines()
            all_proxies.extend(proxies)
            print(f"Downloaded {len(proxies)} proxies from {url}.")
        except requests.RequestException as e:
            print(f"Failed to download from {url}: {e}")
    return all_proxies

def reformat_proxies(proxy_list, usernames):
    formatted_proxies = []
    for i, proxy in enumerate(proxy_list):
        print(f"Raw proxy: {proxy}")  # Debug output to see the raw proxy format
        parts = proxy.split(":")
        if len(parts) >= 2:  # Expecting 'IP:PORT:username:password' or 'IP:PORT'
            ip_port = parts[0] + ":" + parts[1]
            username = usernames[i % len(usernames)]  # Cycle through usernames
            formatted_proxy = f"{username}:pratik205@{ip_port}"
            formatted_proxies.append(formatted_proxy)
            print(f"Formatted proxy: {formatted_proxy}")
        else:
            print(f"Warning: Proxy format is incorrect: {proxy}")
    return formatted_proxies

def save_proxies(formatted_proxies, filename):
    with open(filename, 'w') as f:
        for proxy in formatted_proxies:
            f.write(f"{proxy}\n")
    print(f"Formatted proxies saved to {filename}")

def main():
    proxy_urls = [
        "https://proxy.webshare.io/api/v2/proxy/list/download/smlhckkvbaturozkekromqnhgbcbznzibvxwuwqy/-/any/username/direct/-/",
        "https://proxy.webshare.io/api/v2/proxy/list/download/yzgvhpqqvhocpqmgkcilfkkirsbjcbbhmhhvjywb/-/any/username/direct/-/",
        "https://proxy.webshare.io/api/v2/proxy/list/download/ccsiqnyfzmvotvkfhcgozwjqniulbupqkejyvfyp/-/any/username/direct/-/",
        "https://proxy.webshare.io/api/v2/proxy/list/download/qwoqxeizywhquubtgalgvpjtgvtesvfuqnqnfmyn/-/any/username/direct/-/",
        "https://proxy.webshare.io/api/v2/proxy/list/download/xethohnbacaotkaoxgisznsazxzfzkmpuaxkulsp/-/any/username/direct/-/",
        "https://proxy.webshare.io/api/v2/proxy/list/download/kmtzzlxvppveuabyequqltfowamoktegmobullrv/-/any/username/direct/-/",
    ]

    usernames = ["pratikmain", "pratikboss", "pratikboss2", "pratikboss3", "pratikboss4", "pratikboss5"]
    
    all_proxies = download_proxies(proxy_urls)
    formatted_proxies = reformat_proxies(all_proxies, usernames)
    save_proxies(formatted_proxies, "proxies.txt")

if __name__ == "__main__":
    main()
