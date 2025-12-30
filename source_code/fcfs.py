
#First come First served  python code well commented 

#first stage is reading the csv files and storing the processes 

#STEP 1 importing the csv module to read  the required  CSV files 

import csv 

# Mapping of choices to CSV file paths
csv_options = {
    1: "csv_test_files/FCFS_INPUTS/fcfs_input_1.csv",
    2: "csv_test_files/FCFS_INPUTS/fcfs_input_2.csv",
    3: "csv_test_files/FCFS_INPUTS/fcfs_input_3.csv",
    4: "csv_test_files/FCFS_INPUTS/fcfs_input_4.csv"
}

# MAIN LOOP - allow user to run multiple CSVs
while True:
    print("\nSelect a CSV file to run (1-4) or 0 to exit:")
    for opt in csv_options:
        print("Choice" , opt , ":" ,csv_options[opt])
    print("0: Exit program")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting program. Goodbye!")
            break
        elif choice in csv_options:
            csv_file = csv_options[choice]
        else:
            print("Invalid choice. Enter 0-4.")
            continue
    except ValueError:
        print("Please enter a valid integer.")
        continue

    #initializing processes list
    processes = [] 

    #opening the csv files to read the data 
    with open(csv_file, "r") as file:

        reader = csv.DictReader(file) #reading the csv as dictionary
        for row in reader:
            ProcessId = row["ProcessId"]
            Arrival_Time = int(row["Arrival_Time"])
            Burst_Time = int(row["Burst_Time"])
            
            #appending each process as a dictionary with processid,arrival and burst
            processes.append({
                "ProcessId": ProcessId,
                "Arrival_Time": Arrival_Time, #converting arrival time and burst time to interger 
                "Burst_Time": Burst_Time 
            })
            
    #printing the processes to check data is read correctly
    print("Input Processes:")
    print("************************************")

    for P in processes:
        print("Process ID:", P["ProcessId"])
        print("Arrival Time:", P["Arrival_Time"])
        print("Burst Time:", P["Burst_Time"])
        print("********************************")


    #STEP 2 CALCULATING THE STARTING TIME AND COMPLETION TIME 

    #sorting processes by arrival time
    processes.sort(key=lambda x: x["Arrival_Time"])

    #initialising the complition time 
    prev_compTime = 0

    #calculating starting time(ST) and complition time (CT) for each process
    for P in processes:
        #starting time is the max time between the prev_compTime and arrival time 
        P["start"]=max(prev_compTime,P["Arrival_Time"]) 

        #calculating completion time  which is sum of start time and burst time
        P["completion"] = P["start"] + P["Burst_Time"]

        #updating the complition time after each process finish
        prev_compTime=P["completion"]

    #STEP 3 CALCULATING TURN AROUND TIME(TAT) AND WAITING TIME(WT)

    #TAT = COMPLETION TIME - ARRIVAL TIME AND WT = TAT -  BURST_TIME
    for P in processes:
        P["TAT"] = P["completion"] - P["Arrival_Time"]
        P["WT"] = P["TAT"] - P["Burst_Time"]


    #STEP 4 CALCULATING AVERAGE TAT AND WT
    Total_TAT = 0
    Total_WT = 0
    n=len(processes) #total number of processes 

    for P in processes:
        Total_TAT += P["TAT"]
        Total_WT += P["WT"]

    Average_TAT = Total_TAT / n
    Average_WT = Total_WT / n     


    #printing the results
    print("--------------------------------------")
    print ("FCFS Scheduling Results for case:",choice)
    print("--------------------------------------") 

    for P in processes:
        print("Process ID:", P["ProcessId"])
        print("Arrival Time:", P["Arrival_Time"])
        print("Burst Time:", P["Burst_Time"])
        print("Start Time:", P["start"])
        print("Completion Time:", P["completion"])
        print("Turnaround Time(TAT):", P["TAT"])
        print("Waiting Time(WT):", P["WT"])
        print("------------------------------------")
                
    print("Average TAT and WT")
    print("------------------------------------------")
    print("Average Turnaround Time(TAT):",Average_TAT)
    print("Average Waiting Time(WT):", Average_WT)
    print("------------------------------------------")

    #STEP 5 GANTT CHART GENERATION
    print("\nGANTT CHART")
    print("=================")

    #printing processid in order 
    for P in processes:
        print("|" , P["ProcessId"] , end = " ")
    print("|")

    #printing time markers below
    time_marker = 0
    print(time_marker , end = " ")
    for P in processes:
        time_marker = P["completion"]

        spaces = 3 
        print(" " * spaces , time_marker, end="")
    print()    

    print("\n--------------------------------------------")
    print("FCFS run completed. You can select another CSV or exit.")
    print("--------------------------------------------\n")

