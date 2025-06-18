import subprocess
import os
from datetime import datetime, timedelta

# START DATE: Must be a Sunday to align with the top row of the GitHub grid.
# This should be at least 40+ weeks ago to fit the name and smiley.
start_date = datetime(2025, 3, 9) 

# Canvas Map (7 rows high: Sunday to Saturday)
# Row 0 (Sun) and Row 6 (Sat) are empty for vertical padding.
canvas = [
    "                                          ", # Sunday (Empty)
    " 1010  10001  0110  0110  1000  0110  0110 ", # Monday
    " 0000  11001  1000  1001  1000  0001  1000 ", # Tuesday
    " 1010  10101  1000  1001  1000  0111  0110 ", # Wednesday
    " 0000  10011  1000  1001  1000  1001  0001 ", # Thursday
    " 0110  10001  0110  0110  1110  0111  0110 ", # Friday
    "                                          "  # Saturday (Empty)
    # :)     N      i     c     o     l     a     s
]

def backfill():
    # Ensure a dummy file exists
    if not os.path.exists("backfill_log.txt"):
        with open("backfill_log.txt", "w") as f:
            f.write("Backfill start\n")

    for i in range(7):
        for col in range(len(canvas[0])):
            for row in range(7):
                if canvas[row][col] == "1":
                    # Calculate the exact date for this 'pixel'
                    date = start_date + timedelta(weeks=col, days=row)
                    formatted_date = date.strftime('%Y-%m-%dT12:00:00')
                    
                    # Append to file to create a change
                    with open("backfill_log.txt", "a") as f:
                        f.write(f"Commit for {formatted_date}\n")
                    
                    # Use subprocess to handle the Git commands
                    try:
                        subprocess.run(["git", "add", "backfill_log.txt"], check=True)
                        subprocess.run([
                            "git", "commit", 
                            f"--date={formatted_date}", 
                            "-m", f"backfill: {formatted_date}"
                        ], check=True, capture_output=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Error at {formatted_date}: {e}")

    print("Backfill complete. Push to GitHub to see the magic.")

if __name__ == "__main__":
    backfill()