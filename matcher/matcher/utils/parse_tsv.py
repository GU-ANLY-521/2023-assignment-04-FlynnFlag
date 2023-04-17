import abc
import csv
import collections.abc
import dataclasses
from matcher.name_matcher import NameMatchScorer

@dataclasses.dataclass
class Comparison:
    """Class representing two names and their similarity"""
    name1: str
    name2: str
    score: float = 0.0

class DocIterator(abc.ABC, collections.abc.Iterator):
    def __str__(self):
        return self.__class__.__name__
    
class TsvIterator(DocIterator):
    """Iterator to iterate over tsv-formatted documents"""
    def __init__(self, path):
        self.path = path
        self.fp = open(self.path, encoding='utf-8')
        self.reader = csv.reader(self.fp, delimiter='\t')
        next(self.reader) # skip first row
    def __iter__(self):
        return self
    def __next__(self):
        try:
            row = next(self.reader)
            return Comparison(row[0], row[1], NameMatchScorer(row[0], row[1]))
        except StopIteration:
            self.fp.close()
            raise


def split(path,savepath1,savepath2):
    names = set()
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader)
        for row in reader:
            name = tuple(row[:1])
            names.add(name)

    num_train = int(0.8 * len(names))
    train_names = set()
    test_names = set()
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader)
        for row in reader:
            name = tuple(row[:1])
            if name in names:
                if len(train_names) < num_train:
                    train_names.add(name)
                else:
                    test_names.add(name)
                    names.remove(name)

# create train.tsv
    with open(savepath1, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(['personLabel', 'aliasLabel'])
        with open(path, encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)
            for row in reader:
                if tuple(row[:1]) in train_names:
                    writer.writerow(row[:2])

# Create test.tsv
    with open(savepath2, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(['personLabel', 'aliasLabel'])
        with open(path, encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader) 
            for row in reader:
                if tuple(row[:1]) in test_names:
                    writer.writerow(row[:2])

# when impliment,use the following codes
#split("D:/521/2023-assignment-04-FlynnFlag/matcher/data/names.tsv","D:/521/2023-assignment-04-FlynnFlag/matcher/data/names-train.tsv","D:/521/2023-assignment-04-FlynnFlag/matcher/data/names-test.tsv")