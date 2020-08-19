def Word_Count(f):
    read = ''.join([i for i in f]).replace('\n',' ')#converting into the strings and also the enter '\n' to the space ' '
    read = read.split(' ')#now convert it in the string
    print('number of words',len(read))#count the list read words by 'len'
    return read# return the read list containing the list of the words
def WordPrint(Word):
    stop_word = ['as','the','how','a','an','is','in','i','the','of','and']
    i=0
    for x in Word:
        if x in stop_word:
            pass
        else:
            i+=1
            print(x)
            if i == 10:
                break
def Main():
    f = open('tt.txt','r')
    Word = Word_Count(f)#here variable 'Word' will have the returned value that is read list and going to have the all words
    WordPrint(Word)
if __name__ == "__main__":
    Main()