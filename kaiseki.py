#
#

from os import pardir
from janome.tokenizer import Tokenizer

import re
import csv

hinsi = "名詞,(一般|固有名詞|サ変接続|形容動詞語幹)"
onazi = "接頭詞,名詞接続,*,*"

kugiri = "●[2]"

list_data = []

kaiseki = [["(1)ヴァイオリン･ソナタ ヘ長調op.5-4(コレルリ)","(2)同(ドビュッシｰ)"],
        ["(3)ピアノ･ソナタ第10番ハ長調K.330","(4)同第11番イ長調K.33｢トルコ行進曲付き｣"],
        ["(1)ソナタ ホ長調L.23(スカルラッティ)","(2)同ニ短調(同)"],
        ["(1)交響曲第9番ホ短調op.95｢新世界より｣","(2)同第8番ト長調op.88｢イギリス｣"],
        ["(1)カンタｰタ第29番｢神よわれら汝に感謝す｣,","(2)同第119番｢エルサレムよ,主を讃えよ｣"],
        ["(2)チェロ･ソナタ第2番ニ長調BWV1028","(3)同第3番ト短調BWV1029"],
        ["(1)即興曲第1番変イ長調op.29","(2)同第2番嬰ヘ長調op.36"],
        ["(1)ヴァイオリン協奏曲第1番イ短調BWV1041","(2)同第2番ホ長調BWV1042"],
        ["(1)ピアノ協奏曲第1番変ロ短調op.23","(2)同第2番ハ短調op.18"],
        ["(2)前奏曲変ホ長調op.23―6","(3)同嬰ト短調op.32―12"]
          ]

henkan_moji = [
            ["交響曲","同"],
            ["交響詩","同"],
            ["前奏曲","同"],
            ["夜想曲","同"],         
            ["練習曲","同"],
            ["協奏曲","同"],
            ["即興曲","同"],
            ["ソナタ","同"],
            ["即興曲","同"],
            ["幻想曲","同"],
            ["カンタｰタ","同"],
            ["チェロ･ソナタ","同"],
            ["ヴァイオリン･ソナタ","同"],
            ["ヴァイオリン協奏曲","同"],            
            ["ピアノ協奏曲","同"],
            ["ピアノ･ソナタ","同"],
            ["ピアノ三重奏曲","同"],
            ["ピアノ四重奏曲","同"],
            ["ホルン協奏曲","同"],
            ["弦楽四重奏曲","同"],
           
            ["六つの小品集","同"],
            ["メヌエット","同"],         
            ["クラリネット三重奏曲","同"],
            ["クラリネット五重奏曲","同"],
            ["弦楽四重奏曲","同"],
            ["弦楽五重奏曲","同"],
            ["吹奏楽のための組曲","同"],
            ["女声合唱組曲","同"],
            ["女声合唱曲集","同"],
            ["混声合唱組曲","同"],
            ["ノクタｰン","同"],
            ["フルｰトとチェンバロのためのソナタ","同"],
            ["ハンガリｰ舞曲","同"],
            ["歌劇","同"],
            ["スラヴ舞曲","同"],
            ["ハｰプシコｰド協奏曲","同"],
            ["2台のハｰプシコｰドのための協奏曲","同"],
            ["ヴァイオリンとハｰプシコｰドのためのソナタ","同"],
            ["フルｰトとチェンバロのためのソナタ","同"],
            ["スケルツォ","同"],
            ["マズルカ","同"],
            ["ワルツ","同"],
            ["セレナｰド","同"],
            ["12の練習曲","同"],
            ["混声合唱曲","同"],
            ["混声合唱組曲","同"],
            ["リュｰト組曲","同"],
            ["チェンバロのための組曲","同"],
            ["抒情小曲集","同"],
            ["ミクロコスモス","同"],
            ["華麗なるポロネｰズ","同"],
            ["弦楽三重奏曲","同"],
            ["2つのヴァイオリンの協奏曲","同"],
            ["ブランデンブルク協奏曲",""],
            ["フルｰト協奏曲","同"]

          ]

