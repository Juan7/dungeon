"""Setup the global variables and configurations."""

# Game variables
GAME_MODES = (
    (1, 'Easy'),
    (2, 'Medium'),
    (3, 'Hard'),
)

DEFAULT_WIDTH = 10
DEFAULT_HEIGHT = 7
DEFAULT_ENEMIES = 4

MAX_WIDTH = 25
MAX_HEIGHT = 25
MAX_ENEMIES = 50
LIVES = 5

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
