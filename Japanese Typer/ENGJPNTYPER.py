from tkinter import *
import pynput
import clipboard
# Hiragana Dict
hgn = { "1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9", "10" : "10",
        '$' : '¥', '!' : '!', "[" : "「", "]" : "」", "~" : "~", '/' : '/',
        'a'  : "あ", 'i' : "い", 'u' : "う", 'e' : "え", 'o' : "お", 'nn' : "ん", 
        "ka" : "か", "ki" : "き", "ku" : "く", "ke" : "け", "ko" : "こ", 
        "sa" : "さ", "shi" : "し", "su" : "す", "se" : "せ", "so" : "そ", 
        "ma" : "ま", "mi" : "み", "mu" : "む", "me" : "め", "mo" : "も", 
        'ta' : "た", 'chi' : "ち", 'tsu' : "つ", "te" : "て", "to" : "と", 
        'na' : "な", 'ni' : "に", 'nu' : "ぬ", "ne" : "ね", "no" : "の",
        'ha' : "は", 'hi' : "ひ", 'fu' : "ふ", "he" : "へ", "ho" : "ほ",
        'ya' : "や", 'yu' : "ゆ", 'yo' : "よ",
        'ra' : "ら", 'ri' : "り", 'ru' : "る", "re" : "れ", "ro" : "ろ",
        'wa' : "わ", 'wo' : "を",
        "x"  : "っ", "."  : "。", ","  : "、",
        "ga" : "が", "gi" : "ぎ", "gu" : "ぐ", "ge" : "け", "go" : "ご",
        'za' : "ざ", 'ji' : "じ", 'zu' : "ず", "ze" : "ぜ", "zo" : "ぞ",
        'da' : "だ", "de" : "で", "do" : "ど",
        'ba' : "ば", 'bi' : "び", 'bu' : "ぶ", "be" : "べ", "bo" : "ぼ",
        'pa' : "ぱ", 'pi' : "ぴ", 'pu' : "ぷ", "pe" : "ぺ", "po" : "ぽ",
        "kya" : "きゃ", "kyu" : "きゅ", "kyo" : "きょ",
        "sha" : "しゃ", "shu" : "しゅ", "sho" : "しょ",	
        "cha" : "ちゃ", "chu" : "ちゅ", "cho" : "ちょ", 
        "nya" : "にゃ", "nyu" : "にゅ", "nyo" : "にょ", 
        "hya" : "ひゃ", "hyu" : "ひゅ", "hyo" : "ひょ",
        "mya" : "みゃ", "myu" : "みゅ", "myo" : "みょ",	
        "rya" : "りゃ", "ryu" : "りゅ", "ryo" : "りょ", 
        "ja"  : "じゃ", "ju"  : "じゅ", "jo"  : "じょ",
        "gya" : "ぎゃ",	"gyu" : "ぎゅ",	"gyo" : "ぎょ",
        "bya" : "びゃ",	"byu" : "びゅ",	"byo" : "びょ",
        "pya" : "ぴゃ",	"pyu" : "ぴゅ",	"pyo" : "ぴょ"}
# Katakana Dict
ktk = {
    "1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9", "10" : "10",
    '$' : '¥', '!' : '!', "[" : "「", "]" : "」", "~" : "~", '/' : '/',
    'a' :'ア', 'i' :'イ','u'  :'ウ', 'e':'エ','o' :'オ',
    'ka':'カ','ki' :'キ','ku' :'ク','ke':'ケ','ko':'コ',
    'ga':'ガ','gi' :'ギ','gu' :'グ','ge':'ゲ','go':'ゴ',
    'sa':'サ','shi':'シ','su' :'ス','se':'セ','so':'ソ',
    'za':'ザ','ji' :'ジ','zu' :'ズ','ze':'ゼ','zo':'ゾ',
    'ta':'タ','chi':'チ','tsu':'ツ','te':'テ','to':'ト',
    'da':'ダ','ji' :'ヂ','zu' :'ヅ','de':'デ','do':'ド',
    'na':'ナ','ni' :'ニ','nu' :'ヌ','ne':'ネ','no':'ノ',
    'ha':'ハ','hi' :'ヒ','fu' :'フ','he':'ヘ','ho':'ホ',
    'ba':'バ','bi' :'ビ','bu' :'ブ','be':'ベ','bo':'ボ',
    'pa':'パ','pi' :'ピ','pu' :'プ','pe':'ペ','po':'ポ',
    'ma':'マ','mi' :'ミ','mu' :'ム','me':'メ','mo':'モ',
    'ra':'ラ','ri' :'リ','ru' :'ル','re':'レ','ro':'ロ',
    'ya':'ヤ','yu' :'ユ','yo' :'ヨ','wa':'ワ','wo':'ヲ',
    'nn': 'ン', "-" : "ー", "x" : "ッ", "." : "。", "," : "、", 
    "kya" : "キ" + "ャ", "kyu" : "キュ",	"kyo" : "キョ", 
    "gya" : "ギャ", "gyu" : "ギュ",	"gyo" : "ギョ", 
    "sha" : "シャ", "shu" : "シュ",	"sho" : "ショ", 
    "ja " : "ジャ", "ju" : "ジュ", "jo" : "ジョ",
    "cha" : "チャ", "chu" : "チュ",	"cho" : "チョ", 
    "nya" : "ニャ", "nyu" : "ニュ",	"nyo" : "ニョ", 
    "hya" : "ヒャ", "hyu" : "ヒュ",	"hyo" : "ヒョ", 
    "bya" : "ビャ", "byu" : "ビュ",	"byo" : "ビョ", 
    "pya" : "ピャ", "pyu" : "ピュ",	"pyo" : "ピョ", 
    "mya" : "ミャ", "myu" : "ミュ",	"myo" : "ミョ", 
    "rya" : "リャ", "ryu" : "リュ",	"ryo" : "リョ" ,
    "wi" : "ウィ", "we" : "ウェ", "wo" : "ワォ",
    "kwa" : "クァ", "kwi" : "クィ", "kwe" : "クェ", "kwo" : "クォ",
    "tsa" : "ツァ", "tsi" : "ツィ", "tse" : "ツェ", "tso" : "ツォ", "ti" : "ティ", "tyu" : "テュ",
    "fa" : "ファ", "fi" : "フィ", "fyu" : "フュ", "fe" : "フェ", "fo" : "フォ",
    "di" : "ディ", "dyu" : "デュ",
    "va" : "ヴァ", "vi" : "ヴィ", "vu" : "ヴ", "ve" : "ヴェ", "vo" : "ヴォ",
}

