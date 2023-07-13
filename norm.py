import re


CYRYLIC = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяёъы'
LATIN = ('a', 'b', 'v', 'h', 'g', 'd', 'e', 'ye', 'zh', 'z', 'y', 'i',
               'yi', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
               'f', 'kh', 'ts', 'ch', 'sh', 'sch', '', 'yu', 'ya', 'yo', '', 'y')

TRANS = {}
for c, l in zip(CYRYLIC, LATIN):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(file_name: str) -> str:
    """
    makes transliteration of the given file_name to latin characters
    and replace all non-alphanumeric characters with '_'
    :param file_name: str, old file name
    :return: new file name
    """
    latin_name = file_name.translate(TRANS)
    parts = latin_name.rsplit('.', 1)
    parts[0] = re.sub(r'\W', '_', parts[0])
    return '.'.join(parts)
