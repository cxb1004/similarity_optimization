from oldSimilarity.textSimilarity import CosSim as oldCosSim
from newSimilarity.textSimilarity import CosSim as newCosSim

test_list = [
    ['多少钱', '你好，请问你们这个东西多少钱呢'],
    ['多少钱', '我想买一个你们的产品，但是你们的价格有点高，你能告诉我最低多少钱吗？'],
    ['谢谢你','他妈的'],
    ['谢谢你','你妈的'],
    ['谢谢你','滚'],
    ['谢谢你','草你妈'],
    ['谢谢你','日你大爷'],
    ['谢谢你','你妈逼'],
    ['谢谢你','不要废话'],
    ['谢谢你','你妹的']
]

oldUtils = oldCosSim()
newUtils = newCosSim()

for group in test_list:
    oldValue = oldUtils.getSimilarityIndex(group[0],group[1])
    newValue = newUtils.getSimilarityIndex(group[0],group[1])
    compareFlag = '不变'
    if newValue>oldValue:
        compareFlag = '提升'
    elif newValue>oldValue:
        compareFlag = '降低'
    else:
        compareFlag = '不变'
    print('{} / {}'.format(group[0], group[1]))
    print('   {}: {} -> {}'.format(compareFlag, oldValue, oldValue))


sample = '我想买一个你们的产品，但是你们的价格有点高，你能告诉我最低多少钱吗？'
newUtils.getKeywords_textRank(sample)