# -*- coding:utf-8 -*-
#!/user/bin/env python
import pysolr

__author__ = 'ngnono'


class SolrHelp(object):
    def getSolr(self, urlStr, timeout=30):
        return pysolr.Solr(urlStr, timeout=timeout)

    def search(self, solr, q, opts):
        return solr.search(q, opts)

    def search(self, urlStr, q, opts):
        return self.search(self.getSolr(urlStr), q, opts)

    def update(self, solr, datas, isCommit):
        return solr.add(datas, commit=isCommit)

    def update(self, urlStr, datas, isCommit):
        solr = self.getSolr(urlStr)
        return solr.add(datas, commit=isCommit)

    def remove(self, solr, q, isCommit):
        return solr.delete(q=q, commit=isCommit)

    def remove(self, urlStr, q, isCommit):
        solr = self.getSolr(urlStr)
        return solr.delete(q=q, commit=isCommit)


class BaseSearch(object):
    def __init__(self, url, timeout=30):
        self.url = url
        self.timeout = timeout
        self.solrHelp = SolrHelp()
        self.solr = self.solrHelp.getSolr(self.url, self.timeout)

    def search(self, q, opts):
        return self.solr.search(q, opts)

    def update(self, datas, isCommit):
        return self.solr.add(datas, commit=isCommit)

    def remove(self, q, isCommit):
        return self.solr.delete(q=q, commit=isCommit)

