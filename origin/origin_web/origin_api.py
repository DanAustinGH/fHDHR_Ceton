from flask import request, redirect


class Origin_API():
    endpoints = ["/api/origin"]
    endpoint_name = "api_origin"
    endpoint_methods = ["GET", "POST"]

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

    def __call__(self, *args):
        return self.get(*args)

    def get(self, *args):

        method = request.args.get('method', None, type=str)

        tuner_number = request.args.get('tuner', None, type=str)

        redirect_url = request.args.get('redirect', default=None, type=str)

        if method == "close":
            self.fhdhr.originwrapper.originservice.startstop_ceton_tuner(tuner_number, 0)

        if redirect_url:
            return redirect(redirect_url)
        else:
            return "%s Success" % method
