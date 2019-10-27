#!/usr/bin/python

import sys, os, getopt

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"t:c:",["tag_version=","current_version="])
   except getopt.GetoptError:
      print(os.path.basename(__file__) + ' --tag_version <tag_version_number> --current_version <current_version_number>')
      sys.exit(2)
      
   tag_version=""
   current_version=""
   publish_command=""
   
   for opt, arg in opts:
      if opt in ("-t", "--tag_version"):
         tag_version = arg
      if opt in ("-c", "--current_version"):
         current_version = arg

   try:
      current_tuple = get_version_tuple(current_version)
      tag_tuple = get_version_tuple(tag_version)
      current_tuple_major = current_tuple[0]
      current_tuple_minor = current_tuple[1]
      current_tuple_patch = current_tuple[2]
      tag_tuple_major = tag_tuple[0]
      tag_tuple_minor = tag_tuple[1]
      tag_tuple_patch = tag_tuple[2]

      if current_tuple < tag_tuple:
         if tag_tuple_major > current_tuple_major and tag_tuple_major <= current_tuple_major+1 and tag_tuple_minor == 0 and tag_tuple_patch==0:
               print("major")
         elif tag_tuple_minor > current_tuple_minor and tag_tuple_minor <= current_tuple_minor+1 and tag_tuple_major == current_tuple_major and tag_tuple_patch==0:
               print("minor")
         elif tag_tuple_patch > current_tuple_patch and tag_tuple_patch <= current_tuple_patch+1 and tag_tuple_major == current_tuple_major and tag_tuple_minor == current_tuple_minor:
            print("patch")
         else:
            print("print 'Error: tag_version={} is not a valid increment of the current_version={}'".format(tag_version, current_version))
      else:
         print("print 'Error: tag_version={} is not greater than current_version={}'".format(tag_version, current_version))
         sys.exit(1)
   except ValueError:
      print("print 'Error: Invalid arguments --tag_version={} --current_version={} Both values require a semantic version. Please see https://semver.org for information'".format(tag_version, current_version))
      sys.exit(2)
def get_version_tuple(version):
    return tuple(map(int, (version.split("."))))

if __name__ == "__main__":
   main(sys.argv[1:])         
