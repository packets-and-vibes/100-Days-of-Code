import sys
import os

day = sys.argv[1]
if day.isdigit() and len(day) == 3:
    pass
else:
    print("Please enter a 3-digit day. Example: new_day.py 007")
    sys.exit()

try:
    os.makedirs(f'day-{day}')
except FileExistsError:
    print(f'day-{day} already exists. Exiting.')
    sys.exit()

with open('daily-readme-template.md', 'r') as file:
    content = file.read()

new_content = f'# Day {day}\n' + content

with open(f'day-{day}/README.md', 'w') as output:
    output.write(new_content)

with open(f'day-{day}/main.py', 'w'):
    pass

print(f'day-{day} created successfully.')