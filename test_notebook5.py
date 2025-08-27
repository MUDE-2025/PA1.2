from testbook import testbook
import numpy as np

def test_filling_matrix():
    with testbook('5_filling_matrix.ipynb', execute=True) as tb:
        A52 = np.array([[float(tb.value(f'A52[{row},{col}]')) for col in range(3)] for row in range(3)])
        assert np.all(A52==1)
        assert A52.shape==(3, 3)

        A53 = np.array([[float(tb.value(f'A53[{row},{col}]')) for col in range(3)] for row in range(3)])
        assert np.all(A53.diagonal()==3)
        assert A53.sum()==9
        assert A53.shape==(3, 3)

        A54 = np.array([[float(tb.value(f'A54[{row},{col}]')) for col in range(10)] for row in range(10)])
        assert A54.shape==(10, 10)
        assert A54.sum()==5
        assert np.sum(A54==1)==5
        assert np.sum(A54==0)==95

        A55 = np.array([[float(tb.value(f'A55[{row},{col}]')) for col in range(5)] for row in range(5)])
        assert A55.shape==(5, 5)
        assert A55.sum()==(5*5 + 2*4)

        A56 = np.array([[float(tb.value(f'A56[{row},{col}]')) for col in range(10)] for row in range(10)])
        assert A56.shape==(10, 10)
        assert A56.sum()==25