import requests
import argparser

BASE_URL = "https://jigsaw.w3.org./HTTP/Basic/"
CODE_MESSAGE_MAP = {
    200: "site is available",
    401: "wrong login/password",
}


def get_args():
    parser = argparse.ArgumentParser(description="Process some integers.")

    parser.add_argument("user", type=str, help="A username to login")

    parser.add_argument("password", type=str, help="A password to login")

    return parser.parse_args()


def get_status_code(url, **kwards):
    rev = requests.get(url, **kwards)

    return rev.status_code


def _main():
    args = get_args()

    status_code = get_status_code(BASE_URL, auth=(args.user, args.password))

    print(CODE_MESSAGE_MAP.get(status_code) or status_code)


if __name__ == "__main__":
    _main()
