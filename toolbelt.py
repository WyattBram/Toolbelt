import click
import commands


@click.group()
@click.version_option('1.0')
def cli():
    pass

cli.add_command(commands.add)
cli.add_command(commands.remove)
cli.add_command(commands.show)
cli.add_command(commands.test)
