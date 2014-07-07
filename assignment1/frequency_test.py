import sys
import re
import json

def lines(fp):
    print str(len(fp.readlines()))


def tweetdict(fr):
    tweets={}
    i=0
    from collections import defaultdict
    frequency=defaultdict(int)
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

def scoringfunc(tweet):
    
    temp=[]
    
    newtermssent={}
    for t in tweet.keys():
        #print tweet[t]
        
        temp= tweet[t]
        newterms=[]
        
        for wrd in temp:
            newterms.append(wrd)
        
        for term in newterms:
            
            if term in newtermssent.keys():
                
                newtermssent[term]+=1
            else:
                newtermssent[term]=1
    
            # also add new for loop with all new terms her.
    return newtermssent
        
        

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    tweets= tweetdict(tweet_file)
    scores =scoringfunc(tweets)
    
    newterms=scores
    #print len(newterms)
    allterms=sum([i[1] for i in newterms.items()])
    for i in newterms.items():
        print i[0],i[1]/float(allterms)


if __name__ == "__main__":
    main()
