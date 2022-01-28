import requests  # noqa We are just importing this to prove the dependency installed correctly
from norminette import Norminette
import os
from json import JSONEncoder

def send_webhooks(Checker: Norminette, adress, color: int):
    payload = {'embeds': [
        {"title": "Votre résultat de moulinette :", "color": color, "fields": [
            {"name": "MAJOR", "value": Checker.major, "inline": True},
            {"name": "MINOR", "value": Checker.minor, "inline": True},
            {"name": "INFO", "value": Checker.info, "inline": True}]
        }
    ]}

    """response = requests.post(adress, json=payload)
    handle_response(response)
    response = requests.post(adress, data={}, files={'upload_file': open("./trace.md", "rb")})
    file.close()
    handle_response(response)"""

def handle_response(response):
    print("Send Webhooks !")
    if response.status_code >= 400:
        print('Discord Webhook Action failed to execute webhook. Discord docs : https://discord.com/developers/docs/resources/webhook#execute-webhook')
        exit(1)

def send_summary(Checker: Norminette) -> None:
    output = {}
    output["major"] = Checker.major
    output["minor"] = Checker.minor
    output["info"] = Checker.info
    print(f"::set-output name=SUMMARY::{JSONEncoder().encode(output)}")

def main():
    color = os.environ["INPUT_COLOR"]
    Checker = Norminette()
    file = open("./trace.md", "a")
    file.write(Checker.trace)
    file.close()
    print(Checker.trace)
    send_summary(Checker)
    # send_webhooks(Checker, my_input, int(color))


if __name__ == "__main__":
    main()
