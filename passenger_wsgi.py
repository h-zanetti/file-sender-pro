import sys, os

INTERP = "/home/wwagah/repositories/virtualenvs/file-sender/bin/python"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from file_sender.wsgi import application