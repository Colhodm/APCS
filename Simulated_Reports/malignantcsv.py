import numpy as np
import sys
from random import randint
import random
# Import the CSV module
import csv
counter = 0
benigncounter = 0
malignantidentifier = "Malignant"
benignidentifier = "Benign"
basicnames = "diagnosis"
numberofclusters = input('How many clusters do you want to create ')
numberofrecords = input('How many records per cluster ')
sizeoftestingset= input("How many records do you want in your testing set")
randomarray = [0] * sizeoftestingset
linecounter = -1
generalcounter = 0

# The input and output file names. You should change this to fit your needs.
#input_filename = "Real Random Shuffled 10,000 - Sheet1.csv"
#input_#filename = "ALLREALBENIGN - TrainingSET.csv.csv"
#input_filename = "Markov-Malign-Final.csv - Markov-Malign-Final.csv.csv"
#input_filename = "MalignRNNShuffled.csv - MalignRNN.csv.csv"
input_filename = "AllRealMalignantsBirads.csv"


for x in xrange(numberofclusters):
  output_filename = "REALPLUSREAL25%" + str(x) + ".csv"
  output_filenameother = "REALPLUSREAL50TESTING%" + str(x) + ".csv"



# Open the input file in read mode.
  input_file = open(input_filename, "r")

# Open the output file in write mode. make w a to append instead of just writing a new file
  output_file = open(output_filename, "a")
  output_fileother = open(output_filenameother, "a")


# Once the files are open, we use the CSV module to help us read it.
  input_reader = csv.reader(input_file)

# Skip the first line of the CSV file because it's the header, which we don't need
#  input_reader.next()
  for x in xrange(sizeoftestingset):
      randomarray[x] = random.randint(2, 217)
# Use a for loop to iterate through each remaining rows
  for input_line in input_reader:
      linecounter = linecounter + 1
      if(linecounter == 0):
            output_line = input_line[0] + "," + input_line[1] + "," + input_line[2] + "," + input_line[3] + "," + \
              input_line[4] + "," + input_line[5] + "," + input_line[6] + "," + input_line[7] + "," + \
              input_line[8] + "," + input_line[9] + "," + input_line[10] + "," + input_line[11] + "," + \
              input_line[12] + "," + input_line[13] + "," + input_line[14] + "," + input_line[
                  15] + "," + input_line[16] + "," + input_line[17] + "," + input_line[18] + "," + \
              input_line[19] + "," + input_line[20] + "," + input_line[21] + "," + input_line[
                  22] + "," + input_line[23] + "," + input_line[24] + "," + input_line[25] + "," + \
              input_line[26] + "," + input_line[27] + "," + input_line[28] + "," + input_line[
                  29] + "," + input_line[30] + "," + input_line[31] + "," + input_line[32] + "," + \
              input_line[33] + "," + input_line[34] + "," + input_line[35] + "," + input_line[
                  36]
            output_fileother.write(output_line + '\n')
            output_file.write(output_line + '\n')

      else:
      #for y in range(sizeoftestingset):
            if(randomarray[0] == linecounter or randomarray[1] == linecounter or randomarray[2] == linecounter or randomarray[3] == linecounter or randomarray[4] == linecounter or randomarray[5] == linecounter or randomarray[6] == linecounter or randomarray[7] == linecounter or randomarray[8] == linecounter or randomarray[9] == linecounter):
               # print(randomarray[y])
                print(" I AM ON THE " + str(generalcounter))
                print( " I AM ON THE") + str(counter)
                print(" THE LINE COUNTER IS") + str(linecounter)
                output_line = input_line[0] + "," + input_line[1] + "," + input_line[2] + "," + input_line[3] + "," + \
                              input_line[4] + "," + input_line[5] + "," + input_line[6] + "," + input_line[7] + "," + \
                              input_line[8] + "," + input_line[9] + "," + input_line[10] + "," + input_line[11] + "," + \
                              input_line[12] + "," + input_line[13] + "," + input_line[14] + "," + input_line[
                                  15] + "," + input_line[16] + "," + input_line[17] + "," + input_line[18] + "," + \
                              input_line[19] + "," + input_line[20] + "," + input_line[21] + "," + input_line[
                                  22] + "," + input_line[23] + "," + input_line[24] + "," + input_line[25] + "," + \
                              input_line[26] + "," + input_line[27] + "," + input_line[28] + "," + input_line[
                                  29] + "," + input_line[30] + "," + input_line[31] + "," + input_line[32] + "," + \
                              input_line[33] + "," + input_line[34] + "," + input_line[35] + "," + input_line[
                                  36]
                output_fileother.write(output_line + '\n')
                print(output_line)




            else:
                if(input_line[0] == malignantidentifier and counter < numberofrecords):
                    output_line = input_line[0] + "," + input_line[1] + "," + input_line[2] + "," + input_line[3] + "," + input_line[4] + "," + input_line[5] + "," + input_line[6] + "," + input_line[7] + "," + input_line[8] + "," + input_line[9] + "," + input_line[10] + "," + input_line[11] + "," + input_line[12] + "," + input_line[13] + "," + input_line[14] + "," + input_line[15] + "," + input_line[16] + "," + input_line[17] + "," + input_line[18] + "," + input_line[19] + "," +  input_line[20] + "," + input_line[21] + "," +  input_line[22] + "," + input_line[23] + ","  +  input_line[24] + "," + input_line[25] + "," + input_line[26] + "," + input_line[27]+ "," + input_line[28]+ "," +  input_line[29] + "," + input_line[30] + ","  +  input_line[31] + "," + input_line[32] + "," + input_line[33] + "," + input_line[34]+ "," + input_line[35]+ "," +  input_line[36]
                    output_file.write(output_line + '\n')

                    counter = counter + 1
                    print("ARJUN IS HERE")

               # if(input_line[0] == benignidentifier and benigncounter < numberofrecords/2):

                #    output_line = input_line[0] + "," + input_line[1] + "," + input_line[2] + "," + input_line[3] + "," + input_line[4] + "," + input_line[5] + "," + input_line[6] + "," + input_line[7] + "," + input_line[8] + "," + input_line[9] + "," + input_line[10] + "," + input_line[11] + "," + input_line[12] + "," + input_line[13] + "," + input_line[14] + "," + input_line[15] + "," + input_line[16] + "," + input_line[17] + "," + input_line[18] + "," + input_line[19] + "," +  input_line[20] + "," + input_line[21] + "," +  input_line[22] + "," + input_line[23] + ","  +  input_line[24] + "," + input_line[25] + "," + input_line[26] + "," + input_line[27]+ "," + input_line[28]+ "," +  input_line[29] + "," + input_line[30] + ","  +  input_line[31] + "," + input_line[32] + "," + input_line[33] + "," + input_line[34]+ "," + input_line[35]+ "," +  input_line[36] + "," + input_line[37] + ","  +  input_line[38] + "," + input_line[39] + "," + input_line[40] + "," + input_line[41]
                 #   output_file.write(output_line + '\n')
                  #  benigncounter = benigncounter + 1



                        # Write to our output file. We add a newline character (\n) at the end so each
                    # row will be on a different line
# Close the files after we're done with them so other programs can use them.
  if(counter == numberofrecords):
    output_file.close()
    generalcounter = generalcounter + 1
    print("done")

    counter = 0
    benigncounter = 0
    linecounter = -1

if(generalcounter == numberofclusters):
    input_file.close()
    sys.exit()
