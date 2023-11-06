from transformers import GPT2LMHeadModel, GPT2Tokenizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import openai
import pandas as pd


class OpenAIModeling:

    def __init__(self, input_data_or_path):
        if isinstance(input_data_or_path, pd.DataFrame):
            self.input_data = input_data_or_path
        else:
            self.input_data = pd.read_csv(input_data_or_path)
        openai.api_key = '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'  # Placeholder for the API key

    def analyze_comments(self):
        input_text_column = self.input_data['comment']
        category_column = self.input_data['politeness']
        sentiment_column = self.input_data['sentiment']

        print("Analyzing the comments")

        eval_text = input_text_column.tolist()
        eval_category = category_column.tolist()
        eval_sentiment = sentiment_column.tolist()

        prompt1_list = []
        sentiment_score_list = []

        df_output = pd.DataFrame(columns=["Comment", "Actual_results of politeness", "Actual_results of sentiment", "GPT response of politeness", "GPT response of sentiment"])

        processed_comments_count = 0  # Initialize a counter for processed comments

        for input_text, category, sentiment in zip(eval_text, eval_category, eval_sentiment):
            try:
                input_text = str(input_text)[:4090]
                prompt1 = f'''
                Analyze the following comment written by a developer:
                "{input_text}"

                Provide your analysis in the exact format:
                "Classification: [polite/impolite], Confidence Level: [0-1], Reasoning: [explanatory text]."
                '''
                response1 = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt1,
                    max_tokens=60,
                    n=1,
                    stop=None,
                    temperature=0.2,
                )
                generated_response1 = response1.choices[0].text.strip().lower()
                response_l = "\n".join([line for line in generated_response1.splitlines() if line.strip()])
                prompt1_list.append(response_l)

                prompt2 = f'''
                Analyze the sentiment polarity of the given text and provide a sentiment score between -1 and 1, where: -1 represents a strongly negative sentiment, 0 is neutral, 1 represents a strongly positive sentiment.
                Explain the reasoning behind the assigned sentiment score based on the context and content of the comment.
                output should be in this format: sentiment: |reason:
                Comment:
                '{input_text}'

                '''
                response2 = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt2,
                    max_tokens=60,
                    n=1,
                    stop=None,
                    temperature=0.2,
                )
                generated_response2 = response2.choices[0].text.strip().lower()
                sentiment_score_list.append(generated_response2)

                new_row = pd.DataFrame({
                    "Comment": [input_text],
                    "Actual_results of politeness": [category],
                    "Actual_results of sentiment": [sentiment],
                    "GPT response of politeness": [response_l],
                    "GPT response of sentiment": [generated_response2]
                })
                df_output = pd.concat([df_output, new_row], ignore_index=True)

              
                df_output.to_csv('file_name.csv', index=False)

                processed_comments_count += 1  

            except Exception as e:
                print(f"An error occurred after processing {processed_comments_count} comments: {e}")

        return df_output
