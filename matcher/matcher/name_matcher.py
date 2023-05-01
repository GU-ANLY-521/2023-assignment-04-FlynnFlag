
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
    
class TFIDF_matcher(NameMatchScorer):
    def __init__(self, name1, name2,k=1,ngram_range=(1,4),threshold=0.5):
        super().__init__(name1, name2, threshold)
        self.k=k
        self.ngram_range=ngram_range
        if not isinstance(self.k, int) or self.k < 1:
            raise ValueError("k must be a positive integer")


    def _score(self):
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.neighbors import NearestNeighbors
        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1,4))
        x1=vectorizer.fit_transform([self.name1,self.name2])
        knn=NearestNeighbors(n_neighbors=2, metric='cosine')
        knn.fit(x1)
        distances,indices=knn.kneighbors(x1)
        distances
        return 1-distances.mean()

    
    def score(self):
        score=self._score()
        return int(score>=self.threshold)

    

        
class Soundex(NameMatchScorer):
    def __init__(self, name1, name2, threshold=0.5):
        super().__init__(name1, name2, threshold)
    
    def encode(self,name):
        # Define the mapping of letters to Soundex digits
        soundex_digits = "01230120022455012623010202"

        if isinstance(name, float):
            return ''

        # Convert the name to uppercase and remove non-alphabetic characters
        name = ''.join(c for c in name if c.isalpha())
        name = name.upper()
        if name=='':
            return "" 

        # Remove consecutive duplicates
        if len(name)==1:
            pass
        else:
            name = name[0] + ''.join(name[i] for i in range(1, len(name)) if name[i] != name[i-1])
        filter_name=''
        for char in name:
            if ord(char) - ord('A') <= 25:
                filter_name += char
            name=filter_name

        # Replace each letter with its Soundex digit
        if name=='':
            return "" 
        soundex_code = name[0]
        for letter in name[1:]:
            soundex_digit = soundex_digits[ord(letter) - ord('A')]
            if soundex_digit != soundex_code[-1]:
                soundex_code += soundex_digit

        # Remove any zeros and pad the code with trailing zeros if needed
        soundex_code = soundex_code.replace('0', '')
        soundex_code += '0' * (4 - len(soundex_code))

        return soundex_code[:4]



    
    def score(self):
        sound1=self.encode(self.name1)
        sound2=self.encode(self.name2)
        if sound1 == sound2:
            return 1
        elif sound1[:-1] == sound2[:-1]:
            return 1
        return 0
    


