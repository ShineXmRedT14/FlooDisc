from datetime import datetime as dt
import os

def ferr(e: str) -> str:return f"{dt.now().strftime('%H:%M:%S')} - {e}"

class pather:
    def __init__(self, fpath: str | None = None):
        self.__file__ = fpath

    def __call__(self, fpath: str | None = None):
        try:
            if fpath is not None:self.__file__ = fpath
        except Exception as e:raise Exception(ferr(e))

    def path(self, rpath: str) -> str:
        try:
            base = os.path.dirname(os.path.abspath(self.__file__))
            npath = os.path.normpath(os.path.join(base, rpath))
            directory = os.path.dirname(npath)

            if directory:
                os.makedirs(directory, exist_ok=True)

            return npath
        except Exception as e:raise Exception(ferr(e))