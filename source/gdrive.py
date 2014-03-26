#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import dateutil.parser
import json

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

target_files = ["USER_A_POS-jtest.txt", "USER_B_POS-jtest.txt"]
save_path = "."

def auth():
  try:
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)
  except:
    print "Unexpected error:", sys.exc_info()[0]

def createSampleFile(authedDrive, file_name, content):
  drive = authedDrive
  file = drive.CreateFile({'title': file_name})
  file.SetContentString(content)
  try:
    file.Upload()
  except:
    print "Unexpected error:", sys.exc_info()[0]

def setSampleFile():
  for file_name in target_files:
    createSampleFile(drive, file_name, '{"latitude": 35.999999, "longitude": 139.999999}')

def sortByCreatedDate(file_list):
  items = []
  for file_meta in file_list:
    dt = dateutil.parser.parse(file_meta['createdDate'])
    items.append((dt, {'id':file_meta['id'], 'title':file_meta['title']}))
    #items.append((file_meta['createdDate'], {'id':file_meta['id'], 'title':file_meta['title']}))
    sorted(items, reverse=True)
  return items

def newestFile(items, file_name):
  for item in items:
      if item[1]['title'] == file_name:
        return item[1]['id']
  return None

def saveContent(file_obj, file_name):
  content = json.loads(file_obj.GetContentString())
  sketch_conversion_data = ','.join([file_name, str(content['latitude']), str(content['longitude'])])
  file_name = '/'.join([save_path, file_name])
  try:
    fp = open(file_name,'w')
    fp.write(sketch_conversion_data)
    fp.close()
  except:
    print "Unexpected error:", sys.exc_info()[0]
  # print content
  # print sketch_conversion_data

if __name__ == "__main__":

  drive = auth()
  # setSampleFile() # generating initial files for testing.

  # Auto-iterate through all files that matches this query
  file_list = drive.ListFile({'q': "trashed=false"}).GetList()

  items = sortByCreatedDate(file_list)

  if len(items) >= len(target_files):
    for file_name in target_files:
      try:
        file_obj = drive.CreateFile({'id':newestFile(items, file_name)})
        saveContent(file_obj, file_name)
      except:
        print "Unexpected error:", sys.exc_info()[0]
