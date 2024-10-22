#DynamicCSVFileCreateEx1.py
import csv
noc=int(input("Enter How Many Columns u Have:"))
if(noc<=0):
    print("Invalid Number of Columns:")
else:
    colnames=[]
    for i in range(1,noc+1):
        colname=input("Enter {} Col Name:".format(i))
        colnames.append(colname)
    else:
        nor=int(input("Enter How Many Records u Have:"))
        if(nor<=0):
            print("{} is invalid Number of Records".format(nor))
        else:
            records=[] # for placing all records (Outer List)
            for i in range(1,nor+1):
                print("Enter {} Record Values:".format(i))
                print("------------------------------------")
                record=[] # for placing record values (Inner List)
                for j in range(len(colnames)):
                    colval=input("Enter Value for {}:".format(colnames[j]))
                    record.append(colval)
                else:
                    records.append(record)
            else:
                #accept the CSV File Name
                while(True):
                    csvfilename=input("Enter CSV File Name with extension .csv")
                    if( csvfilename.endswith(".csv")):
                        break
                    print("Invalid File Name-try again")
                with open("C:\\PYTHON-Apps\\"+csvfilename,"a") as fp:
                     csvwr=csv.writer(fp)
                     csvwr.writerow(colnames)
                     csvwr.writerows(records)
                     print("CSV File Created Dynamically--Verify")






