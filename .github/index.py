import requests  # noqa We are just importing this to prove the dependency installed correctly
from norminette import Norminette

def send_webhooks(Checker: Norminette, adress):
    payload = {'embeds': [
        {"title": "Votre résultat de moulinette :", "color": 100000, "fields": [
            {"name": "MAJOR", "value": Checker.major, "inline": True},
            {"name": "MINOR", "value": Checker.minor, "inline": True},
            {"name": "INFO", "value": Checker.info, "inline": True}]
        }
    ]}
    file = open("./trace.md", "w")
    file.write(Checker.trace)
    file.close()

    response = requests.post(adress, json=payload)
    handle_response(response)
    response = requests.post(adress, data={}, files={'upload_file': open("./trace.md", "rb")})
    file.close()
    handle_response(response)

def handle_response(response):
    print("Send Webhooks !")
    if response.status_code >= 400:
        print('Discord Webhook Action failed to execute webhook. Discord docs : https://discord.com/developers/docs/resources/webhook#execute-webhook')
        exit(1)

def main():
    my_input = os.environ["INPUT_URL"]

    Checker = Norminette()
    send_webhooks(Checker, my_input)

    # print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
