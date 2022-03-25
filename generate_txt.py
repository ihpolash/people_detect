from os import listdir
from os.path import isfile, join
import re
import sys

mypath = sys.argv[1]
file = sys.argv[2]
txt_name = sys.argv[3]

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

with open(file) as f:
    urls = f.read()
    links = re.findall('"((http)s?://.*?)"', urls)

with open(txt_name, 'w') as f:
  for url in links:
    for file_name in onlyfiles:
      if file_name in url[0]:
        print(url[0])
        f.write(url[0])
        f.write('\n')
