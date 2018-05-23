#!/usr/bin/python3

import argparse
import datetime
import os
import subprocess
import sys

################################################################################
# global variables
################################################################################
big_tmp_dir_area = "/path/to/tmp/dir"
debug_banner = "DEBUG: "
tmp_dir_counter_file = "/path/to/tmp/dir/counter.txt"


################################################################################
# sanity check applicable global variables
################################################################################
if not os.path.isdir(big_tmp_dir_area):
    print(big_tmp_dir_area + " is not a directory", file=sys.stderr)
    sys.exit(1)
if not os.path.exists(tmp_dir_counter_file):
    print(tmp_dir_counter_file + ": file doesn't exist", file=sys.stderr)
    sys.exit(1)

################################################################################
# get user name
################################################################################
username = os.popen('whoami').read()
# http://www.4answered.com/questions/view/d1fec/whoami-in-python
username = username.rstrip()

################################################################################
# get options
################################################################################
parser = argparse.ArgumentParser(
    description="This script will automatically create a tmp directory in: " +
    big_tmp_dir_area,
    formatter_class=argparse.RawTextHelpFormatter,
    epilog=__file__ + ' -m "enter a description for the tmp dir here"'
    )
parser.add_argument("-d", "--debug", action="store_true", help="run in debug "
    "mode")
parser.add_argument("-m", "--message", action="store", help="a description for "
    "the tmp dir", required=True)
args = parser.parse_args()


if args.debug:
    print(debug_banner + "Message: " + args.message)

################################################################################
# read tmpdircounter.txt
################################################################################
with open(tmp_dir_counter_file, 'r') as f:
    tmp_dir_counter_str = f.readline()
    f.close

# chomp
tmp_dir_counter_str = tmp_dir_counter_str.rstrip()

if args.debug:
    print(debug_banner + "Counter: " + str(tmp_dir_counter_str))

################################################################################
# get the next number in tmpdircounter.txt ; save it for later
################################################################################
tmp_dir_counter_int = int(tmp_dir_counter_str)
if args.debug:
    print(debug_banner + "tmp dir counter int: " + str(tmp_dir_counter_int))
new_tmp_dir_counter_int = tmp_dir_counter_int + 1
if args.debug:
    print(debug_banner + "new tmp dir counter int: " +
        str(new_tmp_dir_counter_int) )

tmp_dir_pathname = big_tmp_dir_area + "/tmp" + tmp_dir_counter_str

# exit if counter is over 9000!!! (9999 to be exact)
if tmp_dir_counter_int > 9999:
    print("Not going to make: " + tmp_dir_pathname)
    print("Counter is exceeding four digits 9999.")
    print("Please reset counter manually back to 0000.")
    print("Counter File: " + tmp_dir_counter_file)
    print("Exiting now with 0 status code.")
    sys.exit(0)

# mkdir
print("Making tmp dir: " + tmp_dir_pathname)
os.mkdir(tmp_dir_pathname)
os.chmod(tmp_dir_pathname, 0o777)

# update tmpdircounter.txt
# http://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file-in-python
# pad with zeroes so that counter always has four digits
# http://stackoverflow.com/questions/339007/nicest-way-to-pad-zeroes-to-string
with open(tmp_dir_counter_file, 'w') as f:
    print('{0:04d}'.format(new_tmp_dir_counter_int), file=f)
    f.close

# create readme.txt with date and message
readme_file = tmp_dir_pathname + '/tmp_readme.txt'
with open(readme_file, 'w') as f:
    time_stamp = datetime.datetime.now().strftime("%a %b %e %l:%M:%S %Z %Y")
    print(time_stamp, file=f)
    print(args.message, file=f)
    print("This tmp dir: " + tmp_dir_pathname, file=f)
    f.close

# make readme.txt writable by everyone:
os.chmod(readme_file, 0o666)

if args.debug:
    print(debug_banner + "readme: " + readme_file)

################################################################################
# create INSTALLATION, EXTRACTHERE, and DOWNLOAD_DIR sub-directories
################################################################################
os.mkdir(tmp_dir_pathname + '/INSTALLATION')
os.mkdir(tmp_dir_pathname + '/EXTRACTHERE')
os.mkdir(tmp_dir_pathname + '/DOWNLOAD_DIR')

sys.exit(0)

# add to github best practices notes: standardized way of printing to std err
# add to github best practices notes: standardized way of doing argparse
# add to github best practices notes: python kind of already does a lot of
#     sanity testing of files and directories.
