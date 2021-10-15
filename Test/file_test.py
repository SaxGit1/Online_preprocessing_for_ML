from transformers import CamembertModel, CamembertTokenizer
from transformers import pipeline, logging

camembert_fill_mask = pipeline("fill-mask", model="camembert/camembert-base-wikipedia-4gb", tokenizer="camembert/camembert-base-wikipedia-4gb")
logging.set_verbosity_error()
results = camembert_fill_mask("Plotly c'est <mask>!")
print([results[i]['sequence'] for i in range(len(results))])










