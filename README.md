# HRYString_Reader
A python tool to read HRY string, extract failing bits and return associated failing partitions


Use Cases:

This script can be used to identify which partitions are failing using a HRY string and the corresponding .json file. 

Using the HRY output from a test instance given in the following format: 
![image](https://github.com/cathalba/HRYString_Reader/assets/107694612/f56b2f85-6b5f-401c-99b4-0de8fb9883f3)

![image](https://github.com/cathalba/HRYString_Reader/assets/107694612/e1410e5a-0b28-477b-9dec-4bf7af0e77a2)

And the corresponding HRY.json file for the test instance: 

![image](https://github.com/cathalba/HRYString_Reader/assets/107694612/0ed9ca2b-c4ff-40dc-b7ad-8430a66d9f2d)

The script will return "partitions to ignore":

![image](https://github.com/cathalba/HRYString_Reader/assets/107694612/570c4df1-2e36-4db6-a063-aaeacf27976f)



