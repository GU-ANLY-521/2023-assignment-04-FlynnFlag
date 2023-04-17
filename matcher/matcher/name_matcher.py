
class NameMatchScorer:
    'Interface for scoring putative name matches'
    def __init__(self, name1, name2,threshold=0.5):
        self.name1 = name1
        self.name2 = name2
        self.threshold=threshold

    def __str__(self):
        return f"{self.name1},{self.name2}"
    # TODO - fill in (see our work from corpora.py for an example)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name1},{self.name2})"  
    # TODO - fill in (see our work from corpora.py for an example)
    def score(self, name1, name2):
        pass

class ExactScorer(NameMatchScorer):
    def __init__(self, name1, name2, threshold=0.5):
        super().__init__(name1, name2, threshold)

    def score(self):
        return int(self.name1 == self.name2)  

class JaccardScorer(NameMatchScorer):
    def __init__(self, name1, name2,threshold=0.5):
        super().__init__(name1, name2,threshold)

    def _score(self):
        set1 = set(self.name1)
        set2 = set(self.name2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        score = intersection / union
        return score
    
    def score(self):
        score=self._score()
        return int(score>=self.threshold)

class LevenshteinScorer(NameMatchScorer):
    def __init__(self, name1, name2, threshold=0.5):
        super().__init__(name1, name2, threshold)

    def _score(self):
        from Levenshtein import distance
        score = distance(self.name1, self.name2)
        return score
    
    def score(self):
        score=self._score()
        return int(score>=self.threshold)
    
class tfidf_matcher(NameMatchScorer):
    def __init__(self, name1, name2,k=5,ngram_range=(1,4),threshold=0.5):
        super().__init__(name1, name2, threshold)
        self.k=k
        self.ngram_range=ngram_range
        if not isinstance(k, int) or k < 1:
            raise ValueError("k must be a positive integer")


    def _score(self):
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.neighbors import NearestNeighbors
        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=self.ngram_range)
        name_vector = vectorizer.fit_transform([self.name1,self.name2])
        knn=NearestNeighbors(n_neighbors=self.k, metric='cosine')
        knn.fit(name_vector)
        return 
    
    def score(self):
        score=self._score()
        return int(score>=self.threshold)
        
#tfidf_matcher(["ab"],["abc"])._score()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1,4))
a=vectorizer.fit_transform(['Sulim Yamadayev','Suleiman Bekmirzayevich Yamadayev']).toarray()
knn=NearestNeighbors(n_neighbors=2, metric='cosine').fit(a)
a