temp = hgn
#Tkinter (GUI) stuff
window = Tk()
window.title("ENG -> JPN Keyboard"), window.resizable(False, False)
checker = True
#window.iconphoto(False, PhotoImage(file = 'hiraa.png'))
counter, counter2 = 0, 0
c = (Canvas(window, width = 600, height = 400, background = "black")).pack()
t, t2, t3, t4 = Label(window), Label(window), Label(window), Label(window)
t3.config(text = "┏━━━━━━━━━°⌜ 英語 ⌟°━━━━━━━━━┓", font = ("Giddyup Std", 17, "bold"), fg = "gray", background="black"), t3.place(x=3, y=80)
t4.config(text = "━━━━━━━━°⌜  日本語  ⌟°━━━━━━━━━", font = ("Giddyup Std", 17, "bold"), fg = "gray", background="black"), t4.place(x=25, y= 370)
w, o = [], []

# Places text
def cnf(l, txt, cx, cy, size):
    l.config(text = "".join(txt), font = ("Giddyup Std", size, "bold"), fg = "white", background = "black", anchor = "center"), l.place(x=cx, y=cy)
# Reads key input by user
def on_press(key):
    global o, w, temp, checker, counter, counter2
    # Updates check to allow typing
    if key == pynput.keyboard.Key.ctrl_l: 
        checker = True if checker == False else False
    # Checks if typing is allowed
    if checker != False:
        # Quits program
        if key == pynput.keyboard.Key.esc: 
            window.destroy(), exit()
        # Changes scripture(HRG/KTK)
        if str(key).strip("'") == "`": 
            temp = ktk if temp == hgn else hgn
        # Bug fix for counter
        if counter < 0:
            counter = 0
        # Checks if should add new line / keeps bounds
        if counter >= 20 and key != pynput.keyboard.Key.left: 
            o.append("\n")
            counter2 += 1
            counter = 0
        # Clears the Japanese typing
        if key == pynput.keyboard.Key.down: 
            o, w, counter, counter2 = [], [], 0, 0
        # Copies the text
        if key == pynput.keyboard.Key.tab: 
            clipboard.copy("".join(o).replace("\n", ""))
        # Deletes last English letter
        if key == pynput.keyboard.Key.backspace:
            try: 
                w.pop(-1)
            except: 
                return
        # Deletes last Japanese character
        if key == pynput.keyboard.Key.left:
            try:
                u = o.pop(-1)
                if u == "\n": 
                    counter = 20
                    counter2 -= 1
                else:
                    if u != "  ":
                        counter -= len(u)
                    else:
                        counter -= 1
            except: 
                return
        if counter2 < 8:
            # Makes a new line
            if key == pynput.keyboard.Key.enter:
                o.append("\n")
                counter = 0
                counter2 += 1
            # Clears english typing if too long
            if len(w) == 3: 
                w =  []
            # Adds English letter to screen
            elif hasattr(key, "char") and str(key).strip("'") != '`' and str(key).strip("'") != 'x': 
                w.append(str(key).strip("'").lower())
            # Adds space between Japanese typing
            elif key == pynput.keyboard.Key.space: 
                o.append("  ")
                counter += 1
            # Checks if romaji exists in HGN/KTK, then writes
            if "".join(w) in temp and "".join(w):
                thing = temp["".join(w)]
                o.append(thing)
                counter += len(thing)
                w = []
            # Adds a small 'tsu'
            if key == pynput.keyboard.Key.right: 
                o.append(temp['x'])
                counter += 1
            # Checks for exception of 'n'
            if "".join(w) == "nn": 
                o.append(temp["nn"])
                counter += 1
            # Automatically implements small 'tsu' from stressed romaji
            if len(w) > 1 and w[0] == w[1] and "".join(w[1:]) in temp:
                thing = "".join(w[1:])
                o.append(temp["x"] + temp[thing])
                counter += 2
                w = []
    # Updates text
    cnf(t, w, 255, 20, 40), cnf(t2, o, 50, 120, 18)
# Constantly listens to keyboard input
pynput.keyboard.Listener(on_press=on_press).start(), window.mainloop()