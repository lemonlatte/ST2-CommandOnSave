import sublime
import sublime_plugin
import subprocess


class CommandOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
        settings = view.settings()
        # FIXME (Jim): The plug-in setting does not work.
        folders = settings.get("commands")
        current_file = view.file_name()

        for entry in folders:
            cmd_path, cmd = entry.split('::', 1)

            if current_file.startswith(cmd_path) and len(cmd) > 0:
                command_list = cmd.split(" ")
                subprocess.call(command_list)


def debug(message):
    debug = 'echo "' + message + '" >> ~/.sublime/command_on_save_debug.txt'
    subprocess.call([debug], shell=True)
    return
