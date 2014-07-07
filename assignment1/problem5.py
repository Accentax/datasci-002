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
    tweet_loc={}
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
        if "place" in json.loads(line).keys():
            if json.loads(line)["place"]!=None:
                
                place=json.loads(line)["place"]
                if place["country_code"]=="US":
                    if place["full_name"].split(" ")[-1] in states:
                        tweet_loc[i]= place["full_name"].split(" ")[-1]

    return tweets,tweet_loc

def scoringfunc(tweet,sent, sentgrams):
    scoring={}
    temp=[]
    for t in tweet.keys():
        scoring[t]=0
        temp= tweet[t]
        
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

                                        
                    # sentgram keys er str mens det jeg tester for er list,  konvertere fra list til string
                    #finner bi/tri gram fjerner fra temp.
                
        else:
            for wrd in tweet[t]:
                if wrd.encode(encoding='UTF-8',errors='strict') in sent.keys():
                    scoring[t]+=sent[wrd]
    return scoring
        
        

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    sents, sentgrams =sentdict(sent_file)
    tweets,tweet_locs= tweetdict(tweet_file)
    scores =scoringfunc(tweets,sents, sentgrams)
    state_score={key:[0,0] for key in states.keys()}
    for i in tweet_locs.keys():
        state_score[tweet_locs[i]][0]+=1#antall
        state_score[tweet_locs[i]][1]+=scores[i]
        print tweets[i],scores[i]
    
        
 #   for i in tweets.keys():
#       print scores[i]

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',

































        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


if __name__ == "__main__":
    main()
