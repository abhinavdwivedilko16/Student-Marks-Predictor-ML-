import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass # we will be able to directly define the class variable
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv")  # in the artifact folder we will see the output
    test_data_path: str=os.path.join("artifacts","test.csv")  # in the artifact folder we will see the output
    raw_data_path: str=os.path.join("artifacts","data.csv")  # in the artifact folder we will see the output
    # above mentioned are the input for the data Ingestion component and now data Ingestion component knows where to save the output

# If we have to only initilize the variables then go with the dataclass, 
# And if there are functions inside class then go with __init__ part.

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  #as soon as we call this class, the above 3 mentioned path will save inside this class variable

    def initiate_data_ingestion(self): # if our data is stored in some database then we will write code here to read that data.
        logging.info("Entered in data ingestion component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the data set as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  #creating folder with respect to the paths we defined in dataingestion component
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data completed")

            return(

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
            
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()