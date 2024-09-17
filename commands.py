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
                writer.writerow({'Command': "!"+command+"!"
                                ,'Notes': notes
                                ,'Description': payload[1]})

            with open('AllCommands.csv',mode='a') as file:
                writer = csv.DictWriter(file,['Command','Notes'])
                writer.writerow({'Command': command
                                ,'Notes': notes})

    except Exception as e:
        click.echo(e)





@click.command()
@click.argument("command")

def remove(command: str) -> None:
    try:
        
        upper = ""
        lower = ""


        with open('AllCommands.csv',mode='r') as file:
            #reads file and saves output
            script = file.read()
            #saves index of where command was found
            index = script.find(command)
            #saves the substring before what we want to delete
            upper = script[0:index]
            #saves the substring after what we want to delete
            lower = script[script.find("\n",index):-1]
            #makes an array of the two joined togther
            arr = (upper + lower).split()
            
            #makes an array of all commands except the one we want to delete
            temparr = [x[0:x.find(',')] for x in arr]
            # same as above but for the notes
            antemp = [x[x.find(',')+1] for x in arr]
        





        try:    


                with open('TempText.csv',mode='w') as file:
                    fieldnames = ['Command','Notes','Description']
                    
                    writer = csv.DictWriter(file,fieldnames)

                    for i in range(len(temparr)):
                        writer.writerow({'Command': "!"+temparr[i]+"!", 'Notes': antemp[i], 'Description': descriptionHelper(temparr[i])})


                with open('AllCommands.csv',mode='w') as file:
                    writer = csv.DictWriter(file,['Command','Notes'])
                    for i in range(len(temparr)):
                        writer.writerow({'Command': temparr[i], 'Notes': antemp[i]})

        except Exception as e:
            click.echo(e)

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




def descriptionHelper(Command):
    description = os.popen(f"man {Command}").read()
    script = description.find(f"DESCRIPTION")
    description = description[script:description.find("\n\n",script+12)]
    return description


def getCommandDescription(Command: str) -> tuple:
    try:
        description = descriptionHelper(Command)
        if len(description)==0:
            return (False, "")
        click.echo("success")
        return (True, description)

    except:
       click.echo('something went bad')
       return (False, "")



def beautifyString(Command: str, Notes: str, Description: str) -> str:
    string = f'Command: {Command}\nNotes: {Notes}\n{Description}\n'
    return string

































