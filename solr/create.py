# -*- coding:utf-8 -*-
#!/user/bin/env python
import pysolr

__author__ = 'ngnono'

testSolr = pysolr.Solr('http://10.32.34.97:8080/solr-4.5.1/test/', timeout=30)


def create_datas(docNamePre):
    datas = []
    for i in range(0, 5, 1):
        datas.append(
            {
                "id": docNamePre + str(i),
                "name": "v1",
                "price": 10,
                "title": ["title" + str(i), "title" + str(i)]
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
