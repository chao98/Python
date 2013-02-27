#!c:\Python33\python.exe -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++

  lnames = []
  d = {}

  match_year = r'>(Popularity in[\w\s]+)<'
  match_female = r'>(Female name)<'
  match_html = r'<td>([\w\d]*)</td>'

  f = open(filename, 'r')
  linesStr = f.readlines()
  f.close()

  find_year = False
  find_female = False
  find_last = False
  year = ''
  i = 0

  while i < len(linesStr):
      if not find_year:
          m = re.search(match_year, linesStr[i])
          if m:
              find_year = True
              year = (m.group(1).split())[2]

      elif not find_female:
          m = re.search(match_female, linesStr[i])
          if m:
              find_female = True

      elif find_female and (not find_last):
          linfo = re.findall(match_html, linesStr[i])

          if len(linfo) == 3:
              if linfo[0].isdigit() and int(linfo[0]) == 1000:
                  find_last = True

              d[linfo[1]] = linfo[0]
              d[linfo[2]] = linfo[0]
          else:
              print('Error syntax parse, please check program')
              sys.exit(1)
          
      i = i + 1

  if find_year: lnames.append(year)
  if find_female and find_last:
      for key in sorted(d):
          eachname = key + ' , ' + d[key]
          lnames.append(eachname)

  return lnames

def out_file(filename, outputl):
    '''
    f, file to be opened to print information into
    l, list of "list of information of that year"

    output format would be:
    year: 
    (xxx, nnn)    (yyy, nnn)    (zzz, nnn)...  
    '''
    f = open(filename, 'w')

    if len(outputl):
        for lnames in outputl:
            if not len(lnames):
                print('Error, no data to output')
                sys.exit(1)

            f.write(lnames[0])
            f.write(':')
            f.write('\n')
            del lnames[0]

            for eachname in lnames:
                f.write('(')
                f.write(eachname)
                f.write(')')
                f.write('    ')
            
            f.write('\n')

    f.close()
    return

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  outfile = ''
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  
  if len(args) >= 2:
    outfile = args[0]
    del args[0]
  else:
      print('Format error, please check')
      sys.exit(1)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  outl = []

  for f in args:
      outl.append(extract_names(f))

  out_file(outfile, outl)

  
''' main file begins '''
if __name__ == '__main__':
  main()

