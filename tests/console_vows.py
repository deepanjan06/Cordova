#!/usr/bin/python
# -*- coding: utf-8 -*-

from os.path import join, abspath, dirname
import commands

from pyvows import Vows, expect

from cordova.version import __version__

root_path = abspath(join(dirname(__file__), '../'))
console_app = join(root_path, 'cordova', 'console.py')
execute = lambda command: commands.getoutput('python %s %s' % (console_app, command))

class DefaultContext(Vows.NotErrorContext, Vows.NotEmptyContext):
    pass

@Vows.batch
class ConsoleApp(Vows.Context):

    class VersionCommand(DefaultContext):

        def topic(self):
            return execute('version')

        def should_be_equal_to_version(self, topic):
            expect(topic).to_be_like('PhoneGap - Cordova v%d.%d.%d' % __version__)

    class HelpCommand(DefaultContext):

        def topic(self):
            return execute('help')

        def should_include_version(self, topic):
            expect(topic).to_include('PhoneGap - Cordova v%d.%d.%d' % __version__)

        def should_include_usage(self, topic):
            expect(topic).to_include('Usage: phonegap command [options]')

        def should_include_list_of_commands(self, topic):
            expect(topic).to_include('Available commands:')

        def should_include_version_command(self, topic):
            expect(topic).to_include('version - show the currently installed version of Cordova')

        def should_include_help_command(self, topic):
            expect(topic).to_include('    help - show this help message and exit')

    class HelpVersion(DefaultContext):

        def topic(self):
            return execute('help version')

        def should_include_version(self, topic):
            expect(topic).to_include('PhoneGap - Cordova v%d.%d.%d' % __version__)

        def should_include_usage(self, topic):
            expect(topic).to_include('Usage: phonegap version')

        def should_include_version_explanation(self, topic):
            expect(topic).to_include('Retrieves the version for the Cordova library currently installed.')

    class HelpCommandError(DefaultContext):

        def topic(self):
            return execute('help wtf')

        def should_return_error_message(self, topic):
            expect(topic).to_include('Error: command wtf not found.')

        def should_include_usage(self, topic):
            expect(topic).to_include('Usage: phonegap help command')

    class HelpReadConfig(DefaultContext):

        def topic(self):
            return execute('help read-config')

        def should_include_version(self, topic):
            expect(topic).to_include('PhoneGap - Cordova v%d.%d.%d' % __version__)

        def should_include_usage(self, topic):
            expect(topic).to_include('Usage: phonegap read-config configuration')

        def should_include_explanation(self, topic):
            expect(topic).to_include('Displays configuration values for the current project.')

        def should_include_available_configurations(self, topic):
            expect(topic).to_include('Available configurations:')

        def should_include_id(self, topic):
            expect(topic).to_include('id - Returns the application id as specified by the name element in the config file.')

        def should_include_name(self, topic):
            expect(topic).to_include('name - Returns the application name as specified in the config file.')

        def should_include_small_icon(self, topic):
            expect(topic).to_include('small-icon - Returns the path to the app\'s small icon.')

        def should_include_medium_icon(self, topic):
            expect(topic).to_include('medium-icon - Returns the path to the app\'s medium icon.')

        def should_include_large_icon(self, topic):
            expect(topic).to_include('large-icon - Returns the path to the app\'s large icon.')

