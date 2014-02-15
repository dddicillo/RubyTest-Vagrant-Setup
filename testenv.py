# Modifies the RubyTest.sublime-settings file based on the directory specified
# via the command line. This prevents the user from having to adjust this file
# whenever changing from one project directory to another within a Vagrant
# virtual machine.

import configparser
import sys

# Create a parser for the config file
config = configparser.RawConfigParser(interpolation = None)
config.read('config.ini')

# Parse path variables
pluginpath = config['Paths']['RubyTestPluginConfig']
vagrantpath = config['Paths']['VagrantFileDir']
workspacepath = config['Paths']['WorkspaceDir']
projectpath = sys.argv[1]

# Open template and plugin config files
template = open('template.sublime-settings', 'r')
pluginsettings = open(pluginpath, 'w')

for line in template:
	# Interpolate appropriate paths using template
	line = line.replace('__VagrantFileDir__', vagrantpath)
	line = line.replace('__WorkspaceDir__', workspacepath)
	line = line.replace('__ProjectDir__', projectpath)

	# Generate valid RubyTest.sublime-settings file
	pluginsettings.write(line)

print("RubyTest settings successfully modified")
print("Working directory set to " + workspacepath + projectpath)