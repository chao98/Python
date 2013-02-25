#!c:\Python33\python.exe -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def strip_sign(s):
  sign = ',\:;\"?!.)\'`\(\-\[\]\_1234567890\*'

  while len(s) >= 1 and s[0] in sign:
    s = s[1:]

  while len(s) >= 1 and s[-1] in sign:
    s = s[:-1]

  return s

def format_print_d(d):
  rjust_width = len(str(sorted(d.values(), reverse = True)[0])) + 1
  ljust_width = len(sorted(d.keys(), key = len, reverse = True)[0]) + 1
  num_per_line = 2

  i = 1
  for key in sorted(d, key = str.lower):
    value = str(d[key]).rjust(rjust_width)
    line = (key.ljust(ljust_width) + ': ' + value)

    if i < num_per_line:
      print(line, end = '\t')
      i = i + 1
    else:
      print(line)
      i = 1

  return

def print_words(filename):
  fileopened = open(filename, 'r')
  word_count = {}

  for line in fileopened:
    words = line.split()
    
    for word in words:
      word = strip_sign(word)

      if word in word_count:
        word_count[word] = word_count[word] + 1
      elif len(word) >= 1:
        word_count[word] = 1

  fileopened.close()

  format_print_d(word_count)

  return

def sort_dict_value(d):

  l_tuple = [(k, d[k]) for k in sorted(d, key = d.get, reverse = True)]

  return l_tuple

def format_print_l(l, n):
  l = l[:n]

  rj_wdt = len(sorted([str(value) for key, value in l], key = len, reverse = True)[0]) + 1
  lj_wdt = len(sorted([key for key, value in l], key = len, reverse = True)[0]) + 1
  np_line = 2
  i = 0

  for item in l:
    v = str(item[1]).rjust(rj_wdt)
    line = (item[0].ljust(lj_wdt) + ': ' + v)

    if i < np_line:
      print(line, end = '\t')
      i = i + 1
    else:
      print(line)
      i = 0

  return

def print_top(filename):
  f = open(filename, 'r')
  w_cnt = {}

  for line in f:
    words = line.split()

    for w in words:
      w = strip_sign(w)
      w = w.lower()

      if w in w_cnt:
        w_cnt[w] = w_cnt[w] + 1
      elif len(w) >= 1:
        w_cnt[w] = 1

  f.close()

  data_tb_show = 20
  format_print_l(sort_dict_value(w_cnt), data_tb_show)

  return

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
