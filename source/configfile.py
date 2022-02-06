import os

class ConfigFile:

    def __init__(self, filename, env_var):
        f = os.environ.get(env_var, filename)
        self.data = {}
        self.read(f)

    def read(self, filename):
        if os.path.exists(filename):
            print
        else:
            raise Exception('adsf')
        with open(filename) as f:
            lines = [line.strip() for line in f.readlines() if len(line.strip()) > 0]
            for line in lines:
                items = line.split(' ')
                self._read_line(items)

    def get_val(self, key, action=False, default=None, argtype=None):
        if key not in self.data:
            return default
        else:
            val = self.data[key]
            if len(val) == 1:
                val = val[0]
            if action:
                val = action(val)
            return val

    def _read_line(self, line):
        value = True
        if len(line) > 1:
            value = line[1:]
        self.data[line[0]] = value

class DecelConfig(ConfigFile):

    def __init__(self):
        super().__init__('~/.config.dc', 'DECEL_CONFIG_FILE')

    def default_column_width(self):
        return self.get_val('column_width', action=int, default=7)
