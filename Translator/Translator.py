from translate import Translator
translator= Translator(to_lang="hi")


if(__name__=='__main__'):
    with open('./text.txt', mode='r') as my_file:
        text=my_file.read();
        translation = translator.translate(text)
        with open('./translated_file.txt' , mode='w') as translated_file:
            translated_file.write(translation);
        print(translation)