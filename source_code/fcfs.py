#First come First served  python code well commented 

#first stage is reading the csv files and storing the processes 

#importing the csv module to read  the required  CSV files 
import csv 

processes = [] #a list to store all the processes 

#opening the csv files to read the data 
with open("csv_test_files/FCFS_INPUTS/fcfs_input_1.csv", "r") as file:

    reader = csv.DictReader(file) #reading the csv as dictionary
    for row in reader:
        #appending each process as a dictionary with prrocesid,arrival and burst
        processes.append({
            "pid": row["ProcessId"],
            "arrivalTime": int(row["Arrival_Time"]), #converting arrival time and burst time to interger
            "burstTime": int(row["Burst_Time"])
        })
        
#printing the processes to check data is read correctly
print(processes)       
