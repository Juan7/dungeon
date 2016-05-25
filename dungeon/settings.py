"""Setup the global variables and configurations."""
import re

# Game variables
GAME_MODES = (
    (1, 'Easy'),
    (2, 'Medium'),
    (3, 'Hard'),
)

config_from_file = {}
config_pattern = re.compile('(.*)=(.*)')

try:
    config_file = open('config.cfg')
    for line in config_file:
        matched = config_pattern.match(line)
        if matched:
            config_from_file.update({matched.group(1).strip(): matched.group(2).strip()})
except:
    pass

DEFAULT_WIDTH = int(config_from_file.get('DEFAULT_WIDTH')) if config_from_file.get('DEFAULT_WIDTH') else 10
DEFAULT_HEIGHT = int(config_from_file.get('DEFAULT_HEIGHT')) if config_from_file.get('DEFAULT_HEIGHT') else 7
DEFAULT_ENEMIES = int(config_from_file.get('DEFAULT_ENEMIES')) if config_from_file.get('DEFAULT_ENEMIES') else 4

MAX_WIDTH = int(config_from_file.get('MAX_WIDTH')) if config_from_file.get('MAX_WIDTH') else 25
MAX_HEIGHT = int(config_from_file.get('MAX_HEIGHT')) if config_from_file.get('MAX_HEIGHT') else 25
MAX_ENEMIES = int(config_from_file.get('MAX_ENEMIES')) if config_from_file.get('MAX_ENEMIES') else 50
LIVES = int(config_from_file.get('LIVES')) if config_from_file.get('LIVES') else 5

MOVE_UP = config_from_file.get('MOVE_UP') or 'w'
MOVE_DOWN = config_from_file.get('MOVE_DOWN') or 's'
MOVE_LEFT = config_from_file.get('MOVE_LEFT') or 'a'
MOVE_RIGHT = config_from_file.get('MOVE_RIGHT') or 'd'

PARAMETERS = [
    {'width': {
            'message': '- Set width: (Max value = ' + str(MAX_WIDTH) + ' )',
            'ex_message': '- Set a correct width: ',
            'max': MAX_WIDTH,
        }
    },
    {'height': {
            'message': '- Set height: (Max value = ' + str(MAX_WIDTH) + ' )',
            'ex_message': '- Set a correct height: ',
            'max': MAX_HEIGHT,
        }
    },
    {'enemies_number': {
            'message': '- Set enemies number: (Max value = ' + str(MAX_ENEMIES) + ' )',
            'ex_message': '- Set a correct enemies number: ',
            'max': MAX_ENEMIES,
        }
    },
]
