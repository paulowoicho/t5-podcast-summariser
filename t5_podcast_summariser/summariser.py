from transformers import T5Tokenizer, T5ForConditionalGeneration
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import string

class Summariser:

    def __init__(self, model='paulowoicho/t5-podcast-summarisation'):
        self.tokenizer = T5Tokenizer.from_pretrained(model)
        self.model = T5ForConditionalGeneration.from_pretrained(model)
    
    def clean_up(self, summary):
        head, _ , _ = summary.partition(' ---')
        head = head.strip()
        first_letter = head[0].capitalize()
        head = first_letter + head[1:]
        if head[-1] in string.punctuation:
            pass
        else:
            head += '.'
        return head
    
    def summarise(self, transcript):
        transcript = 'summarize: ' + transcript
        tokenized_transcript = self.tokenizer.encode(transcript, return_tensors="pt")
        if len(tokenized_transcript[0]) > 6500:
            #crashes on more than 6500 tokens
            sentence_list = sent_tokenize(transcript)
            length = len(sentence_list)
            truncated_transcript = sentence_list[:int(length/2)] #maybe they talk about content in the first half? find proof
            transcript = ' '.join(truncated_transcript)
            return self.summarise(transcript)
        summary_ids = self.model.generate(tokenized_transcript, max_length=150, num_beams=2, repetition_penalty=2.5, length_penalty=1.0, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summary = self.clean_up(summary)
        return summary