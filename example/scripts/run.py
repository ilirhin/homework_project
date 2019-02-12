import pandas

from example import learners
from example import features_extractors


if __name__ == '__main__':
    learner = learners.Simple()
    fe = features_extractors.Trivial()
    df = pandas.read_csv('../../HR.csv')
    print(learner(fe(df), df['left']))
