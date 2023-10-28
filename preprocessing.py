import pandas as pd
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import spacy

# nltk.download('stopwords')



df = pd.read_csv("./dataset.csv")
threshold = 5000
df = df.fillna(df.mode().iloc[0])
needed_info = df.loc[:, ['university_name',
                        'university_rank',
                        'program_name',
                        'program_type',
                        'tution_1_money', 
                        'ielts_score', 
                        'structure', 
                        'academic_req',
                        'tuition_price_specification', 
                        'city', 
                        'duration'
                        ]]


def money_to_semester(money, specification):
    if specification == 'Tuition (Year)':
        return money / 2
    elif specification == 'Tuition (Semester)':
        return money
    elif specification == 'Tuition (Full programme)':
        return money / 2
    elif specification == 'Tuition (Credit)':
        return money * 12
    elif specification == 'Tuition (Module)':
        return money * 2
    elif specification == 'Tuition (Trimester)':
        return money * 3/2
    elif specification == 'Tuition (Month)':
        return money * 6
    elif specification == 'Tuition (Quarter)':
        return money * 2
    else:
        return money


def is_affordable(money, threshold):
    return money <= threshold

def extract_prompt_keywords(x):
    prompt_keywords = []
    
    if x['affordable']:
        prompt_keywords.append("this program is affordable for me")

    prompt_keywords.append(f"i love living in the city of {x['city']}")
    prompt_keywords.append(f"i love the fact that the program duration is only {x['duration']}")
    prompt_keywords.append(f"i am very keen to participate in a university with the rank of {x['university_rank']}")
    prompt_keywords.append(f"i am very interested to join the university of {x['university_name']}")
    prompt_keywords.append(f"i am having the ielts of score {x['ielts_score']}")
    prompt_keywords.append(f"i love to take lectures in {x['lectures']}")
    
    prompt_keywords .append( ','.join(x['academic_req_key_phrases']))

    return ','.join(prompt_keywords)


def remove_html_tags(text):
    text = str(text)
    clean_text = re.sub('<[^<]+?>', '', text)
    return clean_text.strip()

def extract_key_sentences(text):
    sentences = re.split('[.!?]', text)
    
    filtered_sentences = [sentence for sentence in sentences if sentence.strip() != '' and len(sentence.split()) >= 5]
    
    return filtered_sentences


def extract_keywords(x):
    keywords = []

    if x['affordable']:
        keywords.append("affordable")
    
    else:
        keywords.append("not affordable")


    keywords.append(x['city'])
    keywords.append(x['duration'])
    keywords.append(str(x['university_rank']))
    keywords.append(x['university_name'])
    keywords.append(str(x['ielts_score']))
    keywords + x['academic_req_token']
    keywords+ x['lectures']

    return ','.join(keywords)


def extract_key_phrases(x):
    removed_html = remove_html_tags(x)
    return extract_key_sentences(removed_html)


def clean_text(text):
    cleaned_text = re.sub(r'<.*?>', '', text)
    cleaned_text = re.sub(r"[^\w\s']", "", cleaned_text)
    normalized_text = cleaned_text.lower()
    return normalized_text


def extract_lectures(text):
    # Find lecture titles using regex pattern
    pattern = r"'(.*?)'"
    lectures = re.findall(pattern, text)

    return lectures

nlp = spacy.load('en_core_web_sm')

def extract_academic_keywords(text):
    # Load the spaCy English model
    

    # Process the text
    doc = nlp(text)

    # Extract unique keywords from nouns and proper nouns
    keywords = {token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']}
    # print("done")
    return keywords

stopwords_set = set(stopwords.words('english'))



df['structure_cleaned'] = df['structure'].apply(clean_text)
df['structure_token'] = df['structure_cleaned'].apply(word_tokenize)
df['structure_token'] = df['structure_token'].apply(lambda tokens: [token for token in tokens if token not in stopwords_set])
print("structured")
df['tuition_money_semester'] = df.apply(lambda x: money_to_semester(x['tution_1_money'], x['tuition_price_specification']), axis=1)
df['tuition_money_semester'] = df['tuition_money_semester'].fillna(df['tuition_money_semester'].mean())
df['affordable'] = df.apply(lambda x: is_affordable(x['tuition_money_semester'], threshold), axis=1)
print("affordable")



df['lectures'] = df['structure_cleaned'].apply(lambda text: extract_lectures(text))


df['academic_req_cleaned'] = df['academic_req'].apply(clean_text)
df['academic_req_token'] = df['academic_req_cleaned'].apply(word_tokenize)
df['academic_req_token'] = df['academic_req_token'].apply(lambda tokens: [token for token in tokens if token not in stopwords_set])
print("academic")
# df['academic_req_keywords'] = df['academic_req_cleaned'].apply(lambda x: extract_academic_keywords(x))
# print("academic keywords")
df['academic_req_key_phrases'] = df['academic_req'].apply(lambda x: extract_key_phrases(x))
print("academic phrases")
df['prompt_keywords'] = df.apply(lambda x: extract_prompt_keywords(x), axis=1)
print("prompt")
df['keywords'] = df.apply(lambda x: extract_keywords(x), axis=1)
print("keywords")

df.to_csv('your_updated_dataset.csv', index=False)