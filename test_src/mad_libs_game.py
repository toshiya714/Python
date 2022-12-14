import re

text = """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since earliest times. The
 giraffe is the tallest of all
 living __PLURAL_NOUN__, but
 scientists are unable to
 explain how it got its long
 __PART_OF_THE_BODY__. The
 giraffe's tremendous height,
 which might reach __NUMBER__
 __PLURAL_NOUN__, comes from
 it legs and __BODYPART__.
"""

def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分は後を２つのアンダースコアで挟んでください。
    ヒントの単語にはアンダースコアを含めないでください。__hint_hint__はだめです。
    __hint__はOKです。
    """
    
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力 : ".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
            print(mls)
        else:
            print("引数mlsが無効です")

mad_libs(text)