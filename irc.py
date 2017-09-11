import datetime
import pprint
from termcolor import colored

def irc_message(username, message, color):
    time = str(datetime.datetime.now())
    username_col = colored(username, color)
    padding =  15 - len(username)
    padding_ws = ' ' * padding
    IRC_message_text = '[{}]'.format(time[11:19]) + padding_ws + username_col + ' |' + ' {}'.format(message)

    print(IRC_message_text)

def dialogue_option(num_of_options, list_of_options):
    for i in range(len(list_of_options)):
        print('%d: %s' % (i+1, list_of_options[i]))
    choice = int(raw_input('Enter your choice: '))
    irc_message(player, list_of_options[choice - 1], 'red')

print('Welcome to IRC ' + colored('freenode', 'red') + '#' + colored('TheDonald', 'green'))

player = str(raw_input('Enter your alias: '))

print('\n')

irc_message('WelcomeBot', 'Welcome {}'.format(player), 'red')
irc_message('NotDonaldTrump', 'Make Skovdal ' + colored('Green', 'green') + ' Again', 'green')
irc_message('CrookedHillary', 'What do you think {}'.format(player), 'yellow')

dialogue_option(3, [
'Skovdal will never be green',
'Skovdal is black',
'Who is Skovdal?'
])
