
import openai

class connectopenai():
    def fn_openai_connect(self):
        openai.api_key = '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'
        response = openai.Completion.create(
        engine='gpt-3.5-turbo-16k-0613',  
        prompt='Check the sentiment, politeness and emotions of the comments',
        max_tokens=50
        )

        generated_text = response.choices[0].text.strip()
        print(generated_text)
        

        return " "