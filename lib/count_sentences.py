#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ''
        else:
            self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
            self._value = ''
        else:
            self._value = val

    def is_sentence(self):
        return self.value.endswith('.')
    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        sentences = re.split('[.!?]', self.value)
        return len([sentence for sentence in sentences if sentence.strip()])
    

    # Example usage
string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences())  

   