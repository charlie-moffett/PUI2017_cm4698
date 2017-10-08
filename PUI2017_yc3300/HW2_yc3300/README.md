# Assignment
## Assignment 1: tracking each vehicle for a lin
## Assignment 2: next stop information
## Assignmnet 3: Read CSV files with pandas

# Process:
## Assignment 1:Write a Python script to retrieve and report information about active vehicle for a bus line.
1. For this assignment, I opened bus data (with my APIKEY) using chrome. All the numbers and information were combined and messed up together with no sequences at all, rachel lim xin rong helped me find data location by opening data on her computer using firefox.
2. For assignment 1&2, I had little idea on how they should be done, I started of  with naming file with sys.argv but I didn't know what to half way. Rachel (Rachel Lim Xin Rong) helped me with writing code for assignment 1, I followed along what she said (for both assignment 1&2). 
3. Unisse Chua helped me with debugging some commands as some commads were recognized as invalid syntax.

## Assignment 2: Write a Python script that displays information on the next stop location of all busses of a given line.
1. Again, I used Rachel's computer to read data location for this assignment, at the same time, Unisse Chua introduced me to jsonformatter.org which organize Json data in a clearer format. 
2. I had trouble finding bus stop information, Rachel helped me with that, she also corrected my loop with corrected data locations. 
3. Due the similarity between assignment one and two, I copied and pasted some of the code for assignment 1 and added bus stop information as what Rachel told me.
4. I had problem with fout.write in the last step. As I ran fout.write() it kept showing errors, I tried print as well, Rachel corrected me as the print code prints wrong format. Gaurav Bhardwaj said that he has the same probelm and he helped me with erasing fout code, then added a "writer" code both before and in the loop, I followed along what he said and changed the fout.write to writer. 


## Assignment 3: Work on compute. Choose a dataset within the CUSP data facility (DF) that is available in CSV format. Chose one that has at least 2 numerical value columns.
1. I had trouble finding data in data catalog, Unisse Chua taught me instead of going to data catalog, I can just go to "Urban Profiler" and filter the chart with numbers.
2. This assignment is similar to the class example professor did, I individually opened CSV file uding DFDATA.
3. Unisse Chua helped me with correcting code for narrowing down the columns using df.drop 
4. I individually plotted the figure.
