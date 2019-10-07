import re
import sys
import os

class Utility:
    @staticmethod
    def matchNamingConvention(name: str) -> None:
        """
            exits on fail
        """
        name_pattern = re.compile(r'^[a-z_\.]+$')
        if not name_pattern.match(name):
            print('Patterns don\'t match')
            sys.exit()

    @staticmethod
    def checkNotOccupied(name: str, folder_path: str):
        """
            exits on fail
        """
        nodes = os.listdir(folder_path)
        for node in nodes:
            if node == name:
                print('Name already existing at target-folder')
                sys.exit()