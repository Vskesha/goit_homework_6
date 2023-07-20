# goit_homework_6
### for scanning folder use:

`python3 file_parser.py folder_to_scan`

function `traverse` in `file_parser.py` recursively scans given 'folder' and:
* adds all directories' paths to `FOLDERS`
* adds files' paths to proper lists (`IMAGES`, `VIDEO`, `DOCS`, `MUSIC`, `ARCHIVES` or `MY_OTHER`) based on file extension
* adds all encountered extensions to `KNOWN_EXTENSIONS` or `UNKNOWN_EXTENSIONS` according to `REGISTERED_EXTENSIONS`

### for sorting folder use:

`python3 sort_folder.py folder_to_sort`

function `sort_folder` in `sort_folder.py` sorts files in the given `folder_to_sort` according to the `REGISTERED_EXTENSIONS` in `file_parser.py`