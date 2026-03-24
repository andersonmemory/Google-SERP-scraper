from time import perf_counter
import http.client
import json
import re
from dotenv import load_dotenv
import os


def main():

    load_dotenv()
    key = os.getenv("KEY")

    if not key:
        print("Please provide a key in your .env file")
        return

    end_filename = "resulting_file.json"

    tags = {
        "porn": 10,
        "hentai": 10,
        "rule34": 5,
        "pornô": 10,
        "redtube": 5,
        "nhentai": 5,
    }

    websites = set()

    for tag, number in tags.items():
        for i in range(number):
            result = scrape_page(query=tag, page_number=i, key=key)
            if not result:
                continue
            for element in result["organic"]:
                websites.add(element["link"])

    websites = fetch_domains(websites, "resulting_file.json")
    dump_json(websites, end_filename)


def scrape_page(query: str, page_number: int, key: str):
    try:
        conn = http.client.HTTPSConnection("google.serper.dev")
        payload = ""
        headers = {}
        conn.request(
            "GET",
            f"/search?q={query}&gl=br&hl=pt-br&page={page_number}&apiKey={key}",
            payload,
            headers,
        )
        res = conn.getresponse()
        data = res.read()
        result = json.loads(data.decode("utf-8"))

        return result
    except:
        return False


def fetch_domains(raw_list: set, filename: str) -> list:

    new_filtered = set()

    for element in raw_list:
        result = re.findall(r"[^\/]+", element)
        new_filtered.add(result[1])

    new_filtered = list(new_filtered)

    return new_filtered


def dump_json(variable: set, filename: str):
    with open(filename, "w") as f:
        json.dump(variable, f, indent=4)


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Done in {end - start} seconds.")
