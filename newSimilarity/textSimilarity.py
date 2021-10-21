from collections import Counter
import jieba
from jieba import analyse
import jieba.posseg
import numpy as np


class CosSim(object):
    # 默认取3个关键词用于比较
    DEFAULT_kEYWORD_COUNT = 100

    def __init__(self):
        # 调整jieba输出日志
        jieba.setLogLevel(jieba.logging.INFO)
        try:
            jieba.load_userdict(r'jieba_white_list.txt')
        except Exception as ex:
            print('没有找到白名单文件：jieba_white_list.txt')


        try:
            stopwords = [line.strip().decode('utf-8') for line in open('jieba_black_list.txt').readlines()
        except Exception as ex:
            print('没有找到白名单文件：jieba_white_list.txt')


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

    @staticmethod
    def getKeywords_textRank(input_str):
        # 使用TextRank算法来提取关键词
        # 这里不使用TF-IDF的原因是TF-IDF是需要有词频文件，即关键词在这个文本中高频，同时在其他文本中低频
        word_tag = jieba.posseg.lcut(input_str)
        for x in word_tag:
            print('{}：{}'.format(x.word, x.flag))

        tool = analyse.textrank
        kws = tool(input_str, topK=CosSim.DEFAULT_kEYWORD_COUNT, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v', 'm'))
        print(kws)

        pass