t = Tokenizer()

def onaji_syori( moto_text, dou_text):
    print( moto_text + " " + dou_text )
    for i in range(len(list_data)):
        if re.search(list_data[i][0],moto_text) and re.search( list_data[i][1],dou_text): 
                return re.sub(list_data[i][1],list_data[i][0],dou_text)
    return dou_text




def dou_syori2( moto_text, dou_text ):

        if re.search("交響曲第",moto_text) and re.search( "同第",dou_text): 
            print( re.sub("同第","交響曲第",dou_text))
        elif re.search("カンタｰタ第",moto_text) and re.search( "同第",dou_text):
            print( re.sub("同第","カンタｰタ第",dou_text))
        elif re.search("チェロ･ソナタ第",moto_text) and re.search( "同第",dou_text):
            print( re.sub("同第","チェロ･ソナタ第",dou_text))





        else:
            pass
    


def analyze(text):
    
    tokens = t.tokenize(text)
    result = []

    for token in tokens:
        result.append(
            [token.surface,
             token.part_of_speech])
    return( result )

def study_noun( parts ):
    for word,part in parts:
        if( word == "同" and part == onazi ):
            return( True)
                #   print( word + "" + part,end='' )
    return(False)

def keyword_check(part):
    return re.math(hinsi,part)


if __name__ == '__main__':

    #
    file_pass = 'e:\\classiccd\\'
    filename_doucsv = file_pass + '交響曲_同.csv'
    filename_doutxt = file_pass + '同処理.txt'
    filename_doudoutxt = file_pass + '同同.txt'
    filename_mototxt = file_pass + 'クラシック加工済み.txt'
    #

    with open(filename_doucsv, encoding='utf8', newline='') as f:
        iter_data = csv.reader(f)
        for data in iter_data:
            list_data.append(data)

 #   for i in range(len(list_data)):
 #       print(list_data[i][0] + "+" + list_data[i][1] + "+" )


    kyoku_f = open(filename_doutxt,'w',encoding='utf-8')
    kyoku_writer = csv.writer(kyoku_f)
    kyoku_writer = csv.writer(kyoku_f, lineterminator='\n')

    dou_f = open(filename_doudoutxt,'w',encoding='utf-8')
    
#file=open('e:\\classiccd.txt','r',encoding='utf_8')
    file_r=open(filename_mototxt,'r',encoding='utf_8')
    tmp=""
    tmp_old = ""
    count = 1
    while True:
#    while count < 50:
        
        line = file_r.readline()
       
        if line:
            line = line.rstrip()
        #    print(line)
            res = analyze(line)
            if study_noun(res):
                if( tmp.startswith("[") or tmp.startswith("●") ):
                 #   print("-" + tmp_old)
                 #   print(f'{count} ' + line)
                    memo = []
                    memo.append(count)
                    memo.append( tmp_old )
                    memo.append( line )
                    if onaji_syori(tmp_old,line) == line:
                        dou_f.write(f'{count}'+ line + "+"+ tmp_old + "+"+  onaji_syori(tmp_old,line)+"\n")
                else:
                 #   print("+" + tmp)
                 #   print(f'{count} ' + line)
                    memo = []
                    memo.append(count)
                    memo.append( tmp )
                    memo.append( line )
                    if onaji_syori(tmp,line) == line:
                        dou_f.write(f'{count}'+ line + "-" + tmp + "-"+ onaji_syori(tmp,line)+"\n")
                #
                kyoku_writer.writerow(memo)
                

        else:
            break
        #
        count = count + 1
        tmp_old = tmp
        tmp = line
        
    #for i,line in enumerate(lines):
        #print(line)
        #tokens = analyze(line)
     #   lines[i] = lines[i].rstrip()

    #for line in lines:
    #    res = analyze( line)
    #    print( line)
    #    study_noun( res )

    file_r.close()
    kyoku_f.close()
    dou_f.close()


