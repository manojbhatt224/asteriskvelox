class PredictionParameters:
    def __init__(self):
        self.__no_of_days=0
        self.__growth_rate=0.00
        self.__social_distance_compliance=0.00
    def get_no_of_days(self):
        return(self.__no_of_days)
    def get_growth_rate(self):
        return(self.__growth_rate)
    def get_scaled_growth_rate(self):
        return(self.__growth_rate*(1-(self.__social_distance_compliance/100)))
    def get_social_distance_compliance(self):
        return(self.__social_distance_compliance)
    def set_no_of_days(self, d):
        if (d<0):
            raise Exception("InvalidInteger")
        self.__no_of_days=d
    def set_growth_rate(self, gr):
        if (gr<0 or gr>100):
            raise Exception("InvalidRate")
        self.__growth_rate=gr
    def set_social_distance_compliance(self, sdc):
        if (sdc<0 or sdc>100):
            raise Exception("InvalidRate")
        self.__social_distance_compliance=sdc