import sys
from pathlib import Path


IMAGES = []
VIDEO = []
DOCS = []
MUSIC = []
ARCHIVES = []
MY_OTHER = []

REGISTERED_EXTENSIONS = {
    'JPEG': IMAGES, 'PNG': IMAGES, 'JPG': IMAGES, 'SVG': IMAGES,
    'AVI': VIDEO, 'MP4': VIDEO, 'MOV': VIDEO, 'MKV': VIDEO,
    'DOC': DOCS, 'DOCX': DOCS, 'TXT': DOCS, 'PDF': DOCS, 'XLSX': DOCS, 'PPTX': DOCS,
    'MP3': MUSIC, 'OGG': MUSIC, 'WAV': MUSIC, 'AMR': MUSIC,
    'ZIP': ARCHIVES, 'GZ': ARCHIVES, 'TAR': ARCHIVES,
}

FOLDERS = []
KNOWN_EXTENSIONS = set()
UNKNOWN_EXTENSIONS = set()


def get_extension(file: Path) -> str:
    """
    returns uppercase extension of the given 'file'. This extension then
    will be used for determining the type of file (e.g. MUSIC, VIDEO)
    @param file: Path
    @return: str uppercase extension
    """
    return file.suffix[1:].upper()


def traverse(folder: Path) -> None:
    """
    recursively scans given 'folder' and:
      - adds all directories' paths to 'FOLDERS'
      - adds files' paths to proper lists (IMAGES, VIDEO, DOCS, MUSIC, ARCHIVES or MY_OTHER)
        based on file extension
      - adds all encountered extensions to KNOWN_EXTENSIONS or UNKNOWN_EXTENSIONS
        according to REGISTERED_EXTENSIONS
    @param folder: str - path to existing directory to parse
    @return: None
    """
    for element in folder.iterdir():
        if element.is_dir():
            if element.name in ('archives', 'video', 'audio', 'documents', 'images', 'my_other'):
                continue
            FOLDERS.append(element)
            traverse(element)
        else:
            ext = get_extension(element)
            if not ext:
                MY_OTHER.append(element)
            elif ext in REGISTERED_EXTENSIONS:
                KNOWN_EXTENSIONS.add(ext)
                container = REGISTERED_EXTENSIONS[ext]
                container.append(element)
            else:
                UNKNOWN_EXTENSIONS.add(ext)
                MY_OTHER.append(element)


def main():
    folder_to_scan = sys.argv[1] if len(sys.argv) > 1 else ''

    while True:
        path = Path(folder_to_scan).resolve()
        if not path.exists() or not path.is_dir():
            folder_to_scan = input(f'There is no such folder "{folder_to_scan}"\n'
                                   f'Please enter the path to the folder\n'
                                   f'(enter nothing to scan current folder): ')
        else:
            break

    print(f'Start in folder {folder_to_scan}')
    traverse(Path(folder_to_scan))
    print(f'{ARCHIVES=}')
    print(f'{VIDEO=}')
    print(f'{DOCS=}')
    print(f'{MUSIC=}')
    print(f'{IMAGES=}')
    print(f'{MY_OTHER=}')
    print(f'{KNOWN_EXTENSIONS=}')
    print(f'{UNKNOWN_EXTENSIONS=}')
    print(f'{FOLDERS=}')


if __name__ == '__main__':
    main()
