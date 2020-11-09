import os, os.path
import glob
import sys
import argparse
from PIL import Image
from os import path

def main():
  parse_cmd_args(sys.argv[1:])
  cwd = os.getcwd()
  # ---------------------
  #       FOLDER
  # ---------------------
  dir_name = 'converted'
  if path.exists(dir_name):
    print('Directory already exists...\nProceeding...')
  else:
    os.mkdir(dir_name)
    print('Converted directory created...')
  # ---------------------
  #       WINDOWS
  # ---------------------
  print('Converting...\nPlease wait...')
  # JPG to Webp
  arrjpg = glob.glob(cwd+'/*.jpg')
  for arrpath in arrjpg:
    if '\\' in arrpath:
      mainfile = arrpath.split('\\')
    elif '/' in arrpath:
      mainfile = arrpath.split('/')
    filenameext = mainfile[-1] # gets the file name and extension
    filename = mainfile[-1].split('.')[0] # gets the filename
    img = Image.open(filenameext).convert('RGB')
    os.chdir(dir_name)
    img.save(filename+'.webp','webp')
    # Go back to main directory
    os.chdir('../')

  # PNG to Webp
  arrpng = glob.glob(cwd+'/*.png')
  for arrpath in arrpng:
    if '\\' in arrpath:
      mainfile = arrpath.split('\\')
    elif '/' in arrpath:
      mainfile = arrpath.split('/')
    filenameext = mainfile[-1] # gets the file name and extension
    filename = mainfile[-1].split('.')[0] # gets the filename
    img = Image.open(filenameext).convert('RGB')
    os.chdir(dir_name)
    img.save(filename+'.webp','webp')
    # Go back to main directory
    os.chdir('../')

  # Open the converted files folder
  print('Opening folder')
  os.system('explorer.exe .')

def parse_cmd_args(cmd_args):
  parser = argparse.ArgumentParser(prog='pywebp', usage='%(prog)s')
  parser._positionals.title = 'commands'
  if len(cmd_args) > 0:
      parser.print_help()
      sys.exit(1)
if __name__ == '__main__':
  main()