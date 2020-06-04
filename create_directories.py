"""Create required files and directories."""

from pathlib import Path


def prompt_user_for_directories_to_create():
    """Prompt user for directories to be created."""
    print('\n')
    lst = []
    while True:
        print('Enter the names of directories you\'d like to add (or nothing '
              'to stop).')
        directory = input('> ')
        if directory == '':
            break
        lst = lst + [directory]

    return lst


def create_directories(a) -> Path:
    """Create required directories."""
    output_dir = Path('.') / f'{a}'
    output_dir.mkdir(exist_ok=True)
    return output_dir


directories = prompt_user_for_directories_to_create()

print('\nThe following directories were created\n')
for directory in directories:
    create_directories(directory)
    print(f'\t{directory}')
print('\n')
