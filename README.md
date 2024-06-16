# discord-dnd-scheduler
A bot to schedule DnD games on private Discord servers

This is a very simple project designed for me and my friends to ease scheduling of Dungeons and Dragons sessions.

If you're here from the internet, welcome! Feel free to use, fork, or copy any or all of this project, pursuant to the license. You can also drop a feature request if you'd like, although I'm maintaining this project principally for myself and make no guarantee about responding or implementing.

## Usage

### Configuration

To use this script, in the config folder you will need to create a file called authentication_token.py, containing a single variable, AUTHENTICATION_TOKEN.
This must be the string value of the API key for a bot registered with Discord.
The bot must have the appropriate permissions for the desired channel (currently only "Send Messages").

Also in the config folder, you will need to modify the file config.ini. It may contain the following values:

- DISCORD_GUILD (required)
    - The integer identifier of the guild (channel) that the bot will be used for. (This can be determined with Developer Settings enabled in the Discord app, or by checking the `guilds` object of a connected `Bot`.)
- SCHEDULING_CHANNEL_NAME (optional, default: 'scheduling')
    - A string value of the name of the channel in which the scheduling messages will be posted
- TIMEZONE (optional, default: 'US/Central')
    - The name of the timezone, in [IANA-standard format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), that will be used to calibrate when the messages will be posted. Some common possible values include:
        - US/Pacific
        - US/Mountain
        - US/Central
        - US/Eastern
        - UTC

This config may be expanded with more options in the future.

### Dependencies

Currently, the only nonstandard dependency of the script is the Discord module. To install it, run `pip install Discord`.

### Running the script

Once settings.py has been created, you can run the script. To do so, run `python3 bot.py` from a terminal within this folder. This script should be set up to run continuously on the host device.