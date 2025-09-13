def prod_non_zero_diag(x):
    ans2 = 1
    k = min(len(x), len(x[0]))
    for i in range(k):
        if x[i][i] != 0:
            ans2 *= x[i][i]
    return ans2


def are_multisets_equal(x, y):
    xs = sorted(x)
    ys = sorted(y)
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        if xs[i] != ys[i]:
            return False
    return True


def max_after_zero(x):
    cond = False
    mx = -1
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            if not(cond) or x[i] > mx:
                mx = x[i]
                cond = True
    if not(cond):
        return [-1, -1]
    else:
        return mx


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(x):
    if len(x) == 0:
        return [0, 0]
    ans1 = []
    ans2 = []
    for i in range(len(x)):
        if len(ans1) == 0 or ans1[-1] != x[i]:
            ans1.append(x[i])
            ans2.append(1)
        else:
            ans2[-1] += 1
    return [ans1, ans2]


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    pass
