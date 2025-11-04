import json, re, html
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------- 1. Load dataset --------
with open("tesco_sample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# -------- 2. Clean text --------
def clean_html(text: str) -> str:
    """Remove HTML tags and normalize spaces"""
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)      # remove HTML tags
    text = re.sub(r"\s+", " ", text).strip()  # collapse whitespace
    return text.lower()

names = []
texts = []
for item in data:
    if "description" in item:
        cleaned_text = clean_html(item["description"])
        if cleaned_text.strip():  # Filter out empty descriptions immediately
            names.append(item.get("name", "Unnamed product"))
            texts.append(cleaned_text)

# Remove duplicates
unique_df = pd.DataFrame({"name": names, "text": texts}).drop_duplicates(subset="text")
names = unique_df["name"].tolist()
texts = unique_df["text"].tolist()

# -------- 3. TF-IDF representation --------
# Custom stop-word list (optional preprocessing)
custom_stopwords = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'you', 'he', 'she', 'it',
    'they', 'them', 'this', 'that', 'is', 'was', 'am', 'be', 'been',
    'have', 'do', 'does', 'did', 'the', 'and', 'or', 'in', 'on', 'of', 'for'
]

vectorizer = TfidfVectorizer(stop_words=custom_stopwords)
X = vectorizer.fit_transform(texts)

# -------- 4. Cosine similarity --------
sim = cosine_similarity(X)
np.fill_diagonal(sim, 0)  # ignore self-similarity

# -------- 5. Find top similar pair --------
i, j = np.unravel_index(np.argmax(sim), sim.shape)

print("Most similar products:")
print(f"• {names[i]}")
print(f"• {names[j]}")
print(f"Cosine similarity = {sim[i, j]:.4f}")

# -------- 6. Save results --------
top_pairs = []
for a in range(len(names)):
    for b in range(a + 1, len(names)):
        top_pairs.append((names[a], names[b], sim[a, b]))

df = pd.DataFrame(top_pairs, columns=["Product A", "Product B", "Cosine Similarity"])
df = df.sort_values("Cosine Similarity", ascending=False)
df.to_csv("tesco_top_similar_pairs.csv", index=False)

# -------- 7. Create README.txt --------
with open("README.txt", "w", encoding="utf-8") as f:
    f.write("# Cosine Similarity Lab – Tesco Sample\n\n")
    f.write(f"Most similar products:\n")
    f.write(f"- Product A: {names[i]}\n")
    f.write(f"- Product B: {names[j]}\n")
    f.write(f"- Cosine similarity: {sim[i, j]:.4f}\n\n")
    f.write("Preprocessing steps applied: HTML removal, lowercasing, and stopword filtering.\n")
