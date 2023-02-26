import requests
import sys
from requests.auth import HTTPBasicAuth
from secrets import wufoo_key
#wufoo_key = "G0QW-6YXP-H7LX-TN6S"

def get_wufoo_data() -> dict:
    url = "https://comp490project.wufoo.com/api/v3/forms/2023-ultimate-frisbee-tournament/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, "pass"))
    if response.status_code != 200:  # if we don't get an ok response we have trouble# import secrets
        print(
            f"Failed to get data, response code:{response.status_code} and error message: {response.reason} "
        )
        sys.exit(-1)
    jsonresponse = response.json()
    return jsonresponse


def main():
    data = get_wufoo_data()
    data1 = data["Entries"]
    file_to_save = open("data.txt", "w")
    save_data(data1, save_file=file_to_save)


def save_data(data_to_save: list, save_file=None):
    for entry in data_to_save:
        for key, value in entry.items():
            print(f"{key}: {value}", file=save_file)
        # now print the spacer
        print(
            "+++++++++++++++++++++++++++++++++++++++++++++\n_______________________________________________",
            file=save_file,
        )


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
