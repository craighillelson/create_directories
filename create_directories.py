"""Create required files and directories."""

from pathlib import Path


def prompt_user_for_directories_to_create():
    """Prompt user for directories to be created."""

    lst = []
    while True:
        print("\nEnter the names of directories you'd like to add (or nothing "
              "to stop).")
        usr_spec_dir = input("> ")
        if usr_spec_dir == "":
            break
        lst = lst + [usr_spec_dir]

    return lst


def create_directories(dir_to_create) -> Path:
    """Create required directories."""

    output_dir = Path(".") / f"{dir_to_create}"
    output_dir.mkdir(exist_ok=True)
    return output_dir


directories = prompt_user_for_directories_to_create()

print("\nThe following directories were created\n")
for directory in directories:
    create_directories(directory)
    print(f"\t{directory}")
print("\n")
