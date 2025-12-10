import pandas as pd
from embeddings_utils import get_embedding

# 根据一个指定关键词，去向量空间中检索相似的用户评论

embedding_model = 'text-embedding-3-small'
input_datapath = 'datas/fine_food_reviews_1k.csv'

# 1.准备并读取数据
df = pd.read_csv(input_datapath, index_col=0)
df = df[['Time', 'ProductId', 'UserId', 'Score', 'Summary', 'Text']]

# 2.数据清洗和合并
df = df.dropna()
df['combined'] = 'Title: ' + df.Summary.str.strip() + '; Content: ' + df.Text.str.strip()
print(df.head(2))

# 3.向量化
df['embedding'] = df.combined.apply(lambda x: get_embedding(x, model=embedding_model))
df.to_csv('datas/fine_food_reviews_with_embeddings_1k.csv')
