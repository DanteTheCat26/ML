import numpy as np


def prod_non_zero_diag(x):
    diag_x = np.diag(x)
    non_zero_diag = diag_x[diag_x != 0]
    ans1 = np.prod(non_zero_diag)
    return ans1


def are_multisets_equal(x, y):
    xs = np.sort(x)
    ys = np.sort(y)
    ans1 = np.array_equal(xs, ys)
    return ans1


def max_after_zero(x):
    mask_zero = x[:-1] == 0
    after_zero = x[1:][mask_zero]
    if len(after_zero) == 0:
        return [-1, -1]
    else:
        return np.max(after_zero)


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """

    pass


def run_length_encoding(x):
    if len(x) == 0:
        return [np.array([]), np.array([])]
        
    # Находим, где элементы отличаются от предыдущих
    diff = np.r_[True, x[:-1] != x[1:]]
        
    # Уникальные значения (первые элементы серий)
    values = x[diff]
        
    # Индексы, где начинаются новые серии
    indices = np.where(diff)[0]
        
    # Добавляем длину массива в конец для расчета длин
    indices = np.append(indices, len(x))
        
    # Длины серий (разница между индексами)
    lengths = np.diff(indices)


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Vctorized implementation.
    """

    pass
