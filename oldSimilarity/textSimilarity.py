from collections import Counter

import jieba
import jieba.analyse
import numpy as np


class CosSim(object):

    @staticmethod
    def getSimilarityIndex(input1, input2):
        # 切词
        str1 = jieba.lcut(input1)
        str2 = jieba.lcut(input2)
        # 统计词频
        co_str1 = (Counter(str1))
        co_str2 = (Counter(str2))
        p_str1 = []
        p_str2 = []
        # 切词结果生成一个随机集合，可以看作坐标系
        for temp in set(str1 + str2):
            # 生成每个句子在这个坐标系上的向量
            p_str1.append(co_str1[temp])
            p_str2.append(co_str2[temp])

        p_str1 = np.array(p_str1)
        p_str2 = np.array(p_str2)
        # print('{}\n{}'.format(p_str1,p_str2))
        result = p_str1.dot(p_str2) / (np.sqrt(p_str1.dot(p_str1)) * np.sqrt(p_str2.dot(p_str2)))
        return round(result, 4)


