#
# This program will randomly determine the number of different colored marbles within a user-defined number of bags
#  Johnny Nguyen
#  06/29/2021
#

# --- MODULE
import py_mod_marbles as mod

# --- MAIN PROGRAM
mod.displayMessage("This program will randomly determine the number of different colored marbles within a user-defined number of bags")
bags=(mod.getNumBags())
mod.table(bags)
mod.displayMessage("Program is now exiting. Goodbye!")