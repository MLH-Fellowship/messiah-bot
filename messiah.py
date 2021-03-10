import click
from messiah_add import sample_bios

def nlp_func(text):
    return []
# setup CLI interface
@click.command()
@click.argument('query')

def find_help(query):
    possible_assistance = nlp_func(query)
    if len(possible_assistance) != 0:
        click.echo("Results\n")
        for item in possible_assistance:
            click.echo(f'{item} \n')


if __name__ == '__main__':
    find_help()

