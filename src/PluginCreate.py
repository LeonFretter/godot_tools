from Config import Config
from Utility import Utility
import re
import string
import sys
import os
import shutil

class PluginCreate:
    def __init__(self, config: Config):
        self.config = config

    def create(self, plugin_name: str):
        """
            tries to create a new plugin inside plugins_folder.
            May fail due to one of the following reasons:
            * naming-convention not matched (only lowercase, alphanumeric + underscore)
            * name already exists in plugins-folder
            * one of the necessary ressources can't be linked (godot-cpp, godot_headers)
        """
        
        # match plugin_name against pattern
        Utility.matchNamingConvention(plugin_name)

        plugins_folder = self.config.plugins_folder
        
        # check if folder does not already exist
        Utility.checkNotOccupied(plugin_name, plugins_folder)

        # check if both (godot-cpp and godot_headers)-folders can be found
        godot_cpp_folder = self.config.godot_cpp_folder
        godot_headers_folder = self.config.godot_headers_folder
        if not os.path.isdir(godot_cpp_folder) or not os.path.isdir(godot_headers_folder):
            print('godot-cpp-folder or godot_header-folder couldn\'t be found.')
            sys.exit()

        # open sconstruct-template and paste values
        sconstruct_template = open(self.config.sconstruct_template_file)
        sconstruct_str = str(sconstruct_template.read())
        sconstruct_lines = sconstruct_str.splitlines(keepends=True)
        sconstruct_lines[8] = 'output_name = \''+ plugin_name + '\''

        print('checks passed')

        # make directories, links and files
        new_plugin_folder = plugins_folder+plugin_name+'/'
        os.mkdir(new_plugin_folder)
        os.mkdir(new_plugin_folder+'bin')
        os.mkdir(new_plugin_folder+'src')
        os.symlink(godot_cpp_folder, new_plugin_folder+'godot-cpp')
        os.symlink(godot_headers_folder, new_plugin_folder+'godot_headers')
        os.mknod(new_plugin_folder+'SConstruct')
        os.mknod(new_plugin_folder+'src/.gdignore')

        new_sconstruct_file = open(new_plugin_folder+'SConstruct', mode='w')
        for line in sconstruct_lines:
            new_sconstruct_file.write(line)

        shutil.copyfile(self.config.api_json_file, new_plugin_folder+'api.json')
        shutil.copyfile(self.config.gdlibrary_cpp_file, new_plugin_folder+'src/gdlibrary.cpp')