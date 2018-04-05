#Project 6 - Fade
#
#Name: Jake Loveland
#Instructor: Brian Jones
#Section: 21
import sys
from math import *

def main():
   try:
      image = sys.argv[1]
      row = int(sys.argv[2])
      col = int(sys.argv[3])
      rad = int(sys.argv[4])
      puzzle = open(image,"r")
   except IndexError:
      print("Usage: python3 fade.py <image> <row> <column> <radius>")
      sys.exit()
   except:
      print("Unable to open {:s}".format(image))
      sys.exit()  
   output = open("fade.ppm", "w")
   output.write(puzzle.readline())
   dimensions = puzzle.readline() 
   output.write(dimensions)
   output.write(puzzle.readline())
   dimensions = dimensions.split()
   dimensions = [int(val) for val in dimensions]
   leftovers = []
   pixel_list = []
   i = 0
   j = 0
   for line in puzzle:
      pixel = []
      line_list = leftovers + line.split()
      leftovers = []
      line_list = groups_of_3(line_list)
      for pix in line_list:
         if len(pix) == 3:
            pixel = [int(val) for val in pix]
            distance = sqrt((j-col)**2 + (i-row)**2)
            if i < dimensions[0]:
               i += 1
            else:
               i = 0
               j += 1
            scale = (rad - distance)/rad
            if scale < .2:
               scale = .2
            for color in pixel:
               color *= scale
            output.write("{:d} {:d} {:d}\n".format(pixel[0],pixel[1],pixel[2]))
         else:
            leftovers = pix
   output.close()
   puzzle.close() 

def groups_of_3(values):
   result = []
   counter = 0
   for val in values:
      if counter % 3 == 0:
         result.append([])
      result[counter//3].append(values[counter])
      counter += 1
   return result

if __name__ == "__main__":
   main()

 

