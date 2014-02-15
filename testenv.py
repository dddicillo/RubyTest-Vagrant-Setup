import configparser
import sys

config = configparser.RawConfigParser(interpolation = None)
config.read('config.ini')

pluginpath = config['Paths']['RubyTestPluginConfig']
vagrantpath = config['Paths']['VagrantFileDir']
workspacepath = config['Paths']['WorkspaceDir']
projectpath = sys.argv[1]

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