from pathlib import Path
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
data_dir = Path(__file__).parent / "data"
un = pd.read_csv(data_dir / 'UN_agreement_titles.csv')
titles = un["title"]
stop_words = stopwords.words('english')
titles_clean = [[
    # Stem and convert to lowercase
    PorterStemmer().stem(lowercase_word)
    # Iterate over words in documents
    for word in snippet
    # Create lowercase words and remove empty strings
    if (lowercase_word := word.lower())
    # Remove stop words
    if lowercase_word not in stop_words
    # Remove non-alphabetical words
    if lowercase_word.isalpha()
]
    # Iterate over tokenized documents
    for snippet in [word_tokenize(s) for s in titles]
    # Remove short documents
    if len(snippet) >= 5
]
word_counts_per_snippet = {" ".join(i): len(i) for i in titles_clean}
char_counts_per_word = {w: len(w) for i in titles_clean for w in i}
print(titles_clean)
print(word_counts_per_snippet)
print(char_counts_per_word)
