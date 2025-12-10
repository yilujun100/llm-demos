import pandas as pd
import numpy as np
from ast import literal_eval
from embeddings_utils import get_embedding, cosine_similarity

datafile_path = 'datas/fine_food_reviews_with_embeddings_1k.csv'

df = pd.read_csv(datafile_path)
df['embedding'] = df.embedding.apply(literal_eval).apply(np.array)  # literal_eval作用：将字符串列表转成Python list


def search_reviews(df, product_description, top_n=3, pprint=True):
    product_embedding = get_embedding(product_description, model='text-embedding-3-small')
    df['similarity'] = df.embedding.apply(lambda x: cosine_similarity(x, product_embedding))

    res = (
        df.sort_values('similarity', ascending=False)
        .head(top_n)
        .combined.str.replace('Title: ', '')
        .str.replace('; Content: ', ': ')
    )
    if pprint:
        for r in res:
            print(r)
            print('-' * 30)
    return res


results = search_reviews(df, 'delicious beans')
print(results)
