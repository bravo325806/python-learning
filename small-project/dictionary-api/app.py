from bs4 import BeautifulSoup
import requests

def format_input_url(searchWord):
    url = 'http://www.learnersdictionary.com/definition/'
    url = url + searchWord.strip().lower().replace(' ', '%20')
    return url

def word_search_parser(wordUrl):
    # url request
    requestsText = requests.get(wordUrl)
    # bs4 get html
    htmlParser = BeautifulSoup(requestsText.text,"html.parser")
    return htmlParser

def find_part_of_speech(htmlParser):
    # span = htmlParser.find_all('span')
    partOfSpeech = []
    fl = htmlParser.findAll("span",{"class":"fl"})
    for w in fl:
        partOfSpeech.append(w.string)
    return partOfSpeech

def find_def_text(htmlParser):
    defOfWord = []
    num = []
    defText = htmlParser.findAll("span",{"class":"def_text"})
    blockNumber = htmlParser.find_all("strong",{"class":"sn_block_num"})
    for n in blockNumber:
        num.append(n.string.replace("\xa0",""))
    for t in defText:
        defOfWord.append(t.string)
    return num , defOfWord

def print_word_results(defNumber, defOfWord, partOfSpeech):
    count = 1
    for s in partOfSpeech:
        print(s)
    for d in defOfWord:
        print(str(count)+":"+str(d))
        count += 1

def main():
    searchWord = input("Search for:")
    # format user enter word
    wordUrl = format_input_url(searchWord)
    # call api and html parser
    htmlParser = word_search_parser(wordUrl)
    # find the word's part of speech ,return tyep : array(list)
    partOfSpeech = find_part_of_speech(htmlParser)
    # find define of word and count number , return tyep : array(list)
    defNumber, defOfWord = find_def_text(htmlParser)
    # print results
    print_word_results(defNumber, defOfWord, partOfSpeech)

if __name__== "__main__":
    main()
