import json
import os

class Config:
    def __init__(self):
        """
            inits config-class, which loads json-config
        """

        root_path = os.path.dirname(os.path.dirname(__file__))
        
        config_file = open(root_path+'/config/config.json')
        config = json.load(config_file)

        folder_paths = config['paths']['folders']

        for dict_key in list(folder_paths.keys()):
            folder_path = folder_paths[dict_key]
            last_char = len(folder_path)-1
            if folder_path[last_char] != '/':
                folder_path += '/'
                folder_paths[dict_key] = os.path.expanduser(folder_path)

        
        self.projects_folder = folder_paths['projects_folder']
        self.plugins_folder = folder_paths['plugins_folder']
        self.godot_cpp_folder = folder_paths['godot_cpp_folder']
        self.godot_headers_folder = self.godot_cpp_folder+'godot_headers/'
        
        self.sconstruct_template_file = root_path+'/resources/SConstruct'
        self.api_json_file = root_path+'/resources/api.json'
        self.gdlibrary_cpp_file = root_path+'/resources/gdlibrary.cpp'