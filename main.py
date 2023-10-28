import pandas as pd 
from sop_generator import generate_cv


df = pd.read_csv("./your_updated_dataset.csv")


def main():
    university_name = input("university name: ")
    program = input("input program: ")
    user_keywords = input("enter your key phrases separated with comma separated style: ").split(",")
    source_uni = input("source university: ")
    pd.set_option('display.max_colwidth', None)
    row = df.loc[(df['university_name'] == university_name) & (df['program_name'] == program)]

    prompt_keywords = row['prompt_keywords'].str.split(",")

    generate_cv(source_uni, university_name, user_keywords, prompt_keywords)


if __name__ == "__main__":
    main()