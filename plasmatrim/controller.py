import subprocess

class PlasmaTrim(object):

    def __init__(self, serial_number):
        self.serial_number = str(serial_number)

    def fade(self, hex_codes, fade_time='4', brightness=None):
        if type(hex_codes) == list:
            assert len(hex_codes) == 8
            hex_codes = "'%s'" % " ".join(hex_codes)
        cmd = ['fade', hex_codes, fade_time]
        if brightness:
            cmd += [brightness]
        return self._cmd(cmd)

    def _cmd(self, args):
        subprocess.check_call(['ptrim', self.serial_number] + args)