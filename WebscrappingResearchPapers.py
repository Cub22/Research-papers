from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re

# Jeśli to Twój pierwszy raz z nltk
nltk.download('stopwords')

# Wczytaj plik txt
with open('WordCloudResearchPapers.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Usuń znaki specjalne, cyfry itp.
text = re.sub(r'[^a-zA-Z\s]', '', text)
text = text.lower()

# Usuń stopwords (słowa typu "the", "and", "in" itd.)
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in text.split() if word not in stop_words]

# Sklej z powrotem do jednego tekstu
filtered_text = ' '.join(filtered_words)

# Generuj chmurę słów
wordcloud = WordCloud(width=1200, height=600, background_color='white').generate(filtered_text)

# Pokaż
plt.figure(figsize=(14, 7))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()