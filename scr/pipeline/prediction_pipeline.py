import sys
import os
from scr.exception import CustomException
from scr.logger import logging
from scr.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                Airline:str,
                 Source:str,          
                Destination:str,     
                Total_Stops:float,   
                Additional_Info:str,            
                Day:int,              
                Month:int,            
                Year:int,              
                Dept_Hour:int,          
                Dept_Min:int,           
                Arrival_hour:int,       
                Arrival_min:int,        
                duration_hour:int,      
                duration_min:int):
        
        self.Airline=Airline
        self.Source=Source        
        self.Destination=Destination    
        self.Total_Stops=Total_Stops  
        self.Additional_Info=Additional_Info           
        self.Day=Day             
        self.Month=Month            
        self.Year=Year             
        self.Dept_Hour=Dept_Hour          
        self.Dept_Min=Dept_Min           
        self.Arrival_hour=Arrival_hour       
        self.Arrival_min=Arrival_min       
        self.duration_hour=duration_hour      
        self.duration_min=duration_min

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Airline':[self.Airline],
                'Source':[self.Source],          
                'Destination':[self.Destination],     
                'Total_Stops':[self.Total_Stops],   
                'Additional_Info':[self.Additional_Info],            
                'Day':[self.Day],              
                'Month':[self.Month],            
                'Year':[self.Year],              
                'Dept_Hour':[self.Dept_Hour],          
                'Dept_Min':[self.Dept_Min],           
                "Arrival_hour":[self.Arrival_hour],       
                'Arrival_min':[self.Arrival_min],        
                'duration_hour':[self.duration_hour],      
                'duration_min':[self.duration_min]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)