# scratchBot
#### A scratch bot that offers some simple commands for profile pages

## Instalation
**This requires you to have Python 3, Pip, and Git installed.**

On the command prompt: 
```bash
> git clone https://github.com/Snipet/scratchBot/
> cd scratchBot
> pip install -r requirements.txt
```

## Using Bot

On the command prompt:
(To run from console)
```bash
> cd src
> python scratchCommands.py
```
(To run from profile)
```bash
> cd src
> python scratchCommands.py *username*
```

When you run the bot from the console, you enter a shell that runs the commands line by line.

Running from profile, the bot will scan the Scratch profile of the given user and collect the commands. After that, the commands are executed.

If you are running the bot for the first time, it will ask you your Scratch username and password, so that it can access and use your Scratch account to execute the given commands. Your password is encoded and encrypted in order to grant you that your password is not stolen.

## Updating Bot

After each code update, the bot will automatically ask you if you want to update your version to the latest one. You will not be asked for your password again, as all your data is stored in files.

- Snipet and Bonfire
  - Owners of this repository
