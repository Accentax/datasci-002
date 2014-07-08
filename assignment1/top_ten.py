import sys
import re
#test
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
import json
def tweetdict(fr):
    tweets={}
    tweet_loc={}
    import collections
    tags=collections.defaultdict(int)
    for line in fr:

        if "entities" in json.loads(line).keys():
            if "hashtags" in json.loads(line)["entities"]:
                hashtags=json.loads(line)["entities"]["hashtags"]
                if hashtags!=[]:
                    for k in hashtags:
                        tags[k["text"]]+=1
                        
      
    return tags


def main():

    tweet_file = open(sys.argv[1])

    #lines(sent_file)
    #lines(tweet_file)

    hashtags= tweetdict(tweet_file)
    import operator
    sorted_tags=sorted(hashtags.iteritems(), key=operator.itemgetter(1))
    sorted_tags.reverse()
    for i in sorted_tags[:10]:
        print i[0],i[1]
    
if __name__ == "__main__":
    main()
