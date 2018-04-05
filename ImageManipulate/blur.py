import sys
from math import *

def main():
   try:   
      image = sys.argv[1]
      pixels = ppm_to_list(image)
      pic = open(image,"r")
   except IndexError:
      print("Usage: python3 blur.py <image> [<reach>]")
      sys.exit()
   except:
      print("Unable to open {:s}".format(image))
      sys.exit()
   try:
      reach = int(sys.argv[2])
   except:
      reach =4
   output = open("blurred.ppm", "w")
   output.write(pic.readline())
   dimensions = pic.readline()
   output.write(dimensions)
   output.write(pic.readline())
   dimensions = dimensions.split()
   dimensions = [int(val) for val in dimensions]
   y = 0
   for row in pixels:
      x = 0
      for pix in row:
         new_pix = []
         r_sum = 0
         g_sum = 0
         b_sum = 0
         num = 0
         for j in range(-reach, reach+1):
            for i in range(-reach, reach+1):
               if(x + i >= 0 and y + j>= 0) and (x+i < dimensions[0] and y+j < dimensions[1]):
                  r_sum += pixels[y+j][x+i][0]
                  g_sum += pixels[y+j][x+i][1]
                  b_sum += pixels[y+j][x+i][2]
                  num += 1
         new_pix.append(int(r_sum/num))
         new_pix.append(int(g_sum/num))
         new_pix.append(int(b_sum/num))
         for color in new_pix:
            output.write("{:d} ".format(color))
         output.write("\n")
         x+=1
      y+=1
   output.close()

def ppm_to_list(image):
   my_pic = open(image,"r")
   file_list = []
   lin_num = 0
   for line in my_pic:
      line_list = line.split()
      if lin_num > 0:
         for val in line_list:
            file_list.append(int(val))
      lin_num += 1
   width = file_list[0]
   height = file_list[1]
   pixels = groups_of_3(file_list[3:])
   pixel_list = []
   k = 0
   for i in range(height):
      pixel_list.append([])
      for j in range(width):
         pixel_list[i].append(pixels[k])
         k += 1
   my_pic.close()
   return pixel_list

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
