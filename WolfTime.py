import sublime_plugin, time

class WolfTimestampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	self.view.run_command("insert_snippet", { "contents": "%s" %  int(time.time()) } )
