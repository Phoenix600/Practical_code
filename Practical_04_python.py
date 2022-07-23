scores = input("[+]Enter the scores of the students ").split()

# converting the string scores list into int list 
for INDEX in range(0,len(scores)) :
    scores[INDEX] = int(scores[INDEX])

# Average scores 
Avg_score = float(sum(scores)/len(scores))
print("Average Marks : ",round(Avg_score,2))

scores.sort()
#print(scores)
print("Second Largest Score : ",scores[len(scores)-2])

for INDEX in range(0,len(scores)) :
    if scores[INDEX] > 100 :
        print("Value over 100 has been entered")
        break
    else :
        None

scores.sort(reverse=True)
#print(scores)
scores.pop()
scores.pop()

Avg_score = float(sum(scores)/len(scores))
print("Average Marks : ",round(Avg_score,2))


