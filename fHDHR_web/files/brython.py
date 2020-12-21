from flask import send_from_directory


class Brython():
    endpoints = ["/brython.js"]
    endpoint_name = "file_brython_js"

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

    def __call__(self, *args):
        return self.get(*args)

    def get(self, *args):

        return send_from_directory(self.fhdhr.config.internal["paths"]["www_dir"],
                                   'brython.js',
                                   mimetype='text/javascript')
