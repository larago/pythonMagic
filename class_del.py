# encoding=utf8

from os.path import join

class FileObject(object):

    def __init__(self, filePath='', fileName='sample.txt'):
        self.file = open(join(filePath, fileName), 'r+')

    def __del__(self):
        self.file.close()
        del self.file

FileObject()