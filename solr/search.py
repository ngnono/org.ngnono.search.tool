# -*- coding:utf-8 -*-
#!/user/bin/env python
import pysolr

__author__ = 'ngnono'


class SolrHelp(object):
    def getSolr(self, urlStr):
        return pysolr.Solr(urlStr, timeout=30)

    def search(self, urlStr, q, opts):
        solr = self.getSolr(urlStr)
        result = solr.search(q, opts)

        return result

    def update(self, urlStr, datas, isAutoCommit):
        solr = self.getSolr(urlStr)
        solr.add(datas, isAutoCommit)

    def remove(self, urlStr, q, isAutoCommit):
        solr = self.getSolr(urlStr)
        solr.delete(q=q, isAutoCommit)


class BaseSerach(object):
    def __init__(self, url):
        self.url = url
        self.solr = SolrHelp()

    def search(self, q, opts):
        return self.solr.search(self.url, q, opts)

    def update(self, datas, isAutoCommit):
        return self.solr.update(self.url, datas, isAutoCommit)

    def remove(self, q, isAutoCommit):
        return self.solr.remove(self.url, q, isAutoCommit)

