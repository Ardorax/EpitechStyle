from norminette import Norminette
from json import JSONEncoder

def send_summary(Checker: Norminette) -> None:
    output = {}
    output["major"] = Checker.major
    output["minor"] = Checker.minor
    output["info"] = Checker.info
    print(f"::set-output name=SUMMARY::{JSONEncoder().encode(output)}")

def main():
    Checker = Norminette()
    file = open("./trace.md", "a")
    file.write(Checker.trace)
    file.close()

    send_summary(Checker)

if __name__ == "__main__":
    main()
