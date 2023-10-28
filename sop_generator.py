import requests
import openai




API_KEY = "OPENAI_API_KEY"

openai.api_key = API_KEY
model_engine = "gpt-3.5-turbo-0301"



def generate_cv(source_uni, dest_uni, user_keywords, extracted_keywords):
    prompt = f'''hi i am a student at {source_uni} and i want a SOP for {dest_uni} 
    please generate a sop for me with below structures and please use this keywords and 
    phrases as possible.
    
    structure: introduction (1 paragraph), past exprience (2 paragraphs), 
    future plans (1 to 2 paragraphs), why us (1 to 2 paragraphs), conclusion (1 paragraph)

    
    key phrases: {user_keywords} ,  {extracted_keywords}

    '''

    print(f"prompt : {prompt}")
    response = openai.ChatCompletion.create(
        model=model_engine, 
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system", "content": "You are a helpful assistant."}
            ]
    )
    
    sop = response.choices[0].message.content
    with open('sop.txt', 'w') as f:
        f.write(f"prompt: {prompt}\n")
        f.write("=================\n")
        f.write(sop)


if __name__ == "__main__":
    response = generate_cv("Ferdowsi University of Mashhad", "Stanford University", ["GPA of 4", "BCS of Computer Engineering", "TA of Data Mining"], ["this program is affordable for me", "i love the city of stanford", "i like that this program is only 4 month"])
    print(response)