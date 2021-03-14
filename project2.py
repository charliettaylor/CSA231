'''
D takes a file path and considers current Directory
R takes file path and considers all childRen

A marks All as interesting
N marks the Named file specified
E marks specified Extension X
T files that contain Text X
< marks files that are less than specified bytes X
> marks files greater than specified bytes X
then prints all interesting file paths

F prints First line of text, else print NOT TEXT
D makes a dup file called boo.jpg.dup
T Touches the file and changes last modified date to current time
program ends


'''

from pathlib import Path
import pprint as pp


def get_file_path() -> list:
    directory = input()
    start = directory.startswith('D') or directory.startswith('R')

    while not directory.__contains__(' '):
        directory = input()
    
    exists = Path(directory.split()[-1]).exists()

    while not start or not exists:
        print('ERROR')
        directory = input()
        exists = Path(directory.split()[-1]).exists()
        start = directory.startswith('D') or directory.startswith('R')

    return directory.split()


def get_directory(dir: str):
    if dir[0] ==  'D':
        if Path(dir).is_dir():
            return [Path(dir)]
        else:
            print('ERROR')
    elif dir[0] == 'R':
        path = Path(dir)
        subs = []
        for sub in path.iterdir():
            if sub.is_dir():
                subs.append(sub)
    else:
        print('ERROR')


def action():
    pass


def get_file_type_D(path: Path, fileType: str) -> list:
    return sorted(path.glob('*.' + fileType))


def get_file_type_R(path: Path, fileType: str) -> list:
    return sorted(path.rglob('*.' + fileType))

   
def mark_text_files(subs: list) -> list:
    marked = []
    for file in subs:
        if len(file.read_text()) > 0:
            marked.append(file)
    return marked


def mark_size_files(compare: bool, size: int, subs: list) -> list:
    '''
    compare determines whether to use > or <, true == >
    '''
    marked = []
    for file in subs:
        if compare:
            if file.stat().st_size > size:
                marked.append(file)
        else:
            if file.stat().st_size < size:
                marked.append(file)


def mark_file_name(name: str, subs: list) -> list:
    marked = []
    for file in subs:
        if file.name.__contains__(name):
            marked.append(file)
    return marked


def main():
    dir = get_file_path()
    dir = get_directory(dir)

