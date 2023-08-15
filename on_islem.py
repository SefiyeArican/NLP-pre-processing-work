import pandas as pd
import re
import snowballstemmer


#sayısal değerlerin kaldırılması
def remove_numeric(value):
    bfr=[item for item in value if not item.isdigit()]
    print(bfr)
    bfr="".join(bfr)
    return bfr

#emojilerin kaldırılması
def remove_emoji(value):
    bfr=re.compile("[\U00010000-\U0010ffff]",flags=re.UNICODE)
    bfr= bfr.sub(r'',value)
    return bfr

#tek karakterli ifadelerin kaldırılması
def remove_single_chracter(value):
     return re.sub(r'(?:^| )\w(?:$| )','',value)

#noktalama işaretlerinin kaldırılması
def remove_noktalama(value):
     return re.sub(r'[^\w\s]','',value)

#hashtagların kaldırılması
def remove_hashtag(value):
    return re.sub(r'#[^\s]+','',value)

#linklerin kaldırılması
def remove_link(value):
    return re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))','',value)

#kullanıcı adı kaldırma
def remove_username (value):
     return re.sub('@[^\s]+','',value)

#kök indirgereme ve stop words işlemi
def stem_word(value):
    stemmer=snowballstemmer.stemmer("turkish")
    value=value.lower()
    value=stemmer.stemWords(value.split())
    stop_words=['acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç', 'bir şey', 'biz', 'bu',
                "çok", 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem', 'hep', 'hepsi',
                'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mi', 'mu', 'mü', 'nasıl', 'ne', 'neden',
                'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey', 'siz', 'şu',
                'tüm', 've', 'veya', 'ya', 'yani', 'bir', 'iki', 'üç', 'dört', 'bes', 'alti', 'yedi', 'sekiz', 'dokuz', 'on']
    value = [item for item in value if not item in stop_words]
    value=' '.join(value)
    return value

def pre_processing(value):
     return [remove_numeric(remove_emoji
                            (remove_single_chracter
                             (remove_noktalama
                              (remove_link
                               (remove_hashtag
                                (remove_username
                                 (stem_word(word)))))))) for word in value. split()]


# Boşlukların kaldırıllması
def remove_space(value):
     return [item for item in value if item.strip()]







