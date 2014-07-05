import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    print type(fp)
    for i in fp:
        print i

def sentdict(wf):
    print "in sentdict"
    print wf
    afinnfile=open(wf)
    print len(afinnfile.readlines())
    scores ={}
    for line in afinnfile:
        print line
    print afinnfile.readlines()

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    sentdict(sys.argv[1])


if __name__ == '__main__':
    main()
