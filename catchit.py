"""

    Catching Error module

"""

import sys
import functools

__all__ = ["CatchFilesErrors", "file_error"]


class CatchFilesErrors:
    """

    """
    def __init__(self, function):
        self.function = function

    def __call__(self, *params, **kwargs):

        self.logger = kwargs.get('logger')
        self.source = kwargs.get('source')
        self.dest = kwargs.get('dest')
        message = f"File Path: {self.source}"
        try:
            return self.function(*params, **kwargs)
        except NotADirectoryError as error:
            self.logger.critical(f"Not ADirectory Error {message}")
            error.reason = "Not ADirectory Error"
            return error
        except FileNotFoundError as error:
            self.logger.critical(f"FileNot Found Error{message}")
            error.reason = "File Not Found Error"
            return error
        except PermissionError as error:
            self.logger.critical(f"Permission Error {message}")
            error.reason = "Permission Error"
            return error


def file_error(function):
    """
    file errors decorators function
    :param function:
    :return:
    """
    @functools.wraps(function)
    def wraps(*args, **kwargs):
        """
        wraps
        :param args:
        :param kwargs:
        :return:
        """

        try:
            return function(*args, **kwargs)
        except NotADirectoryError:
            print("Not ADirectory Error", file=sys.stderr)
            return "NotADirectoryError"
        except FileNotFoundError:
            print("File Not Found Error", file=sys.stderr)
            return "FileNotFoundError"
        except PermissionError:
            print("Permission Error", file=sys.stderr)
            return "PermissionError"

    return wraps
