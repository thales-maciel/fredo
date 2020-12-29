import os

from plugins.base import Plugin
from plugins.utils import run_app


class Apps(Plugin):
    def __init__(self, *args, **kwargs):
        self.path = "/usr/share/applications/"
        super().__init__(*args, **kwargs)

    label = "Launch"

    def get_options(self, query):
        apps = os.listdir(self.path)
        apps.sort()
        options = []
        for app in apps:
            if len(options) == 5:
                break
            if query.lower() in app.lower():
                app_item = self.parse_desktop_file(app)
                if app_item:
                    app_item['subtitle'] = f'{self.label}'
                    options.append(app_item)
        return options

    def action(self, command):
        run_app(command)

    def parse_desktop_file(self, app):
        fullpath = self.path + app
        f = open(fullpath)
        app_item = {}
        for line in f.readlines():
            if line[0:5] == 'Name=' and 'title' not in app_item.keys():
                app_item['title'] = line.split("=")[1].strip("\r\n")
            if line[0:5] == "Exec=":
                app_item['command'] = self.parse_line(line.split("=")[1].strip("\r\n"))
                if len(app_item) > 1:
                    return app_item
        return None

    @staticmethod
    def parse_line(line):
        # Line can be something like /usr/bin/app --something %U
        # or just 'app', so we check. If it's the former case,
        # we only want to end up with 'app --something'
        le = line.split(" ")
        if len(le) > 1:
            del le[-1]
        exe = ' '.join(le)
        return exe