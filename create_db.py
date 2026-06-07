python -c "
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-mpnet-base-v2')

client = chromadb.PersistentClient(path='./chroma_db')
try:
    client.delete_collection('company_policies')
except:
    pass

collection = client.create_collection(name='company_policies')

docs = ['20 paid vacation days', 'Work from home 3 days/week', '90 days maternity leave']
embeddings = model.encode(docs).tolist()

collection.add(documents=docs, ids=['v', 'r', 'm'], embeddings=embeddings)
print('✅ Database ready')
"