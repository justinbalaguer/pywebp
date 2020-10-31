import os
import glob
import sys
import argparse
from PIL import Image

def main():
  parse_cmd_args(sys.argv[1:])
  cwd = os.getcwd()
  # ---------------------
  #       WINDOWS
  # ---------------------
  # JPG to Webp
  arrjpg = glob.glob(cwd+"/*.jpg")
  for arrpath in arrjpg:
    mainfile = arrpath.split("\\")
    filenameext = mainfile[-1] # gets the file name and extension
    filename = mainfile[-1].split(".")[0] # gets the filename
    img = Image.open(filenameext).convert("RGB")
    img.save(filename+".webp","webp")

  # PNG to Webp
  arrpng = glob.glob(cwd+"/*.png")
  for arrpath in arrpng:
    mainfile = arrpath.split("\\")
    filenameext = mainfile[-1] # gets the file name and extension
    filename = mainfile[-1].split(".")[0] # gets the filename
    img = Image.open(filenameext).convert("RGB")
    img.save(filename+".webp","webp")

def parse_cmd_args(cmd_args):
  parser = argparse.ArgumentParser(prog='pywebp', usage='%(prog)s')
  parser._positionals.title = 'commands'
  if len(cmd_args) > 0:
      parser.print_help()
      sys.exit(1)
if __name__ == '__main__':
  main()