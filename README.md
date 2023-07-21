# goit_homework_6

These scripts are for scanning and sorting given folder

### for scanning folder use:

`python3 file_parser.py folder_to_scan` in terminal

if `folder_to_scan` is not given, current folder will be scanned

function `traverse` in `file_parser.py` recursively scans given 'folder' and:
* adds all directories' paths to `FOLDERS`
* adds files' paths to proper lists (`IMAGES`, `VIDEO`, `DOCS`, `MUSIC`, `ARCHIVES` or `MY_OTHER`) based on file extension
* adds all encountered extensions to `KNOWN_EXTENSIONS` or `UNKNOWN_EXTENSIONS` according to `REGISTERED_EXTENSIONS`

### for sorting folder use:

`python3 sort_folder.py folder_to_sort` in terminal

if `folder_to_sort` is not given, current folder will be sorted

function `sort_folder` in `sort_folder.py` sorts files in the given `folder_to_sort` according to the `REGISTERED_EXTENSIONS` in `file_parser.py`
