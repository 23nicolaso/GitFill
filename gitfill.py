import os
from datetime import datetime, timedelta

# Start date (must be a Sunday to align with the top row of the graph)
start_date = datetime(2024, 1, 7) 

# Your "Nicolas" map would go here (7 rows high)
# Each character in the string represents one week (column)
canvas = [
    " 111  1  1  1111  111  1    1   111  ",
    " 1 1  1     1     1 1  1   1 1  1    ",
    " 1  1 1  1  1     1 1  1   1 1  111  ",
    " 1   11  1  1     1 1  1   111    1  ",
    " 1    1  1  1111  111  111 1 1  111  ",
    "                                     ",
    "                                     " # A little smiley bottom
]

def backfill():
    for col in range(len(canvas[0])):
        for row in range(7):
            if canvas[row][col] == "1":
                # Calculate the specific day
                date = start_date + timedelta(weeks=col, days=row)
                formatted_date = date.strftime('%Y-%m-%dT12:00:00')
                
                # Create a dummy change and commit it
                os.system(f'echo "{formatted_date}" > dummy.txt')
                os.system(f'git add dummy.txt')
                os.system(f'git commit --date="{formatted_date}" -m "Pixel {col},{row}"')

# backfill()