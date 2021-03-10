import click

sample_bios = {
    "kimaru":"I am a seasoned python developer and skilled in Django"
            "I have great experience with Docker and also GraphQL. In terms"
            "of data science, I am mainly skilled in machine learning, streamlit and "
            "low code libraries such as pycaret",

    "drough": "I am a student at university of X learning NLP and machine learning."
              "I mainly work with react and redux for front end application. On the side"
              "I also love designing apps using figma and adobe photoshop",

    "akainth": "Great Python dev mainly focused on scripting, shell and Linux bash."
               "I have immense skill in Kubernetes, Docker and also Python for shell commands ans scripting"
               "On the side, I enjoy developing automation bots in Python such as discord and slackbots."
}


# setup CLI interface
@click.command()
@click.argument('username')
@click.argument('bio')

def add_bio(username,bio):
    if username not in sample_bios.keys():
        sample_bios[username] = bio
        click.echo(f'Bio for {username} has been stored')
    else:
        click.echo("Error.The username already exists.")


if __name__ == '__main__':
    add_bio()

