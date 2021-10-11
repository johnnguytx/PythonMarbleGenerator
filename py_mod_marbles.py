#
# This file will define functions to be used in the main program
#  Johnny Nguyen
#  06/29/2021
#

# --- MODULE
import random

# --- MODULE VARIABLES
MIN_BAGS = 5
MAX_BAGS = 15
MIN_MARBLES = 180
MAX_MARBLES = 220
FILENAME = "MarbleReport.txt"

# --- FUNCTIONS
def displayMessage(msg):
  # PURPOSE: Displays a simple message
  # RETURNS: n/a
  # IN: msg, to be displayed
  # OUT: n/a
  print(msg)

def getNumBags():
  # PURPOSE: Prompts the user for a number of bags
  # RETURNS: bags, number of bags
  # IN: n/a
  # OUT: n/a
  bags = int(input("Enter a number of bags between 5 and 15: "))
  while bags < MIN_BAGS or bags > MAX_BAGS:
   bags = int(input("Please enter number of bags within the specified range: "))
  return bags

def table(bags):
  # PURPOSE: Controls generation of the table by calling other functions
  # RETURNS: n/a
  # IN: bags, number of bags
  # OUT: n/a
  colors = {
    "red": 0,
    "orange": 0,
    "yellow": 0,
    "green": 0,
    "blue": 0,
    "purple": 0,
    "total" : 0,
  }
  id = 1
  seed()
  f = open(FILENAME, "w")
  header(f)
  i = 0
  while i < bags:
    a = row(f,id)
    i += 1
    id += 1
    for x in a:
      num1 = a[x]
      num2 = colors[x]
      sum1 = num1 + num2
      colors[x] = sum1
  footer(f,colors)
  f.close

def seed():
  # PURPOSE: Seeds the random number generator
  # RETURNS: n/a
  # IN: n/a
  # OUT: n/a
  random.seed()

def header(f):
  # PURPOSE: displays the table header and writes it to the file
  # RETURNS: n/a
  # IN: n/a
  # OUT: n/a
  line = "{:>3}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}"
  print(line.format("BAG","RED","ORG","YEL","GRN","BLU","PPL","TOT"))
  print("---------------------------------------------")
  f.write(line.format("BAG","RED","ORG","YEL","GRN","BLU","PPL","TOT\n"))
  f.write("---------------------------------------------\n")

def row(f,id):
  # PURPOSE: displays a table row and writes it to the file
  # RETURNS: Returns a dictionary of bag color counts
  # IN: f, the output file, id the bag id
  # OUT: n/a
  colors = {"red": 0,"orange": 0,"yellow": 0,"green": 0,"blue": 0,"purple": 0}
  a = (rng(MIN_MARBLES,MAX_MARBLES))
  i = 0
  while i < a:
    num = random.choice(list(colors))
    colors[num] += 1
    i += 1
  total = colors["red"] + colors["orange"] + colors["yellow"] + colors["green"] + colors["blue"] + colors["purple"]
  line = "{:>3}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}"
  print(line.format(id,colors["red"],colors["orange"],colors["yellow"],colors["green"],colors["blue"],colors["purple"],total))
  f.write(line.format(id,colors["red"],colors["orange"],colors["yellow"],colors["green"],colors["blue"],colors["purple"],total))
  f.write("\n")
  return colors

  


def rng(lower, upper):
  # PURPOSE: generates a random number
  # RETURNS: a random number within given bounds
  # IN: upper, the upper bound, lower, the lower bound
  # OUT: n/a
  num = random.randint(lower, upper)
  return num

def footer(f,colors):
  # PURPOSE: Displays the table footer and writes it to the file
  # RETURNS: a random number within given bounds
  # IN: f, the output file, colors, a dictionary of total color counts, with color names (strings) as the keys and total color counts as the values
  # OUT: n/a
  tot = colors["red"] + colors["orange"] + colors["yellow"] + colors["green"] + colors["blue"] + colors["purple"]
  line = "{:>3}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}"
  print("---------------------------------------------")
  print(line.format("TOT",colors["red"],colors["orange"],colors["yellow"],colors["green"],colors["blue"],colors["purple"],tot))
  f.write("---------------------------------------------\n")
  f.write(line.format("TOT",colors["red"],colors["orange"],colors["yellow"],colors["green"],colors["blue"],colors["purple"],tot,"\n"))



