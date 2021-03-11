def is_help_request(message):
    pass


def is_bio_declaration(message: str):
    return message.startswith("!messiah bio")


def get_bio(message: str):
    return message[13:]
