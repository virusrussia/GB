# 1. Создайте класс Word.
# 2. Добавьте свойства text и part of speech.
# 3. Добавьте возможность создавать объект слово со значениями в скобках.
# 4. Создайте класс Sentence
# 5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
# 6. Добавьте метод show, составляющий предложение.
# 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.


class Word:
    text = "Unknown"
    part_of_speech ="Unknown"
    
    def __init__(self, word=None,part=None):
        if word and part:
            self.text=word
            self.part_of_speech=part


class Sentence:
    content=[]
    word_list=[]
    
    def __init__(self,content=[], word_list=[]):
        if (content and word_list):
            self.content=content
            self.word_list=word_list         

    def show(self):
        temp = ""
        for i in self.content:
            temp = f"{temp}{self.word_list[i].text} "
        return temp

    def show_parts (self):
        temp = ""        
        for i in range(0,len(self.word_list)):
            temp=f"{temp}{self.word_list[i].part_of_speech} "
        
        return temp


obj_sentence = Sentence([2, 1, 0], [Word('раму', 'существительное'), Word('мыла', 'глагол'), Word('мама', 'существительное')])

print(obj_sentence.show())

print(obj_sentence.show_parts())