#!/usr/bin/python

import sys
import os

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"t:c:",["tag_version=","current_version="])
   except getopt.GetoptError:
      print os.path.basename(__file__) + ' --tag_version <tag_version_number> --current_version <current_version_number>'
      sys.exit(2)
      
   tag_version=""
   current_version=""
   publish_command=""
   
   for opt, arg in opts:
      if opt in ("-t", "--tag_version"):
         tag_version = arg
      if opt in ("-c", "--current_version"):
         current_version = arg
         
   print tag_version
   print tag_version
   print "circleci orb publish packed.yml lbh-test/test-mvp@dev:${CIRCLE_BRANCH} --token ${CIRCLE_API_KEY}"
         
if __name__ == "__main__":
   main(sys.argv[1:])         
