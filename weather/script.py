import numpy as np
from transformers import BertTokenizer, TFBertForSequenceClassification
from django.contrib.staticfiles import finders
from googletrans import Translator


def BERT(X):
    translator = Translator(service_urls=['translate.googleapis.com'])
    X = translator.translate(X)
    X = str(X.text)
    X = X.lower() # Добавить исправление ошибок, если такие есть
    model_name = 'bert-base-uncased'
    file_path = finders.find('weights/model_weights_04.h5')
    model = TFBertForSequenceClassification.from_pretrained(model_name,num_labels=10)
    model.load_weights(file_path)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    predict_encodings = tokenizer(X, truncation=True, padding=True, max_length=256, return_tensors = 'tf')
    y_pred = model.predict(dict(predict_encodings))
    y_pred_labels = np.argmax(y_pred.logits,axis=1)
    if y_pred_labels == [0]:
        y_pred_labels = [10]
    return y_pred_labels[0]
    