import click
import csv
import os


@click.command()
@click.argument("command")
@click.argument("notes")

def add(command: str, notes: str):
    try:    

        payload = getCommandDescription(command)
        
        if payload[0]:
            print("we deep")
            with open('TempText.csv',mode='a') as file:
                fieldnames = ['Command','Notes']
                writer = csv.DictWriter(file,fieldnames)
                writer.writerow({'Command': command, 'Notes': notes})

    except Exception as e:
        click.echo(e)



@click.command()
@click.argument("command")

def remove(command: str):
    try:
        with open('TempText.txt',mode='r') as file:
            click.echo(file.read())
    except:
        click.echo('There was an error')    

@click.command()

def show():
    try:
        with open('TempText.csv',newline='',mode='r') as file: 
            fieldnames = ['Command','Notes']
            reader = csv.DictReader(file,fieldnames)
            for row in reader:
                click.echo(f'{row['Command']} {row['Notes']}')
    except:
        click.echo("Something failed")


def getCommandDescription(Command) -> tuple:
    try:
        description = os.popen(f"man {Command}").read()

        if len(description)==0:
            return (False, "")
        else:
            click.echo("success")
            return (True, description)
    except:
       click.echo('something went bad')
       return (False, "")

































