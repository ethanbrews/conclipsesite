from django.http import HttpResponseForbidden
from django.shortcuts import render
import os


def _in_directory(file, directory, allow_symlink=False):
    directory = os.path.abspath(directory)
    file = os.path.abspath(file)
    if not allow_symlink and os.path.islink(file):
        return False
    return os.path.commonprefix([file, directory]) == directory


def almost_static(request, slug):
    pages_root = 'pages'
    path = os.path.join(pages_root, slug+".html")
    if not _in_directory(path, pages_root):
        return HttpResponseForbidden()

    print(path)

    return render(request, path)


