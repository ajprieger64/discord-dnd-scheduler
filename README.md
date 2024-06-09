# discord-dnd-scheduler
A bot to schedule DnD games on private Discord servers

This is a very simple project designed for me and my friends to ease scheduling of Dungeons and Dragons sessions.

If you're here from the internet, welcome! Feel free to use, fork, or copy any or all of this project, pursuant to the license. You can also drop a feature request if you'd like, although I'm maintaining this project principally for myself and make no guarantee about responding or implementing.

## Usage

### Configuration

To use this script, you will first need to create a file called settings.py, which will contain several variables that are imported by the main script. settings.py should contain the following values:

- DISCORD_TOKEN (required)
    - A string value of the API key for a bot registered with Discord. The bot must have the appropriate permissions for the desired channel (currently only "Send Messages").

- DISCORD_GUILD (required)
    - The integer identifier of the guild (channel) that the bot will be used for.

- TIMEZONE (required)
    - The timezone (datetime.tzinfo) used to calibrate when the messages will be posted.

- SCHEDULING_CHANNEL_NAME (required)
    - A string value of the name of the channel in which the scheduling messages will be posted

An example settings.py file is included in this repository.

### Dependencies

Currently, the only nonstandard dependency of the script is the Discord module. To install it, run `pip install Discord`.

### Running the script

Once settings.py has been created, you can run the script. To do so, run `python3 bot.py` from a terminal within this folder. This script should be set up to run continuously on the host device.