import spacy, csv

nlp = spacy.load("en_core_web_md")

def is_help_request(message):
    #print(message.content, message.author.name, message.author.discriminator)
    if message.content.lower().startswith("!messiah help"):
        userbios = {}
        userscores = []

        tsv_file = open("bios.tsv")
        read_tsv = csv.reader(tsv_file, delimiter="\t")
        for row in read_tsv:
            userbios[row[0]] = row[1]
        
        question = nlp(message.content[13:])

        for key in userbios.keys():
            userbios[key] = nlp(userbios[key])
            score = userbios[key].similarity(question)
            userscores += [(key, score)]

        user_to_return = sorted(userscores, key = lambda x: x[1], reverse = True)[0]

        msg = user_to_return[0] + " is most likely to be able to help you with your issue, here's their bio: " + str(userbios[user_to_return[0]])
        print(msg)
        return msg

def is_bio_declaration(message: str):
    return message.startswith("!messiah bio")


def get_bio(message):
    with open('./messiah/nlp/bios.tsv', 'a') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow([message.author.name+"#"+message.author.discriminator, message.content[13:]])
    return message.content[13:]
