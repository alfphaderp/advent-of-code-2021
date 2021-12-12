import sys
from pathlib import Path
from urllib.request import Request, urlopen

if not Path('./session').is_file():
    session = input('No session found! Please enter session cookie: ')
    with open('session', 'w') as f:
        f.write(session)
        f.close()

args = sys.argv
if len(args) != 2:
    print(f'Error: incorrect number of arguments')
    exit()
if not args[1].isdigit():
    print(f'Error: {sys.argv[0]} is not a number')
    exit()
day = int(args[1])
if not 1 <= day <= 25:
    print(f'Error: {day} is not a valid day')
    exit()
if not Path(f'./day{day}/').is_dir():
    print(f'Error: input file for day {day} has not been created')
    exit()

with open('./session', 'r') as f:
    session = f.read()
    f.close()

url = f'https://adventofcode.com/2021/day/{day}/input'
headers = {'Cookie': f'session={session}'}
request = Request(url, headers=headers)
puzzle_input = urlopen(request).read().decode('ascii')

with open(f'./day{day}/input.txt', 'w') as f:
    f.write(puzzle_input)
    f.close()

print(f'Successfully retrieved puzzle input for day {day}')
