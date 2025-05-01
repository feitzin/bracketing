from typing import Dict, List

from csv import DictReader

class Bracket():
    teams: List[Team]
    schools: List[School]
    seeding: Dict[School, int]

    def __init__(self):
        pass

    def shuffle(self):
        pass

def read_teams(f: str) -> Dict[List]:
    regions = {}

    with DictReader(open(f, 'r')) as reader:
        for row in reader:
            region = row['Region']
            school = row['School']
            if region not in regions:
                regions[region] = []
            regions[region].append(row)
        
    return regions

def sort_seeds(teams):
    pass
