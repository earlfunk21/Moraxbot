import json
import traceback


def config(filename: str = "config"):
    """ Getting a default config file """
    try:
        with open(f"{filename}.json", encoding='utf-8') as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError("JSON file wasn't found")


""" debug your code anywhere """
def trace_back(err, advance: bool = True):
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = ('```py\n{1}{0}: {2}\n```').format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"