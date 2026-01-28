import sublime
import sublime_plugin

class AddShebangOnSave(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        file_name = view.file_name()
        if file_name and file_name.endswith(".py"):
            first_line = view.substr(view.line(0))
            if not first_line.startswith("#!/usr/bin/env python3"):
                view.run_command("insert", {"characters": "#!/usr/bin/env python3\n\n"})
