#!/usr/bin/python3

import subprocess

# This short script illustrates a clean way to capture the output of a shell
# subprocess command AND the return code. The output will not be formatted 
# properly unless it is decoded. Note the ".decode('ascii')" below.

# Google Search: "subprocess.popen.communicate newline"
# https://stackoverflow.com/questions/15374211/why-does-popen-communicate-return-bhi-n-instead-of-hi

# Google Search: "python subprocess get output and return code"
# https://stackoverflow.com/questions/30937829/how-to-get-both-return-code-and-output-from-subprocess-in-python

import subprocess

diff_area_1="testDIr/section1Dir/"
diff_area_2="testDIr/section2Dir/"

command = "diff -r --brief " + diff_area_1 + " " + diff_area_2
print("Executing in shell: " + command)
out = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)

output = out.communicate()[0].decode('ascii')
returncode = out.returncode

print(output)
print("Return Code: " + str(returncode))

# In fact, this can be packaged nicely into a function:
def elegant_shell_execute(command):
    print("Executing in shell: " + command)
    out = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    output = out.communicate()[0].decode('ascii')
    returncode = out.returncode
    print(output)
    print("Return Code: " + str(returncode))
    print("")
    pass

command = "ls -l /path/to/some/symlink"

elegant_shell_execute(command)
