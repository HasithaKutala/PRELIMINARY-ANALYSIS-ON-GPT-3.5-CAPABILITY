import sys
import pandas as pd

from Function.get_input_data import connectpostgre
from Function.connect_openai import connectopenai
from Function.data_split import train_test_split
from Function.open_ai_model import OpenAIModeling

if __name__ == '__main__':
    print("Starting the process...")
    
    
    db = connectpostgre()
    input_data = pd.read_csv("/Users/hasithakutala/Documents/MSc/SGPT/csv /jira_dataset.csv",nrows=5)
    print("Data retrieved from database")
    model = OpenAIModeling(input_data)
    print("Starting the analysis with OpenAI model...")
    analysis_results = model.analyze_comments()
    print("Analysis completed")
    
    