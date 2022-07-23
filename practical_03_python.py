# Write main code here 
string_sample = input("[+]Enter the string : ")
# Check point-01 :
print(f"Total number of characters in string is {len(string_sample)}")
# check point-02 :
print(string_sample*10)
# check point-03 :
print(string_sample[0])
# check point-04 :
print(string_sample[:3])
# check point-05 :
print(string_sample[len(string_sample)-3:])
# check point-06 :
print(string_sample[::-1])
# check point-07 :
if len(string_sample) >= int(7) :
    print(string_sample[6])
else :
    print("String is not long enough")
# check point-08 :
string_new_sample = string_sample[1:len(string_sample)-2]
# check point-09 :
string_sample_caps = string_sample.upper()
print(string_sample_caps)
# check point-10 
replace_string = string_sample.replace('a','e')
print(replace_string)

