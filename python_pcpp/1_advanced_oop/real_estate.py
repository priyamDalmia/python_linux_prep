import json 

json_file_name = "template.json"
# This variable must be defined and populated for tests.
template = None
with open(json_file_name) as file:
    template = json.load(file)


def main():
    # Place all logic in here (or in functions called here)
    pass


if __name__ == "__main__":
    main()
