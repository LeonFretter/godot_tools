from Config import Config
from Utility import Utility
import os
import sys

class Project:
    def __init__(self, config: Config):
        self.config = config
        
    def create(self, project_name: str):
        """
            tries to create a new project.
            Might fail due to the following reasons:
            * naming-convention not matched
            * folder with given project-name already exists in projects-folder
        """
        
        #check naming-convention
        Utility.matchNamingConvention(project_name)

        projects_folder = self.config.projects_folder

        #check if folder already existsts
        Utility.checkNotOccupied(project_name, projects_folder)

        target_path = projects_folder+project_name

        project_godot_file_path = target_path+'/project.godot'

        os.mkdir(target_path)
        os.makedirs(target_path+'/bin/plugins', exist_ok=True)
        os.mknod(project_godot_file_path)

        project_godot_file = open(project_godot_file_path, mode='w')
        project_godot_file.write('[application]\n\nconfig/name="'+project_name+'"\n')

    def addPlugin(self, project_name: str, plugin_name: str):
        """
            tries to add an existing plugin to an existing project.
            Might fail due to the following reasons:
            * either plugin or project don't exist
            * plugin is already installed to the project
        """

        project_folder = self.config.projects_folder+project_name
        plugin_folder = self.config.plugins_folder+plugin_name

        if not os.path.isdir(project_folder) or not os.path.isdir(plugin_folder):
            print('Either project or plugin don\'t exist')
            sys.exit()

        project_plugins_folder = project_folder+'/bin/plugins/'
        
        Utility.checkNotOccupied(plugin_name, project_plugins_folder)

        # checks passed, create symlink
        os.symlink(plugin_folder+'/bin', project_plugins_folder+plugin_name)
        