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

def list_to_ppm(list1,ppm_file):
   new_image = open(ppm_file,"w")
   new_image.write("P3\n")
   new_image.write("{:d} {:d}\n255\n".format(len(list1[0]),len(list1)))
   for i in range(len(list1)):
      for j in range(len(list1[0])):
         new_image.write("{:d} {:d} {:d}".format(list1[i][j][0],list1[i][j][1],list1[i][j][2]))
         new_image.write("\n")

 def groups_of_3(values):
   result = []
   counter = 0
   for val in values:
      if counter % 3 == 0:
         result.append([])
      result[counter//3].append(values[counter])
      counter += 1
   return result 

def read_pixel(count,filename):
   my_file = open(filename, "r")
   lin_num = 1
   i = 0
   pixel = []
   for line in my_file:
      if lin_num > 3:
         line_list = line.split()
         if i + len(line_list) > count:
            for num in line_list:
               if len(pixel) < 3:
                  pixel.append(int(num))
               else:
                  break;
         if len(pixel) >=3:
            break;
         i += len(line_list)
      lin_num += 1
   my_file.close()
   return pixel

def get_dimen(filename):
   my_file = open(filename, "r")
   lin_num = 1
   dimensions = []
   for line in my_file:
      if lin_num == 2:
         line_list = line.split()
         dimensions.append(int(line_list[0]))
         dimensions.append(int(line_list[1]))
         break
      lin_num += 1
   my_file.close()
   return dimensions
