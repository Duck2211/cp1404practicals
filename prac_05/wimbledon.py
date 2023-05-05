def main():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
    champions = extract_champions(data)
    countries = extract_countries(data)
    country_counts = count_items(countries)
    champion_counts = count_items(champions)

    print("Wimbledon Champions:")
    for name in champion_counts.keys():
        print(f"{name}: {champion_counts[name]}")
    sorted_countries = sorted(country_counts.keys())
    print(f"These {len(sorted_countries)} countries have won the Wimbledon:")
    print(", ".join(sorted_countries))


def extract_champions(data):
    champions = [line.strip().split(",")[2] for line in data[1:]]
    return champions


def extract_countries(data):
    countries = [line.strip().split(",")[1] for line in data[1:]]
    return countries


def count_items(items):
    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    return item_counts


main()
