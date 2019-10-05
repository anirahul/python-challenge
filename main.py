# Modules
import os
import csv

count_voters = 0
count_cand = 0
volume_counter = 0
temp_percentage = 0
highest_vote = 0
i=0
j=0
k=0
all_candidate_name = []
candidate_name = []
all_volume = []
all_percentage = []
all_final = []
#all_final2 = []
def key_index(emp):
    return emp[2]

# read the election file
pypoll_in = os.path.join("/Users/anirbanmukherjee/Documents/UNC Homeworks/HW_10052019", "election_data1.csv")

#count all votes 
with open(pypoll_in, newline='') as pypoll:
    pypoll_reader = csv.reader(pypoll, delimiter =',')
    pypoll = next(pypoll_reader)

    for row in pypoll_reader:
        count_voters = count_voters + 1   
        all_candidate_name.append(row[2])
        
#unique list of candidates
candidate_name = list(set(all_candidate_name))

# count of candidates
for row in candidate_name:
    count_cand = count_cand + 1

#print(all_candidate_name)


#volume of votes received by candidates
while (i < count_cand): 
    for row in all_candidate_name:
        #print(row[0])
        if candidate_name[i] == row:    
            volume_counter = volume_counter+1
    all_volume.append(volume_counter)
    #print(volume_counter)
    volume_counter = 0
    i = i+1

highest_name = candidate_name[0]
highest_vote = all_volume[0]


#determine highest voted and % of votes received
while (j < count_cand): 
    if highest_vote < all_volume[j]:
        highest_name = candidate_name[j]
        highest_vote = all_volume[j]

    temp_percentage =round((all_volume[j]/count_voters)*100,3)
    all_percentage.append(temp_percentage)
    j= j+1

#sort by highest voted
all_final_int = zip(candidate_name,all_volume,all_percentage)

all_final = list(all_final_int)

all_final.sort(key=key_index, reverse=True)

#print to output
print("Election Results")
print("--------------------------------------")
print("Total Votes:  " + str(count_voters))
print("--------------------------------------")
for row in all_final:
    print(row[0] + ":   " + str(row[2]) + "00%   ("+ str(row[1])+")")

print("--------------------------------------")
print("Winner:  " + highest_name)
print("--------------------------------------")


#write report
pypoll_out = os.path.join("/Users/anirbanmukherjee/Documents/UNC Homeworks/HW_10052019/python-challenge-master/PyPoll", "election_data_out.txt")
with open(pypoll_out, 'w', newline='') as csvfilewrite:
    writer = csv.writer(csvfilewrite)
    writer.writerow(["Election Results"])
    writer.writerow(["--------------------------------------"])
    writer.writerow(["Total Votes:  " + str(count_voters)])
    writer.writerow(["--------------------------------------"])
    for row in all_final:
        writer.writerow([row[0] + ":   " + str(row[2]) + "00%   ("+ str(row[1])+")"])
    writer.writerow(["--------------------------------------"])
    writer.writerow(["Winner:  " + highest_name])
    writer.writerow(["--------------------------------------"])
    





#print(count_voters)
#print(list(set(all_candidate_name)))
# print(candidate_name)
# print(count_cand)
# print(all_volume)
# print(all_percentage)
# print(highest_name)
#print(all_final)
# while (k < count_cand): 
#     print(all_final[k] + ":   " + str(all_percentage[k]) + "   ("+ str(all_volume[k])+")")
#     k= k+1
# print("Total:  " + "$"+str(profit))
# print("Average  Change:  " + "$"+str(average_change))
# print("Greatest Increase in Profits: " + great_inc_month + "  $("+str(great_inc)+")")
# print("Greatest Decrease in Profits: " + great_dec_month + "  $("+str(great_dec)+")")

#write report
# pybank_out = os.path.join("/Users/anirbanmukherjee/Documents/UNC Homeworks/HW_10052019", "budget_data_out.txt")
# with open(pybank_out, 'w', newline='') as csvfilewrite:
#     writer = csv.writer(csvfilewrite)
#     writer.writerow("Election Results")
#     writer.writerow(["--------------------------------------"])
#     writer.writerow(["Total Votes:  " + str(count_voters)])
    # writer.writerow(["Total:  " + "$"+str(profit)])
    # writer.writerow(["Average  Change:  " + "$"+str(average_change)])
    # writer.writerow(["Greatest Increase in Profits: " + great_inc_month + "  $("+str(great_inc)+")"])
    # writer.writerow(["Greatest Decrease in Profits: " + great_dec_month + "  $("+str(great_dec)+")"])
