import math
from models.PredictionParameters import PredictionParameters


class CovidPositiveCases:
    def __init__(self): 
        self.__prediction_parameters=PredictionParameters()
        self.__current_pos_cases=[]
    def set_current_pos_cases(self, path):
        try:
            f=open(path,'r')
            lines_list=f.readlines()
        except:
            raise Exception("InvalidFileError")
        for i in range(0, len(lines_list), 2):
            state=lines_list[i].strip()
            value=int(lines_list[i+1].strip())
            self.__current_pos_cases.append({"state":state,"pos_case":value})
    def set_prediction_parameters(self):
        while(1):
            try:
                no_of_days=int(input("Enter no. of days for the prediction:"))
                self.__prediction_parameters.set_no_of_days(no_of_days)
                break
            except:
                print("Please enter a valid no. of days.")        
        while(1):
            try:
                social_distance_compliance=float(input("Enter social distance compliance in (x)%:"))
                self.__prediction_parameters.set_social_distance_compliance(social_distance_compliance)
                break
            except:
                print("Please enter a valid percentage.")
        while(1):
            try:
                growth_rate=float(input("Enter growth rate in (x)%:"))
                self.__prediction_parameters.set_growth_rate(growth_rate)
                break
            except:
                print("Please enter a valid percentage.")

    def print_current_pos_cases(self):
        if (self.__current_pos_cases==[]):
            print("Please import datasource!")
        else:
            for i in self.__current_pos_cases:
                print(i.get("state"), end="\t")
            print("\n------------------------------------------------------------")
            for i in self.__current_pos_cases:
                print(i.get("pos_case"), end="\t")
            
    
    def print_predicted_positive_cases(self):
            total=0
            print(
                f"\nCOVID-19 POSITIVE RESULTS {self.__prediction_parameters.get_no_of_days()} DAY PREDICTIONS\n"
                f"GROWTH RATE: {self.__prediction_parameters.get_growth_rate()}\n"
                f"SOCIAL DISTANCING COMPLIANCE:{self.__prediction_parameters.get_social_distance_compliance()}%"
                )
            
            print("Day", end="\t")
            for i in self.__current_pos_cases:
                    print(i.get("state"), end="\t")
            print("Total")
            print("-----------------------------------------------------------------------------")
            for day in range (0, int(self.__prediction_parameters.get_no_of_days())+1):
                total=0
                print(day+1, end="\t")
                for i in self.__current_pos_cases:
                    j=float((self.__prediction_parameters.get_scaled_growth_rate()))
                    pos_case=float(i.get("pos_case"))*math.pow(j,day)
                    pos_case=round(pos_case)
                    total=total+pos_case
                    print(pos_case, end="\t")
                print(total)
                day=day+1
