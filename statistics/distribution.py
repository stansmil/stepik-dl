import math

from data import possibility_tables
from statistics.groups_comparisons import ssb, ssw


def Z(mean_partial, mean_general, se):
    """

    :param mean_partial:
    :param mean_general:
    :param se: standard deviation error
    :return:
    """
    return round((mean_partial - mean_general) / se, 2)


def T_Student(mean_partial, mean_general, sd, n):
    """

    :param mean_partial:
    :param mean_general:
    :param sd: standrad deviation of a partial
    :param n: amount of elements
    :return:
    """
    return round((mean_partial - mean_general) / (sd / math.sqrt(n)), 2)


def standard_deviation(disp):
        """"
        :param disp: variance (dispersion)
        """
        return round(math.sqrt(disp), 2)


def standard_error_of_mean(sd, n):
        """

        :param sd: standard deviation
        :param n: amount elements
        :return:
        """
        return round(sd / math.sqrt(n), 2)


def calculate_possibility(val, M, sd):
    z, precision = get_z_possibility_params(val, M, sd)
    tbl_poss = possibility_tables.possibilities_right if z > 0 else possibility_tables.possibilities_left
    possibility = None
    for possibilities in tbl_poss:
        if z in possibilities:
            possibility = possibilities[precision + 1]
            break

    answer = 100 - (int(possibility * 100))
    # print(f"{answer}%")
    return answer


def get_z_possibility_params(val, M, sd) -> tuple:
    Zi = Z(val, M, sd)
    hundred_prec = int((Zi * 100) % 10)
    return round(Zi, 1), hundred_prec


def x2_Pirson(observed_values: list, expected_values: list):
    """
    # https://habr.com/en/company/stepic/blog/311354/

    :param observed_values:
    :param expected_values:
    :return: returns X**2
    """
    summ = 0
    for o, e in zip(observed_values, expected_values):
        summ += (o - e)**2 / e

    return summ


def F_distribution(groups: list) -> float:
    SSB = ssb(groups)
    SSW = ssw(groups)

    df_ssb = len(groups) - 1
    df_ssw = len(groups) * (len(groups[0]) - 1)

    return round((SSB / df_ssb) / (SSW / df_ssw), 2)

