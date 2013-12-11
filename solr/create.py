# -*- coding:utf-8 -*-
#!/user/bin/env python
import time

import pysolr


__author__ = 'ngnono'

testSolr = pysolr.Solr('http://10.32.34.51:8080/solr-4.5.1/test/', timeout=30)


def create_datas(docNamePre):
    datas = []
    for i in range(0, 1000, 1):
        datas.append(
            {
                "id": docNamePre + str(i),
                "name": "v1",
                "price": 10,
                "title": [u"丰田汽车，卡罗拉我靠EST，凯美瑞买不起，锐志后取的" + str(i), u"本田杰德" + str(i)],
                "titled_" + (str(i)): [u"北京现代汽车，卡罗拉我靠EST，凯美瑞买不起，锐志后取的" + str(i), u"本田杰德" + str(i)],
                "titled_" + (str(i + 1)): [u"北京现代汽车，卡罗拉我靠EST，凯美瑞买不起，锐志后取的" + str(i), u"本田杰德" + str(i)],
                "titled_" + (str(i + 2)): [u"北京现代汽车，卡罗拉我靠EST，凯美瑞买不起，锐志后取的" + str(i), u"本田杰德" + str(i)],
                "titled_" + (str(i + 3)): [u"北京现代汽车，卡罗拉我靠EST，凯美瑞买不起，锐志后取的" + str(i), u"本田杰德" + str(i)],
                "titled_" + (str(i + 4)): [u"北京现代汽车，卡罗拉我靠EST，凯美瑞买不起，锐志后取的" + str(i), u"本田杰德" + str(i)],
                "titled_" + (str(i + 5)): [u"北京现代汽车，卡罗拉我靠EST，凯美瑞买不起，锐志后取的" + str(i), u"本田杰德" + str(i)],
                "titled_" + (str(i + 6)): [u"北京现代汽车，卡罗拉我靠EST，凯美瑞买不起，锐志后取的" + str(i), u"本田杰德" + str(i)],
                "titled_" + (str(i + 7)): [u"北京现代汽车，卡罗拉我靠EST，凯美瑞买不起，锐志后取的" + str(i), u"本田杰德" + str(i)],
            }
        )

    return datas


def addSolr(datas):
    testSolr.add(datas, commit=False)


def removeAllSolr():
    testSolr.delete(q="*:*", commit=False)


def addData2Solr():
    addData2Solr("doc")


def addData2Solr(namepre):
    datas = create_datas(namepre)
    addSolr(datas)


def addData4While():
    i = 900
    while (True):
        print "%s" % i
        addData2Solr(str(i) + u"dahdjk纹dd")
        i += 1
        time.sleep(1)

