import csv
from datetime import datetime
#Sub_ids is a dictinary which points every subscription Id to a list containing
#[Subsciption ID, Subscription Type,Duration,Date of First Trxn, Date of Last Trxn]

sub_ids={}
f=open('subscription_report.csv')
csv_f=csv.reader(f)
flag='True'
for row in csv_f:
    if flag=='True':      #Skipping Header Row         
        flag='False'
        continue
    if row[1] not in sub_ids:       #Adding new Subscription IDs
        sub_ids[row[1]]=[row[1],'one-off',1,row[3],row[3]]
        
    else:                           #If already added then add new Last Trxn Date
        
        a=datetime.strptime(row[3], "%m/%d/%Y")
        sub_ids[row[1]][4]= a
        b=datetime.strptime(sub_ids[row[1]][3], "%m/%d/%Y")
                                    #Calculating Subscription Type & duration.
        if (a-b).days > 360 and sub_ids[row[1]][1] != 'monthly':
            if sub_ids[row[1]][1]=='one-off':
                sub_ids[row[1]][1]= 'yearly'
            if sub_ids[row[1]][1]=='yearly':
                sub_ids[row[1]][2]+=1
                
        elif (a-b).days > 27 and sub_ids[row[1]][1] != 'daily':
            if sub_ids[row[1]][1]=='one-off':
                sub_ids[row[1]][1]= 'monthly'                
            if sub_ids[row[1]][1]=='monthly':
                sub_ids[row[1]][2]+=1
        elif (a-b).days >= 1:
            sub_ids[row[1]][1]= 'daily'
            sub_ids[row[1]][2]+=1 
     
for x in sub_ids:                   # Print out the list containing the RESULT :)
    print sub_ids[x][0:3]
print sub_ids['15447']
f.close()