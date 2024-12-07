from collections import Counter
import urllib.request, urllib.parse, urllib.error
import ssl
from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from urllib.parse import urlparse,ParseResult,quote
# It was my first attempt to rewrite program from one big script into several functions.
# Now I see that it has a lot of flaws. You can comment on these flaws, but it's
# not necessary. This program is structured as the YouTubeKach program (main and after_main functions).
# Look at the bottom of the code. I need your opinion on the structure.
def main():

    def get_text_content():

        url = input('Enter the URL of the page you want to analyze:  ')
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
        number_of_words = input("How many most frequent words on the page to find: ")
        number_of_words = int(number_of_words)
        
        return number_of_words


    def get_word_to_look():
        word_to_look = input("What word to look for: ")
        
        return  word_to_look


    def get_word_to_look_no_ending(known_word):
        word_to_look_no_ending = input("Enter the word without ending (to find all its forms). Just press Enter if you don't need to find word forms: ")
        if len(word_to_look_no_ending)<1:
            word_to_look_no_ending = known_word
        
        return word_to_look_no_ending



    def print_words_to_look(word_to_look, word_to_look_no_ending):
        print(f"Word without ending: {word_to_look_no_ending}")
        print(f"Word with ending: {word_to_look}")
        

    def count_words(word_to_look):
        number_word_to_look = text_content.count(word_to_look)

        return number_word_to_look

    def print_most_occur():
        handle = text_content.split()
        CounterV = Counter(handle) 
        most_occur = CounterV.most_common(number_of_words)
        print("Frequently used words on the page:")
        for word in  most_occur:
            if len(word[0]) >2:
                print(word[0], word[1])


    def print_number_used_words():
        print(f"How many times the word *{word_to_look}* was used on the page: {number_word_to_look}")
        print(f"How many times the word *{word_to_look_no_ending}* was used on the page: {number_word_to_look_no_ending}")     



    text_content=get_text_content()
    number_of_words=get_number_of_words()
    word_to_look=get_word_to_look()
    word_to_look_no_ending=get_word_to_look_no_ending(word_to_look)
    print_words_to_look(word_to_look, word_to_look_no_ending)
    number_word_to_look=count_words(word_to_look)
    number_word_to_look_no_ending=count_words(word_to_look_no_ending)
    print_most_occur()
    print_number_used_words()

# Here it is: main and then after_main
def after_main():
    while True:
        waiting = input(f"\nGreat! Press Enter to close the program. Press 1 to analyze another page.  \n")
        if len(waiting) < 1:
            quit()
        else:
            main()

while True:
    main()
    after_main()