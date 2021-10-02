from . import js_interface


class Core:
    @staticmethod
    def key_pressed(self, key):
        return js_interface.keyPressed(key)
