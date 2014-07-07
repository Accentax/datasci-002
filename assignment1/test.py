import sys
import re
#test
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
def find_bigrams(input_list):
    return zip(input_list, input_list[1:])

def find_trigrams(input_list):
    return zip(input_list, input_list[1:], input_list[2:])

def sentdict(sr): # function to put AFINN-111.txt sentiment scores into dictionary
    scores={} #create dict
    scoresgrams={}
    for line in sr:
        term, score = line.split("\t") # tab delimited lines with terms and scores
        if " " in term:
            scoresgrams[term]=int(score)

        
        else:
            scores[term]= int(score)
    return scores, scoresgrams
import json

def tweetdict(fr):
    tweets={}
    i=0
    for line in fr:
        if "text" in json.loads(line).keys():
            # edit rawtext and remove any non alphanumeric character 
            #re.sub("[^a-zA-Z]","", old_string)
            #tweets[i]=json.loads(line)["text"]
            tweets[i]= [re.sub("[^a-zA-Z']","", k) for k in json.loads(line)["text"].lower().split(" ") if re.sub("[^a-zA-Z']","", k)!=""]
        else:
            tweets[i]= []
        i+=1
        
    return tweets

def scoringfunc(tweet,sent, sentgrams):
    scoring={}
    temp=[]
    
    newtermssent={}
    for t in tweet.keys():
        scoring[t]=0
        temp= tweet[t]
        newterms=[]
        if len(temp)>1:
            for wrdgram in find_bigrams(temp)+find_trigrams(temp):
                if " ".join(wrdgram) in sentgrams.keys():
                    #print " ".join(wrdgram)
                    scoring[t]+=sentgrams[" ".join(wrdgram)]
                    tempset=set(temp)
                    wrdgset=set(wrdgram)
                    temp=list(tempset-wrdgset)
            for wrd in temp:
                if wrd.encode(encoding='UTF-8',errors='strict') in sent.keys():
                    scoring[t]+=sent[wrd]
                else:
                    newterms.append(wrd)
        
                                                       
                    # sentgram keys er str mens det jeg tester for er list,  konvertere fra list til string
                    #finner bi/tri gram fjerner fra temp.
                
        else:
            for wrd in tweet[t]:
                if wrd.encode(encoding='UTF-8',errors='strict') in sent.keys():
                    scoring[t]+=sent[wrd]
                else:
                    newterms.append(wrd)
        #print len(newterms)
        #print t
        for term in newterms:
            
            if term in newtermssent.keys():
                
                newtermssent[term][0]+=scoring[t]
                newtermssent[term][1]+=1
            else:
                newtermssent[term]=[scoring[t],1]
            # also add new for loop with all new terms her.
    return scoring,newtermssent
        
        

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    sents, sentgrams =sentdict(sent_file)
    tweets= tweetdict(tweet_file)
    scores,newterms =scoringfunc(tweets,sents, sentgrams)
    
    newsent={}
    print len(newterms)
    """for termkey in newterms:
        print termkey, "termkey"
        for term in newterms[termkey][0]:#ordlisten 
            #print term
            #print newterms[termkey][1]
            if term in newsent.keys():
                newsent[term][0]+=newterms[termkey][1]
                newsent[term][1]+=1
            else:
                newsent[term]=[newterms[termkey][1],1]
    """
    for i in newterms.items():
        if i[1][1]>10:
            print i[0], 2*float(i[1][0])/(i[1][1])


if __name__ == "__main__":
    main()
