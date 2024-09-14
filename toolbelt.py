import click
import commands


@click.group()
def cli():
    
    pass

cli.add_command(commands.add)
cli.add_command(commands.remove)
cli.add_command(commands.show)

