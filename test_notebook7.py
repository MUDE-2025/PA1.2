from testbook import testbook
import numpy as np

def test_filling_matrix():
    with testbook('7_filling_matrix.ipynb', execute=True) as tb:
        A72 = np.array([[float(tb.value(f'A72[{row},{col}]')) for col in range(3)] for row in range(3)])
        assert np.all(A72==1)
        assert A72.shape==(3, 3)

        A73 = np.array([[float(tb.value(f'A73[{row},{col}]')) for col in range(3)] for row in range(3)])
        assert np.all(A73.diagonal()==3)
        assert A73.sum()==9
        assert A73.shape==(3, 3)

        A74 = np.array([[float(tb.value(f'A74[{row},{col}]')) for col in range(10)] for row in range(10)])
        assert A74.shape==(10, 10)
        assert A74.sum()==5
        assert np.sum(A74==1)==5
        assert np.sum(A74==0)==95

        A75 = np.array([[float(tb.value(f'A75[{row},{col}]')) for col in range(5)] for row in range(5)])
        assert A75.shape==(5, 5)
        assert A75.sum()==(5*5 + 2*4)

        A76 = np.array([[float(tb.value(f'A76[{row},{col}]')) for col in range(10)] for row in range(10)])
        assert A76.shape==(10, 10)
        assert A76.sum()==25