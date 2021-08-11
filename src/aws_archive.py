import boto3
import os
import glob
import datetime

pictures = os.path.join('C:', os.sep, 'Users', 'jbuck', 'Pictures', 'Photos', '*.*')
print(pictures)

stuff = glob.glob(pictures)
print(stuff)
for s in stuff:
    dt = datetime.datetime.fromtimestamp(os.stat(s).st_mtime)
    print(dt.strftime('%Y-%m-%d %H:%M:%S'))
