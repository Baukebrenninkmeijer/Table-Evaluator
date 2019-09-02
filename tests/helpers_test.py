import pytest
import pandas as pd
import numpy as np
from numpy.testing import assert_almost_equal, assert_array_almost_equal
import sys

sys.path.append('../table_evaluator')
from helpers import *

real, fake = load_data('../data/real_test_sample.csv', '../data/fake_test_sample.csv')
cat_cols = ['trans_type', 'trans_operation', 'trans_k_symbol']


def test_mape():
    assert mean_absolute_percentage_error([1], [2]) == 1.0


def test_mean_absolute_error():
    assert mean_absolute_error([1, 1], [2, 2]) == 1.0


def test_euclidean_distance():
    np.testing.assert_almost_equal(euclidean_distance([0, 0], [1, 1]), 1.41421356)


def test_rmse():
    assert rmse([0, 0], [2, 2]) == 2.0


def test_column_correlation():
    column_correlations(real, fake, cat_cols)


def test_associations():
    associations_real = \
        np.array([[1., 0.52283005, -0.22033994, 0.02887571, 0.47428713,
                   0.83529153, 0.84145113, 0.05457374],
                  [0.52283005, 1., 0.02582938, 0.10896693, 0.04827917,
                   0.08816938, 0.16462397, 0.05213217],
                  [-0.22033994, 0.02582938, 1., 0.39474609, 0.19389971,
                   0.53115804, 0.49494012, 0.01663905],
                  [0.02887571, 0.10896693, 0.39474609, 1., 0.12419171,
                   0.23006188, 0.17818539, 0.12393532],
                  [0.47428713, 0.04827917, 0.19389971, 0.12419171, 1.,
                   0.7092204, 0.51643959, 0.03149601],
                  [0.83529153, 0.08816938, 0.53115804, 0.23006188, 0.7092204,
                   1., 0.66314554, 0.09308971],
                  [0.84145113, 0.16462397, 0.49494012, 0.17818539, 0.51643959,
                   0.66314554, 1., 0.10794488],
                  [0.05457374, 0.05213217, 0.01663905, 0.12393532, 0.03149601,
                   0.09308971, 0.10794488, 1.]])

    associations_real_theil = \
        np.array([[1., 0.52283005, -0.22033994, 0.02887571, 0.47428713,
                   0.83529153, 0.84145113, 0.05457374],
                  [0.52283005, 1., 0.02582938, 0.10896693, 0.04827917,
                   0.08816938, 0.16462397, 0.05213217],
                  [-0.22033994, 0.02582938, 1., 0.39474609, 0.19389971,
                   0.53115804, 0.49494012, 0.01663905],
                  [0.02887571, 0.10896693, 0.39474609, 1., 0.12419171,
                   0.23006188, 0.17818539, 0.12393532],
                  [0.47428713, 0.04827917, 0.19389971, 0.12419171, 1.,
                   0.90447413, 0.48204837, 0.03149601],
                  [0.83529153, 0.08816938, 0.53115804, 0.23006188, 0.4591498,
                   1., 0.60417942, 0.09308971],
                  [0.84145113, 0.16462397, 0.49494012, 0.17818539, 0.25020452,
                   0.61774923, 1., 0.10794488],
                  [0.05457374, 0.05213217, 0.01663905, 0.12393532, 0.03149601,
                   0.09308971, 0.10794488, 1.]])
    associations_fake = \
        np.array([[1., 0.47464356, -0.21334696, 0.01405408, 0.49293285,
                   0.85147598, 0.87141525, -0.02928926],
                  [0.47464356, 1., 0.02421427, 0.06713217, 0.05505763,
                   0.10541731, 0.20035159, -0.02641722],
                  [-0.21334696, 0.02421427, 1., 0.41049495, 0.14384781,
                   0.4707562, 0.44913033, -0.05135895],
                  [0.01405408, 0.06713217, 0.41049495, 1., 0.10800537,
                   0.20073483, 0.13085896, 0.03224008],
                  [0.49293285, 0.05505763, 0.14384781, 0.10800537, 1.,
                   0.69978162, 0.52219307, 0.05610419],
                  [0.85147598, 0.10541731, 0.4707562, 0.20073483, 0.69978162,
                   1., 0.66773686, 0.09200128],
                  [0.87141525, 0.20035159, 0.44913033, 0.13085896, 0.52219307,
                   0.66773686, 1., 0.1489684],
                  [-0.02928926, -0.02641722, -0.05135895, 0.03224008, 0.05610419,
                   0.09200128, 0.1489684, 1.]])

    associations_fake_theil = \
        np.array([[1., 0.47464356, -0.21334696, 0.01405408, 0.49293285,
                   0.85147598, 0.87141525, -0.02928926],
                  [0.47464356, 1., 0.02421427, 0.06713217, 0.05505763,
                   0.10541731, 0.20035159, -0.02641722],
                  [-0.21334696, 0.02421427, 1., 0.41049495, 0.14384781,
                   0.4707562, 0.44913033, -0.05135895],
                  [0.01405408, 0.06713217, 0.41049495, 1., 0.10800537,
                   0.20073483, 0.13085896, 0.03224008],
                  [0.49293285, 0.05505763, 0.14384781, 0.10800537, 1.,
                   0.83079489, 0.47511278, 0.05610419],
                  [0.85147598, 0.10541731, 0.4707562, 0.20073483, 0.43157201,
                   1., 0.6060247, 0.09200128],
                  [0.87141525, 0.20035159, 0.44913033, 0.13085896, 0.25020064,
                   0.61435949, 1., 0.1489684],
                  [-0.02928926, -0.02641722, -0.05135895, 0.03224008, 0.05610419,
                   0.09200128, 0.1489684, 1.]])
    assert_array_almost_equal(associations(real, cat_cols, return_results=True, plot=False).values, associations_real)
    assert_array_almost_equal(associations(real, cat_cols, return_results=True, theil_u=True, plot=False).values, associations_real_theil)
    assert_array_almost_equal(associations(fake, cat_cols, return_results=True, plot=False).values, associations_fake)
    assert_array_almost_equal(associations(fake, cat_cols, return_results=True, theil_u=True, plot=False).values, associations_fake_theil)


def test_numerical_encoding():
    num_encoding = numerical_encoding(real, cat_cols=cat_cols)
    uint_cols = num_encoding.select_dtypes(include=['uint8']).columns.tolist()
    num_encoding[uint_cols] = num_encoding[uint_cols].astype('int64')
    stored_encoding = pd.read_csv('../data/real_test_sample_numerical_encoded.csv')
    pd.testing.assert_frame_equal(num_encoding, stored_encoding)

    num_encoding = numerical_encoding(fake, cat_cols=cat_cols)
    uint_cols = num_encoding.select_dtypes(include=['uint8']).columns.tolist()
    num_encoding[uint_cols] = num_encoding[uint_cols].astype('int64')
    stored_encoding = pd.read_csv('../data/fake_test_sample_numerical_encoded.csv')
    pd.testing.assert_frame_equal(num_encoding, stored_encoding)