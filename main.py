
import sys
import os
from models.ConsoleFileWriter import FileConsoleWriter
from models.CovidPositiveCases import CovidPositiveCases
from dotenv import load_dotenv

load_dotenv()
covidcases=CovidPositiveCases()


try:
   
    covidcases.set_current_pos_cases(os.getenv('datasourcefilepath'))

except:
    print("Please use correct path for file")

while(True):
    print(
    "\n=======================================================\n"
    "Prediction of COVID-19 Positive Cases\n"
    "=======================================================\n"
    "<1> List current positive cases\n"
    "<2> Insert prediction parameters\n"
    "<3> List predicted positive cases\n"
    "<4> Quit"
    )
    while(1):
        try:
            n=int(input(("Please select an option from the above:")))
            break
        except ValueError:
            print("Please enter integer from 1 to 4.")
            
    if (n==1):
        covidcases.print_current_pos_cases()
    elif (n==2):
       covidcases.set_prediction_parameters()
    elif (n==3):
        count=None
        try:
            with open(os.getenv('reportcountfilepath'), 'r') as count_file:
                count = int(count_file.read())
        except FileNotFoundError:
            with open(os.getenv('reportcountfilepath'), "w") as count_file:
                count = 0
                count_file.write(str(count))
        while(1):
            with open(f'{os.getenv("reportlocation")}/report_{count+1}.txt', 'w') as file:
                count=count+1
                original_stdout = sys.stdout
                sys.stdout = FileConsoleWriter(original_stdout, file)
                covidcases.print_predicted_positive_cases()
                with open(os.getenv('reportcountfilepath'), "w") as count_file:
                   count_file.write(str(count))
                sys.stdout=original_stdout
            print(
                "Want to rerun:\n"
                "Rerun(Anykey)\n"
                "Quit(Q)"
                )
            x=input()
            if(x=="Q" or x=="q"):
                break
            else:
                covidcases.set_prediction_parameters()
    
    elif (n==4):
        exit
    else:
        print("Enter valid choice!!")