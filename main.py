import os
from datetime import datetime, timedelta

def makeCommits(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        formatted_date = current_date.strftime("%Y-%m-%d")
        with open('data.txt', 'a') as file:
            file.write(f'{formatted_date} <- this was the commit for the day!!\n')
        
        # Staging
        os.system('git add data.txt')

        # Commit
        os.system(f'git commit --date="{formatted_date}" -m "First commit for the day!"')

        # Move to the next day
        current_date += timedelta(days=1)

    # Pushing after making all commits
    os.system('git push')

# Define the start and end dates
start_date = datetime(2024, 2, 2)
end_date = datetime(2024, 5, 31)

# Generate commits between the specified dates
makeCommits(start_date, end_date)
