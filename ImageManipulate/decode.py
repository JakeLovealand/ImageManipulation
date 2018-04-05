#Project 6 - Decode
#
#Name: Jake Loveland
#Instructor: Brian Jones
#Section: 21

import sys

def main():
   try:
      image = sys.argv[1]
      puzzle = open(image,"r")
   except IndexError:
      print("Usage: python3 decode.py <image>")
      sys.exit()
   except:
      print("Unable to open {:s}".format(image))
      sys.exit()
   output = open("decode.ppm", "w")
   output.write(puzzle.readline())
   output.write(puzzle.readline())
   output.write(puzzle.readline())
   leftovers = []
   pixel_list = []
   for line in puzzle:
      pixel = []
      line_list = leftovers + line.split()
      leftovers = []
      line_list = groups_of_3(line_list)
      for pix in line_list:
         if len(pix) == 3:
            pixel = [int(val) for val in pix]
            #print(pixel)
            if pixel[0]*10<=255:
               pixel[0] *= 10
            pixel[1] = pixel[0]
            pixel[2] = pixel[0]
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


