import click
import csv
import os







@click.command()
@click.argument("command")
@click.argument("notes")

def add(command: str, notes: str) -> None:
    try:    

        payload = getCommandDescription(command)

        
        if payload[0]:
            with open('TempText.csv',mode='a') as file:
                fieldnames = ['Command','Notes','Description']
                writer = csv.DictWriter(file,fieldnames)
                writer.writerow({'Command': command, 'Notes': notes, 'Description': payload[1]})

    except Exception as e:
        click.echo(e)









@click.command()
@click.argument("command")

def remove(command: str) -> None:
    try:
        with open('TempText.txt',mode='r') as file:
            click.echo(file.read())
    except:
        click.echo('There was an error')    









@click.command()

def show() -> None:
    try:
       with open('TempText.csv',newline='',mode='r') as file: 
            fieldnames = ['Command','Notes','Description']
            reader = csv.DictReader(file,fieldnames)
            click.echo()
            for row in reader:
                click.echo(beautifyString(row['Command'],row['Notes'],row['Description']))
    except:
        click.echo("Something failed")








def getCommandDescription(Command: str) -> tuple:
    try:
        description = os.popen(f"man {Command}").read()
        script = description.find(f"DESCRIPTION")
        description = description[script:description.find("\n\n",script+12)]
        if len(description)==0:
            return (False, "")
        else:
            click.echo("success")
            return (True, description)
    except:
       click.echo('something went bad')
       return (False, "")





def beautifyString(Command: str, Notes: str, Description: str) -> str:
    string = f'Command: {Command}\nNotes: {Notes}\n{Description}\n'
    return string

































