# -*- coding:utf-8 -*-
#!/user/bin/env python
import sys
import argparse
from solr.create import *

__author__ = 'ngnono'


def parseArgv():
    newParser = argparse.ArgumentParser()

    newParser.add_argument("-a", "--action", dest="action", help="a or d")
    newParser.add_argument("-dnp", "--docnamepre", dest="doc_name_pre", help="doc name pre")

    args = newParser.parse_args()

    argsDict = args.__dict__

    for arg in argsDict.keys():
        exec (arg + " = args." + arg)

    return argsDict


def main(**kwargs):
    try:
        args = parseArgv()
    except:
        print(u"参数解析异常")
        sys.exit(-1)

    action = str(args["action"])

    if(action == "a" or action == "A"):
        addData2Solr(args["doc_name_pre"])

    if(action == "d" or action == "D"):
       removeAllSolr()

    if(action == "c" or action =="C"):
        addData4While()

    #print(u"参数错误"+action)



if __name__ == "__main__":
    """

    startup method

    """

    print ("run")
    main()
    print("end")

