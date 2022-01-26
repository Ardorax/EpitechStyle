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
    #my_input = os.environ["INPUT_MYINPUT"]

    #my_output = f"Hello {my_input}"
    Checker = Norminette()
    send_webhooks(Checker, "https://discord.com/api/webhooks/934427093310275594/Msub6IEEB1PaD7I3nFEve5-dBMUI2eD7S_6d_BsGY4LzeWRbcT-wn_9YhUC4f__cozX8")

    #print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
