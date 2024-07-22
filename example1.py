"""

Examples of using the CatchFilesErrors decorator


"""
import logging
import os
import pathlib
import shutil
from catchit import CatchFilesErrors, file_error


class AFile:

    def __init__(self, file_path):
        self.file_path = pathlib.Path(file_path)

        self.logger = logging.getLogger("files")
        self.logger.setLevel(logging.DEBUG)
        logger_file = logging.FileHandler(filename=f"{pathlib.Path.cwd()}/logs.log")
        self.logger.addHandler(logger_file)
        self.logger.propagate = False
        self.logger.info("created")

    @CatchFilesErrors
    def __content(self, **kwargs):
        content = open(self.file_path.as_posix()).readlines()
        return content

    @CatchFilesErrors
    def __copy(self, des, **kwargs):
        shutil.copy(self.file_path.as_posix(), des)

    @CatchFilesErrors
    def __rename(self, new_name, **kwargs):
        self.file_path.rename(new_name)

    def content(self):
        return self.__content(self, logger=self.logger, path=self.file_path.as_posix())

    def copy(self, des='./'):
        return self.__copy(self, logger=self.logger, path=self.file_path.as_posix(), des=des)

    def rename(self, new_name):
        return self.__rename(self, logger=self.logger, path=self.file_path.as_posix(), new_name=new_name)


@file_error
def my_read(path):
    """
    My read
    :param path:
    :return:
    """
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


@file_error
def my_write(path):
    """
    My write
    :param path:
    :return:
    """
    file = open(path, mode="w")
    file.write("test")
    file.close()
    return


@file_error
def my_copy(source, dest):
    """
    My Copy
    :param source:
    :param dest:
    :return:
    """
    # os.listdir(source)
    shutil.copy(source, dest)
