from collections import Counter
import urllib.request, urllib.parse, urllib.error
import ssl
from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from urllib.parse import urlparse,ParseResult,quote

def main():

    def get_text_content():

        url = input('Введите URL страницы, которую надо изучить:  ')
        url = urlparse(url)
        url = ParseResult(url.scheme,url.netloc.encode('idna').decode('ascii'),quote(url.path),url.params,url.query,url.fragment).geturl()
        print(url)

        request_site = Request(url, headers={"User-Agent": " Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"})
        uh = urllib.request.urlopen(request_site).read()
        soup = BeautifulSoup(uh, 'html.parser')
        element = soup.find('body')
        text_content = element.get_text()
        
        return text_content


    def get_number_of_words():
        number_of_words = input("Какое количество самых частотных слов на странице искать: ")
        number_of_words = int(number_of_words)
        
        return number_of_words


    def get_word_to_look():
        word_to_look = input("Какое слово искать: ")
        
        return  word_to_look


    def get_word_to_look_no_ending(known_word):
        word_to_look_no_ending = input("Искомое слово без окончания (чтобый найти все его формы). Просто нажмите Enter, если не нужно искать словоформы: ")
        if len(word_to_look_no_ending)<1:
            word_to_look_no_ending = known_word
        
        return word_to_look_no_ending



    def print_words_to_look(word_to_look, word_to_look_no_ending):
        print(f"Слово без окончания: {word_to_look_no_ending}")
        print(f"Слово с окончанием: {word_to_look}")
        

    def count_words(word_to_look):
        number_word_to_look = text_content.count(word_to_look)

        return number_word_to_look

    def print_most_occur():
        handle = text_content.split()
        CounterV = Counter(handle) 
        most_occur = CounterV.most_common(number_of_words)
        print("Часто используемые слова на странице:")
        for word in  most_occur:
            if len(word[0]) >2:
                print(word[0], word[1])


    def print_number_used_words():
        print(f"Сколько раз на странице использовано слово *{word_to_look}*: {number_word_to_look}")
        print(f"Сколько раз на странице использована форма *{word_to_look_no_ending}*: {number_word_to_look_no_ending}")     



    text_content=get_text_content()
    number_of_words=get_number_of_words()
    word_to_look=get_word_to_look()
    word_to_look_no_ending=get_word_to_look_no_ending(word_to_look)
    print_words_to_look(word_to_look, word_to_look_no_ending)
    number_word_to_look=count_words(word_to_look)
    number_word_to_look_no_ending=count_words(word_to_look_no_ending)
    print_most_occur()
    print_number_used_words()

def afterMain():
    while True:
        waiting = input(f"\nОтлично! Нажмите Enter, чтобы закрыть программу. Нажмите 1 если хотите проанализировать еще одну страницу.  \n")
        if len(waiting) < 1:
            quit()
        else:
            main()

while True:
    main()
    afterMain()
