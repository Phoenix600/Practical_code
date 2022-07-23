# write main code here 
sample_set1 = {"Yellow","Orange","Black","Blue"}
sample_set2  = {"Blue","Green","Red","Black"}
print("Sample_set1       :   ",sample_set1)
print("Sample_set2       :   ",sample_set2)
# check-point 1 :
#identical_set = sample_set1 | sample_set2
identical_set = sample_set1.union(sample_set2)
print(f"Identical Set      :   {identical_set}")
# check point 2 :
intersection_set = sample_set1 & sample_set2
print(f"Intersection Set    :   {intersection_set}")
# check point 3 :
sample_set1.discard("Yellow")
# check point 4 :
new_set     = (sample_set1 - sample_set2) | (sample_set2 - sample_set1)
print(f"{new_set}")
# check point 5 :
sample_set1.update(sample_set2 - sample_set2,sample_set1)
print("Updated sample_set1  :   ",sample_set1)
# check point 6 :
Data = dict()
for key in sample_set1 :
    for value in sample_set2 :
        Data[key] = value
print(Data)
