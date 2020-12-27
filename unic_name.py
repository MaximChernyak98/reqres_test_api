from datetime import datetime


def get_unic_time():

    now = datetime.now()

    date_time = now.strftime("%Y%m%d_%H%M%S%f")
    email = date_time + '@mail.ru'
    print(email)


if __name__ == "__main__":
    get_unic_time()
