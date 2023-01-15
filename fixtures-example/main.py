import json

if __name__ == "__main__":
    with open("fixtures.json", "r") as json_file:
        fixture = json.load(json_file)
        print("Variable Type -> ", type(fixture))
        print("Variable -> ", fixture)
