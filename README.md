# Automated SOP Letter Generation
This project was a programming assignment as part of the "Fundamentals of Data Mining" course at Ferdowsi University of Mashhad. Our goal in this project was to leverage the power of data mining and the OpenAI API to automate the generation of Statement of Purpose (SOP) letters for university programs.

## Preprocessing
To ensure the quality of our SOP letter generation, we initiated the project by implementing various preprocessing techniques. These techniques included text cleaning, standardizing different units to a uniform format, handling missing data, and more. This step was crucial to ensure that the data input to our language model was of the highest quality.

## Feature Extraction
Next, we focused on extracting key features from the university program dataset. These features served as the building blocks for our language model to generate robust and relevant text. To gain deeper insights into our keywords, we created a word cloud, allowing us to visualize the prominence of specific terms and phrases in the data.

![](./word-cloud.png)

## Prompt Creation
Creating a well-structured and clear prompt was essential to guide our language model effectively. We incorporated the key sentences generated in the previous step into the prompt, ensuring that the model receives the necessary information to generate accurate SOP letters.

## OpenAI API Integration
In the final phase, we seamlessly integrated the OpenAI API, specifically utilizing the GPT-3.5 Turbo model. We sent our carefully crafted prompt to the API, enabling it to generate SOP letters that met the requirements and expectations of the user.

This project showcases the power of data mining and artificial intelligence in automating complex tasks like SOP letter generation. It's a testament to how cutting-edge technology can be harnessed to simplify and streamline processes that were traditionally time-consuming and manual.