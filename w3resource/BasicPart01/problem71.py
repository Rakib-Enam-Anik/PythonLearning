"""Write a Python program to get a directory listing, sorted by creation date."""
import os
import time
paths = ["%s %s" % (time.ctime(t),f) for t, f in
sorted([(os.path.getctime(x),x) for x in os.listdir(".")])]
print("Directory listing, sorted by creation date:")
for x in range(len(paths)):
    print(paths[x],)