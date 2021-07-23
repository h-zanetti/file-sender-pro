import sys, os

INTERP = "/home/wwagah/repositories/file-sender-pro/.venv/bin/python"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from file_sender.wsgi import application