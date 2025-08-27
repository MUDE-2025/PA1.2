from testbook import testbook
import numpy as np

def test_filling_matrix():
    with testbook('5_filling_matrix.ipynb', execute=True) as tb:
        A52 = np.array(tb.value('list(A52)'))
        assert np.all(A52==1)
        assert A52.shape==(3, 3)

        A53 = np.array(tb.value('list(A53)'))
        assert np.all(A53.diagonal()==3)
        assert A53.sum()==9
        assert A53.shape==(3, 3)

        A54 = np.array(tb.value('list(A54)'))
        assert A54.shape==(10, 10)
        assert A54.sum()==5
        assert np.sum(A54==1)==5
        assert np.sum(A54==0)==95

        A55 = np.array(tb.value('list(A55)'))
        assert A55.shape==(5, 5)
        assert A55.sum()==(5*5 + 2*4)

        A56 = np.array(tb.value('list(A56)'))
        assert A56.shape==(10, 10)
        assert A56.sum()==25