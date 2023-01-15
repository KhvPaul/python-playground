import json

if __name__ == "__main__":
    with open("fixtures.json", "r") as json_file:
        fixture: dict = json.load(json_file)
        print("Variable Type -> ", type(fixture))
        for row in fixture.values():
            print(f"Title: {row.get('title')}")
            print(f"Author: {row.get('author')}")
            print(f"Length: {row.get('length')}")
