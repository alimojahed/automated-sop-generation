import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("./your_updated_dataset.csv")


# Column name to generate the word cloud
column_name = 'keywords'

# Concatenate all texts in the specified column
text = ' '.join(df[column_name])

# Generate word cloud
wordcloud = WordCloud(width=800, height=400).generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()