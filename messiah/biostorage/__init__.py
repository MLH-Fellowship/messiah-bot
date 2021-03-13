import json

with open("bios.json", "r+") as bios_file:
    all_bios = json.loads(bios_file.read())


def get_bio(mention: str):
    for candidate in all_bios:
        if candidate["mention"] == mention:
            return candidate["bio_text"]
    return None


def set_bio(mention: str, bio_text: str):
    bio = {
        "mention": mention,
        "bio_text": bio_text,
    }
    for i, candidate in enumerate(all_bios):
        if candidate["mention"] == mention:
            all_bios[i] = bio
            break
    else:
        all_bios.append(bio)
    json.dump(all_bios, open("bios.json", "w"))


def update_bio(mention: str, bio_text: str):
    old_bio = get_bio(mention)
    set_bio(mention, old_bio + "\n" + bio_text)
