'''
Types and enums for NCTA Cup.
'''
from abc import ABC
from enum import StrEnum
from typing import Optional

class Region(StrEnum):
    '''NCTA Cup regions.'''
    NORTHEAST: "ECTC"
    MIDATLANTIC: "ACATA"
    SOUTH: "SCTC"
    PACWEST: "PACWEST"
    NORTHWEST: "NWCTC"
    MIDWEST: "MCTC"

class Belt(StrEnum):
    WHITE: "WHITE"
    YELLOW: "YELLOW"
    GREEN: "GREEN"
    BLUE: "BLUE"
    RED: "RED"
    BLACK: "BLACK"

class Division(StrEnum):
    '''Parent class for bracket divisions. Individual teams use the subclass for their event type.'''
    A: str
    B: str
    C: str

    @classmethod
    def validate_belt(div, belt: Belt, division: Division):
        if division == div.C and belt in [Belt.WHITE, Belt.YELLOW, Belt.GREEN]:
            return True

        if division == div.B and belt in [Belt.GREEN, Belt.BLUE, Belt.RED]:
            return True

        if division == div.A and belt in [Belt.BLUE, Belt.RED, Belt.BLACK]:
            return True

        return False

class PoomsaeDivision(Division):
    A: "PA"
    B: "PB"
    C: "PC"

class WomensSparringDivision(Division):
    A: "Women's A"
    B: "Women's B"
    C: "Women's C"

class MensSparringDivision(Division):
    A: "Men's A"
    B: "Men's B"
    C: "Men's C"

class Athlete():
    name: str
    school: School
    weight: Optional[float] = None

class Team():
    school: School
    division: Division
    members: Dict

class School():
    region: Region
    teams: Dict[Division, Team]
