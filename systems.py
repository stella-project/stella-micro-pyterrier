import os
import pyterrier as pt 
pt.init()

DATASET = 'irds:cord19'
IDX_PATH = './index/cord19'

class Ranker(object):

    def __init__(self, wmodel):
        self.idx = None
        self.wmodel = wmodel

    def index(self):
        dataset = pt.get_dataset(DATASET)
        indexer = pt.IterDictIndexer(IDX_PATH)
        self.idx = indexer.index(dataset.get_corpus_iter(), fields=['title', 'doi', 'date', 'abstract'])

    def rank_publications(self, query, page, rpp):

        itemlist = []
        
        if query is not None:
            if self.idx is None:
                try:
                    self.idx = pt.IndexFactory.of(os.path.join(IDX_PATH, 'data.properties'))
                except Exception as e:
                    print('No index available: ', e)

            if self.idx is not None:
                wmodel = pt.BatchRetrieve(self.idx, controls={"wmodel": self.wmodel})
                itemlist = wmodel.search(query)['docno'][page*rpp:(page+1)*rpp].tolist()

        return {
            'page': page,
            'rpp': rpp,
            'query': query,
            'itemlist': itemlist,
            'num_found': len(itemlist)
        }


class Recommender(object):

    def __init__(self):
        self.idx = None

    def index(self):
        pass

    def recommend_datasets(self, item_id, page, rpp):

        itemlist = []

        return {
            'page': page,
            'rpp': rpp,
            'item_id': item_id,
            'itemlist': itemlist,
            'num_found': len(itemlist)
        }

    def recommend_publications(self, item_id, page, rpp):

        itemlist = []

        return {
            'page': page,
            'rpp': rpp,
            'item_id': item_id,
            'itemlist': itemlist,
            'num_found': len(itemlist)
        }
