import pandas as pd
import numpy as np
from transformers import pipeline
from transformers import AutoModelForQuestionAnswering

def ExtractDetails(paragraph, model_name, Tname=0.95, Tdes=0.85):
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

    details = {
        'Name': [],
        'Designation': [],
        'Quotes': []
    }

    for para in paragraph:
        QA_input1 = {
            'question': 'who is speaker?',
            'context': para
        }
        temp1 = nlp(QA_input1)

        if temp1['score']>Tname:
            QA_input2 = {
                'question': f"who is {temp1['answer']}?",
                'context': para
            }
            temp2 = nlp(QA_input2)

            if temp2['score']<Tdes:
                temp2['answer'] = 'None'
            
            temp3 = ""
            for i, p in enumerate(para.split('“')):
                if i==0:
                    continue
                temp3+=p.split('”')[0]
            
            details['Name'].append(temp1['answer'])
            details['Designation'].append(temp2['answer'])
            details['Quotes'].append(temp3)

    return pd.DataFrame.from_dict(details)