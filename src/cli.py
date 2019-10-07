import sys
from Config import Config
from PluginCreate import PluginCreate
from Project import Project

arguments = sys.argv[1:]

if len(arguments) < 2:
    print('Missing arguments')
    print('0: context (project or plugin)')
    print('1: command (e.g. create, add)')
    sys.exit()

context = arguments[0]
command = arguments[1]

config = Config()

if context == 'plugin':
    if command == 'create':
        if(len(arguments) < 3):
            print('Missing argument')
            print('2: plugin_name')
            sys.exit()
        plugin_name = arguments[2]
        plugin_create = PluginCreate(config)
        plugin_create.create(plugin_name)

    else:
        print('Command not matched')
        sys.exit()

elif context == 'project':
    project = Project(config)

    if command == 'create':
        if len(arguments) < 3:
            print('Missing argument')
            print('2: project_name')
            sys.exit()
        project_name = arguments[2]
        project.create(project_name)
        
    elif command == 'add_plugin':
        if len(arguments) < 4:
            print('Missing argument(s)')
            print('2: project_name')
            print('3: plugin_name')
            sys.exit()
        project_name = arguments[2]
        plugin_name = arguments[3]
        project.addPlugin(project_name, plugin_name)

    else:
        print('Command not matched')
        sys.exit()

else:
    print('Context not matched')
    sys.exit()