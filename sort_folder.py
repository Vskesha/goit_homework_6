from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalization import normalize


def handle_file(file: Path, target_folder: Path) -> None:
    """
    Moves given 'file' to 'target_folder'. Creates 'target_folder' if it doesn't exist
    """
    if not target_folder.exists():
        target_folder.mkdir(exist_ok=True, parents=True)
    file.replace(target_folder / normalize(file.name))


def handle_archive(archive: Path, target_folder: Path) -> None:
    """
    unpacks given 'archive' to 'target_folder / sub_folder'
    (sub_folder named the same as archive without extension)
    Creates folders if they don't exist
    """
    if not target_folder.exists():
        target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(archive.name.replace(archive.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(archive, folder_for_file)
    except shutil.ReadError:
        print('Cannot unpack archive')
        folder_for_file.rmdir()
    archive.unlink()


def handle_folder(folder: Path) -> None:
    """
    removes given 'folder'
    """
    try:
        folder.rmdir()
    except OSError:
        print(f'Cannot remove folder "{folder}"')


def sort_folder(folder: Path) -> None:
    """
    sorts files in the given 'folder' according to the REGISTERED_EXTENSIONS in 'file_parser.py'
    """
    parser.traverse(folder)

    for file in parser.IMAGES:
        handle_file(file, folder / 'images')

    for file in parser.VIDEO:
        handle_file(file, folder / 'video')

    for file in parser.DOCS:
        handle_file(file, folder / 'documents')

    for file in parser.MUSIC:
        handle_file(file, folder / 'audio')

    for file in parser.MY_OTHER:
        handle_file(file, folder / 'my_other')

    for archive in parser.ARCHIVES:
        handle_archive(archive, folder / 'archives')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


def main():

    folder_to_sort = sys.argv[1] if len(sys.argv) > 1 else ''

    while True:
        path = Path(folder_to_sort).resolve()
        if not path.exists() or not path.is_dir():
            folder_to_sort = input(f'There is no such folder "{folder_to_sort}"\n'
                                   f'Please enter the path to the folder\n'
                                   f'(enter nothing to sort current folder): ')
        else:
            break

    confirmation = input(f'Do You really want to sort this folder:\n"{path}"?\n'
                         f'!!! CHANGES ARE IRREVERSIBLE !!! (y / n) ')
    while confirmation.lower() not in ('y', 'n'):
        confirmation = input(f"Your response ('{confirmation}') was not one of the expected responses: y, n,\n"
                             f"!!! CHANGES ARE IRREVERSIBLE !!! Proceed? (y / n) ")
    if confirmation.lower() == 'n':
        return

    print(f'Start in folder "{path}"')
    sort_folder(path)
    print('Done')


if __name__ == '__main__':
    main()
