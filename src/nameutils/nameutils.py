# nameutils - Identify given/family names and capitalize correctly
# https://raf.org/nameutils
# https://github.com/rafmod/nameutils
# https://codeberg.org/rafmod/nameutils
#
# Copyright (C) 2023 raf <raf@raf.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <https://www.gnu.org/licenses/>.
#
# 20230709 raf <raf@raf.org>

# Lower-case versions of built-in constants

true = True
false = False
none = None

# Define apostrophe-like characters and hyphen-like characters

apostrophe = "['’ʼʻ]" # Apostrophe, Right single quotation mark, Modifier letter apostrophe, Modifier letter turned comma
hyphen = "\p{dash punctuation}" # Hyphen-Minus, Hyphen, En Dash, Em Dash, et al.

def kc(text):
	# Like casefold() but "folds" apostrophe-like and hyphen-like characters as well
	return s(apostrophe, "'", s(hyphen, '-', text.casefold()))

# Builtin namecase exceptions (Mostly gathered by Michael R. Davis (MRDVT))

namecase_exceptions_builtin = \
[
	'MacAlister', 'MacAlpin', 'MacAlpine', 'MacArthur', 'MacAuley', 'MacBain', 'MacBean',
	'MacCallum', 'MacColl', 'MacDomhnaill', 'MacDonald', 'MacDonell', 'MacDonnell', 'MacDougall',
	'MacDowall', 'MacDuff', 'MacEvan', 'MacEwen', 'MacFarlane', 'MacFie', 'MacGill', 'MacGillivray',
	'MacGregor', 'MacInnes', 'MacIntosh', 'MacIntyre', 'MacIver', 'MacKay', 'MacKenzie',
	'MacKinlay', 'MacKinnon', 'MacKintosh', 'MacLachlan', 'MacLaine', 'MacLaren', 'MacLaurin',
	'MacLea', 'MacLean', 'MacLeay', 'MacLellan', 'MacLennan', 'MacLeod', 'MacMillan', 'MacNab', 'MacNaughton',
	'MacNeacail', 'MacNeil', 'MacNeill', 'MacNicol', "MacO'Shannaig", 'MacPhee', 'MacPherson',
	'MacQuarrie', 'MacQueen', 'MacRae', 'MacTavish', 'MacThomas',

	'MacAuliffe', 'MacCarty', 'MacClaine', 'MacCauley', 'MacClelland', 'MacCleery', 'MacCloud',
	'MacCord', 'MacCleverty', 'MacCredie', 'MacCue', 'MacCurrach', 'MacEachern', 'MacGilvray',
	'MacCray', 'MacDuffie', 'MacFadyen', 'MacFarland', 'MacKinley', 'MacKinney', 'MacLaughlin',
	'MacIvor', 'MacKechnie', 'MacLucas', 'MacManus', 'MacMartin', 'MacNeary', 'MacNevin',
	'MacMahon', 'MacNaught', 'MacNeal', 'MacShane', 'MacWhirter', 'MacAtee', 'MacCarthy',
	'MacWilliams', 'MaDej', 'MaGaw',

	'AbuArab',

	'DaSilva', 'DeAnda', 'DeAngelo', 'DeBardelaben', 'DeBary', 'DeBaugh', 'DeBeck', 'DeBergh',
	'DeBerry', 'DeBlanc', 'DeBoe', 'DeBoer', 'DeBonis', 'DeBord', 'DeBose', 'DeBostock', 'DeBourge',
	'DeBroux', 'DeBruhl', 'DeBruler', 'DeButts', 'DeCaires', 'DeCamp', 'DeCarolis', 'DeCastro',
	'DeCay', 'DeConinck', 'DeCook', 'DeCoppens', 'DeCorte', 'DeCost', 'DeCosta', 'DeCoste', 'DeCoster',
	'DeCouto', 'DeFamio', 'DeFazio', 'DeFee', 'DeFluri', 'DeFord', 'DeForest', 'DeFraia', 'DeFrancis',
	'DeFrange', 'DeFree', 'DeFrees', 'DeGarmo', 'DeGear', 'DeGeare', 'DeGnath', 'DeGraff',
	'DeGraffenreid', 'DeGrange', 'DeGraw', 'DeGrenier', 'DeGroft', 'DeGroot', 'DeGuaincour',
	'DeHaan', 'DeHaas', 'DeHart', 'DeHass', 'DeHate', 'DeHaven', 'DeHeer', 'DeHerrera', 'DeJarnette',
	'DeJean', 'DeLaet', 'DelAmarre', 'DeLancey', 'DeLara', 'DeLarm', 'DelAshmutt', 'DeLaughter',
	'DeLay', 'DeLespine', 'DelGado', 'DelGaudio', 'DeLong', 'DeLony', 'DeLorenzo', 'DeLozier',
	'DelPrincipe', 'DelRosso', 'DeLuca', 'DeLude', 'DeLuke', 'DeMaio', 'DeMarchi', 'DeMarco',
	'DeMarcus', 'DeMarmein', 'DeMars', 'DeMartinis', 'DeMay', 'DeMello', 'DeMonge', 'DeMont',
	'DeMontigny', 'DeMoss', 'DeNunzio', 'DeNure', 'DePalma', 'DePaola', 'DePasquale', 'DePauli',
	'DePerno', 'DePhillips', 'DePoty', 'DePriest', 'DeRatt', 'DeRemer', 'DeRosa', 'DeRosier',
	'DeRossett', 'DeSaegher', 'DeSalme', 'DeShane', 'DeShano', 'DeSilva', 'DeSimencourt',
	'DeSimone', 'DesJardins', 'DeSoto', 'DeSpain', 'DesPlanques', 'DeSplinter', 'DeStefano',
	'DesVoigne', 'DeTurck', 'DeVall', 'DeVane', 'DeVaughan', 'DeVaughn', 'DeVaul', 'DeVault',
	'DeVenney', 'DeVilbiss', 'DeVille', 'DeVillier', 'DeVinney', 'DeVito', 'DeVore', 'DeVorss',
	'DeVoto', 'DeVries', 'DeWald', 'DeWall', 'DeWalt', 'DeWilfond', 'DeWinne', 'DeWitt', 'DeWolf',
	'DeYarmett', 'DeYoung', 'DiBenedetto', 'DiBona', 'DiCaprio', 'DiCicco', 'DiClaudio',
	'DiClemento', 'DiFrisco', 'DiGiacomo', 'DiGiglio', 'DiGraziano', 'DiGregorio', 'DiLiberto',
	'DiMarco', 'DiMarzo', 'DiPaolo', 'DiPietrantonio', 'DiStefano', 'DoBoto', 'DonSang', 'DuBois',
	'DuBose', 'DuBourg', 'DuCoin', 'DuPre', 'DuPuy', 'DeVaux', 'DeVoir',

	'EnEarl',

	'Fitzell',

	'LaBarge', 'LaBarr', 'LaBelle', 'LaBonte', 'LaBounty', 'LaBrue', 'LaCaille', 'LaCasse',
	'LaChapelle', 'LaClair', 'LaCombe', 'LaCount', 'LaCour', 'LaCourse', 'LaCroix', 'LaFarge',
	'LaFeuillande', 'LaFlamme', 'LaFollette', 'LaFontaine', 'LaForge', 'LaForme', 'LaForte',
	'LaFosse', 'LaFountain', 'LaFoy', 'LaFrance', 'LaFuze', 'LaGaisse', 'LaGreca', 'LaGuardia',
	'LaHaise', 'LaLande', 'LaLanne', 'LaLiberte', 'LaLonde', 'LaLone', 'LaMaitre', 'LaMatry', 'LaMay',
	'LaMere', 'LaMont', 'LaMotte', 'LaMunyon', 'LaPierre', 'LaPlante', 'LaPointe', 'LaPorte',
	'LaPrade', 'LaPrairie', 'LaQue', 'LaRoche', 'LaRochelle', 'LaRose', 'LaRue', 'LaSalle', 'LaSance',
	'LaSart', 'LaTray', 'LaVallee', 'LaVeau', 'LaVenia', 'LaVigna', 'LeBerth', 'LeBlond', 'LeBoeuf',
	'LeBreton', 'LeCaire', 'LeCapitain', 'LeCesne', 'LeClair', 'LeClaire', 'LeClerc', 'LeCompte',
	'LeConte', 'LeCour', 'LeCrone', 'LeDow', 'LeDuc', 'LeFevre', 'LeFlore', 'LeFors', 'LeFridge',
	'LeGrand', 'LeGras', 'LeGrove', 'LeJeune', 'LeMaster', 'LeMesurier', 'LeMieux', 'LeMoine',
	'LePage', 'LeQuire', 'LeRoy', 'LeStage', 'LeSuer', 'LeVally', 'LeVert', 'LiConti', 'LoManto',
	'LoMastro', 'LoRusso',

	'SanFillipo', 'SanGalli', 'SantaLucia',

	'TePas',

	'VanArsdale', 'VanBuren', 'VanCamp', 'VanCleave', 'VanDalsem', 'VanderLey', 'VanderNeut',
	'VanderTol', 'VanderWegen', 'VanDerWeyer', 'VanderWilligen', 'VanDevelde', 'VandeWege',
	'VanDolah', 'VanDusen', 'VanDyke', 'VanHee', 'VanHoak', 'VanHook', 'VanHoose', 'VanHouten',
	'VanHouwe', 'VanHoven', 'VanKampen', 'VanKleck', 'VanKleeck', 'VanKuiken', 'VanLanduyt',
	'VanLeer', 'VanLiere', 'VanLuven', 'VanMeter', 'VanOlinda', 'VanOrmer', 'VanPelt', 'VanSchaick',
	'VanSciver', 'VanScoy', 'VanScoyk', 'VanSickle', 'VanTassel', 'VanTuyl', 'VanValkenburg',
	'VanVolkenburgh', 'VanWinkle', 'VanWysenberghe', 'VanZandt', 'VenDerWeyer', 'VonCannon'
]

namecase_exceptions = none

# Capitalization exceptions for full names used by namecase().
# Include both forms: "given_names family_name" and "family_name, given_names".

namecase_exceptions_full = none

# Capitalization exceptions for full names used by fnamecase().
# This must have the same keys as namecase_exceptions_full.

fnamecase_exceptions_full = none

# Non-individual case exception replacements need a long regex that needs to
# be constructed, and can change. But probably not often. And sometimes a
# lot at once. Regex construction is cached lazily when needed for use.

need_case_update = 1
namecase_exceptions_re = none

# Name affixes that start a multi-word family name

split_starter = none
split_starter_re = none
split_starter_list = \
[
	'de', 'de’', "de'", 'del', 'dels', 'dela', 'della', 'delle', 'dal', 'dalla', 'degli', 'di', 'da', 'du', 'do', 'dos', 'das',
	'le', 'la', 'li', 'lo', 'y', 'i',
	'van', 'von', 'zu', 'der', 'ter', 'den', 'af', 'av', 'til',
	'el', 'al', 'ibn', 'bin', 'ben', 'bat', 'bint', 'binti', 'binte', 'mibeit', 'mimishpachat',
	'of', 'o', 'ó', 'ni', 'ní', 'mac', 'nic', 'ua', 'bean', 'ui', 'uí', 'mhic', 'ap', 'ab', 'ferch', 'verch',
	'san', 'santa', 'santos', 'st', 'st.', 'ste', 'ste.',
	'ka', 'te'
]

# Data for some regexes that are affected by normalization

irish_o = ('O', 'Ó')
irish_vowel = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')
irish_post_bean = ('Uí', 'Ui', 'Mhic')

irish_o_re = '(?:' + '|'.join(irish_o) + ')'
irish_vowel_re = '(?:' + '|'.join(irish_vowel) + ')'
irish_post_bean_re = '(?:' + '|'.join(irish_post_bean) + ')'

# Family names that appear first (Chinese, Korean, Vietnamese).
# When romanized, these family names can appear first or last.
# This is only possible when there are only hundreds of names.
# For Japanese, a statistical method is used.

family_names_ck = none
family_names_ck_re = none
family_names_ck_roman = none
family_names_ck_roman_re = none
family_names_v_roman = none
family_names_v_roman_re = none

family_names_chinese = \
[
	'王', '李', '張', '张', '劉', '刘', '陳', '陈', '楊', '杨', '黃', '黄', '趙', '赵', '吳', '吴', '周', '徐', '孫', '孙', '馬', '马', '朱', '胡', '郭', '何', '林', '高',
	'羅', '罗', '鄭', '郑', '梁', '謝', '谢', '宋', '唐', '許', '许', '鄧', '邓', '韓', '韩', '馮', '冯', '曹', '彭', '曾', '蕭', '萧', '田', '董', '潘', '袁', '蔡', '蔣', '蒋',
	'余', '于', '杜', '葉', '程', '魏', '蘇', '呂', '丁', '任', '盧', '卢', '苏', '吕', '姚', '沈', '鍾', '钟', '姜', '崔', '譚', '谭', '陸', '陆', '范', '汪', '廖', '石',
	'金', '韋', '韦', '賈', '贾', '夏', '傅', '方', '鄒', '邹', '熊', '白', '孟', '秦', '邱', '侯', '江', '尹', '薛', '閻', '阎', '段', '雷', '龍', '龙', '黎', '史', '陶',
	'賀', '贺', '毛', '郝', '顧', '顾', '龔', '龚', '邵', '萬', '万', '覃', '武', '錢', '钱', '戴', '嚴', '严', '歐', '欧', '莫', '孔', '向', '常', '湯', '汤', '康', '易',
	'喬', '乔', '賴', '赖', '文', '施', '洪', '辛', '柯', '莊', '庄',

	'温', '牛', '樊', '葛', '邢', '安', '齐', '伍', '庞', '颜', '倪', '聂', '章', '鲁', '岳', '翟', '殷', '詹', '申', '耿', '关', '兰', '焦', '俞', '左', '柳', '甘', '祝', '包', '宁', '尚', '符',
	'舒', '阮', '纪', '梅', '童', '凌', '毕', '单', '季', '裴', '霍', '涂', '成', '苗', '谷', '盛', '曲', '翁', '冉', '骆', '蓝', '路', '游', '靳', '欧阳', '管', '柴', '蒙', '鲍', '华', '喻',
	'祁', '蒲', '房', '滕', '屈', '饶', '解', '牟', '艾', '尤', '阳', '时', '穆', '农', '司', '卓', '古', '吉', '缪', '简', '车', '项', '连', '芦', '麦', '褚', '娄', '窦', '戚', '岑', '景', '党',
	'宫', '费', '卜', '冷', '晏', '席', '卫', '米', '柏', '宗', '瞿', '桂', '全', '佟', '应', '臧', '闵', '苟', '邬', '边', '卞', '姬', '师', '和', '仇', '栾', '隋', '商', '刁', '沙', '荣', '巫',
	'寇', '桑', '郎', '甄', '丛', '仲', '虞', '敖', '巩', '明', '佘', '池', '查', '麻', '苑', '迟', '邝', '官', '封', '谈', '匡', '鞠', '惠', '荆', '乐', '冀', '郁', '胥', '南', '班', '储', '原',
	'栗', '燕', '楚', '鄢', '劳', '谌', '奚', '皮', '粟', '冼', '蔺', '楼', '盘', '满', '闻', '位', '厉', '伊', '仝', '区', '郜', '海', '阚', '花', '权', '强', '帅', '屠', '豆', '朴', '盖', '练',
	'廉', '禹', '井', '祖', '漆', '巴', '丰', '支', '卿', '国', '狄', '平', '计', '索', '宣', '晋', '相', '初', '门', '雲', '容', '敬', '来', '扈', '晁', '芮', '都', '普', '阙', '浦', '戈', '伏',
	'鹿', '薄', '邸', '雍', '辜', '羊', '阿', '乌', '母', '裘', '亓', '修', '邰', '赫', '杭', '况', '那', '宿', '鲜', '印', '逯', '隆', '茹', '诸', '战', '慕', '危', '玉', '银', '亢', '嵇', '公',
	'哈', '湛', '宾', '戎', '勾', '茅', '利', '於', '呼', '居', '揭', '干', '但', '尉', '冶', '斯', '元', '束', '檀', '衣', '信', '展', '阴', '昝', '智', '幸', '奉', '植', '衡', '富', '尧', '闭', '由',

	'習', '习', '隰', '郤', '郗'
]

family_names_chinese_roman = \
[
	'Wáng', 'Wang', 'Wong', 'Vang', 'Ông', 'Bong', 'Heng', 'Vòng', 'Uōng', 'Waon', 'Whang', 'Vương', 'Ong', 'Ō',
	'Lǐ', 'Li', 'Lei', 'Lee', 'Ly', 'Lí', 'Lî', 'Lý', 'Ri', 'Yi', 'Rhee', 'Dy', 'Dee', 'Sy',
	'Zhāng', 'Chang', 'Zoeng', 'Cheung', 'Cheong', 'Chong', 'Tiuⁿ', 'Tioⁿ', 'Teo', 'Teoh', 'Tio', 'Chông', 'Tong', 'Thong', 'Tsan', 'Tzan', 'Zan', 'Trương', 'Jang', 'Chō', 'Tiu', 'Tiong', 'Sutiono', 'Tjong',
	'Liú', 'Liu', 'Lau', 'Lao', 'Lou', 'Lưu', 'Lâu', 'Low', 'Liù', 'Liew', 'Lew', 'Lieu', 'Lio', 'Yu', 'Yoo', 'Ryū',
	'Chén', "Ch'en", 'Can', 'Chan', 'Chun', 'Chean', 'Chin', 'Tân', 'Tan', 'Tang', 'Ting', 'Chhìn', 'Thín', 'Thin', 'Zen', 'Tchen', 'Trần', 'Jin', 'Tantoco', 'Tanteksi',
	'Yáng', 'Yang', 'Joeng', 'Yeung', 'Yeong', 'Ieong', 'Young', 'Iûⁿ', 'Iôⁿ', 'Yeoh', 'Yeo', 'Yo', 'Nyo', 'Yòng', 'Yong', 'Iōng', 'Yan', 'Ian', 'Dương', 'Yu', 'Yung', 'Yana', 'Yongco', 'Yuchengco', 'Yō',
	'Huáng', 'Huang', 'Wong', 'Wang', 'Vong', 'N̂g', 'Ûiⁿ', 'Ng', 'Ung', 'Ooi', 'Uy', 'Wee', 'Vòng', 'Bong', 'Uōng', 'Fong', 'Waon', 'Whang', 'Hoàng', 'Huỳnh', 'Hwang', 'Kō',
	'Zhào', 'Chao', 'Ziu', 'Chiu', 'Chu', 'Chio', 'Jiu', 'Tiō', 'Tiǒ', 'Teo', 'Teoh', 'Chhau', 'Chau', 'Thèu', 'Cheu', 'Chew', 'Zau', 'Zo', 'Triệu', 'Jo', 'Tio', 'Chō',
	'Wú', 'Wu', 'Ng', 'Ung', 'Eng', 'Gô͘', 'Ngô͘', 'Goh', 'Ǹg', 'Woo', 'Ngô', 'Oh', 'Go', 'Kure', 'Ngo', 'Gozon', 'Gozum', 'Cinco', 'Gochian', 'Gokongwei', 'Gosiengfiao',
	'Zhōu', 'Chou', 'Zau', 'Chow', 'Chau', 'Jao', 'Chao', 'Chiu', 'Chew', 'Jew', 'Chiû', 'Chiew', 'Tiu', 'Cheu', 'Tseu', 'Tzo', 'Chu', 'Châu', 'Ju', 'Shū', 'Joe',
	'Xú', 'Hsü', 'Ceoi', 'Tsui', 'Choi', 'Chui', 'Tsua', 'Chhî', 'Sîr', 'Chee', 'Cher', 'Cheu', 'Swee', 'Ji', 'Jee', 'Chhì', 'Chi', 'Chhié', 'Zhi', 'Zee', 'Zi', 'Từ', 'Seo', 'Sho', 'Dharmadjie', 'Christiadjie',
	'Sūn', 'Sun', 'Syun', 'Suen', 'Sng', 'Suiⁿ', 'Soon', 'Sûn', 'Sen', 'Tôn', 'Son', 'Suan',
	'Mǎ', 'Ma', 'Maa', 'Mah', 'Mar', 'Má', 'Bé', 'Bey', 'Beh', 'Baey', 'Mâ', 'Mo', 'Mu', 'Mã', 'Mapua', 'Ba',
	'Zhū', 'Chu', 'Zyu', 'Chue', 'Choo', 'Chû', 'Tu', 'Tsy', 'Tsyu', 'Tzu', 'Châu', 'Ju', 'Shu', 'Gee',
	'Hú', 'Hu', 'Wu', 'Woo', 'Vu', 'Ô͘', 'Oh', 'Ow', 'Aw', 'Fù', 'Foo', 'Ū', 'Hồ', 'Ho', 'Ko',
	'Guō', 'Kuo', 'Gwok', 'Kwok', 'Kuok', 'Koeh', 'Keh', 'Kerh', 'Kueh', 'Koay', 'Quay', 'Kwek', 'Quek', 'Kwik', 'Kok', 'Koh', 'Goh', 'Koq', 'Quách', 'Gwak', 'Kaku', 'Que', 'Cue', 'Quezon', 'Quison', 'Ker', 'Kho', 'Kue',
	'Hé', 'Hê', 'Ho', 'Hoe', 'Hô', 'Hor', 'Hou', 'Hò', 'Hó', 'Wu', 'Woo', 'Hà', 'Ha', 'Ka',
	'Lín', 'Lin', 'Lam', 'Lum', 'Lîm', 'Lim', 'Lìm', 'Līm', 'Ling', 'Lâm', 'Im', 'Rim', 'Rin', 'Hayashi',
	'Gāo', 'Kao', 'Gou', 'Ko', 'Kou', 'Go', 'Ko͘', 'Kor', 'Kô', 'Kau', 'Koo', 'Gau', 'Cao', 'Kō', 'Caw', 'Co', 'Gao',
	'Luó', 'Lo', 'Law', 'Loh', 'Lowe', 'Lor', 'Lô', 'Lò', 'Lō', 'Lu', 'Loo', 'La', 'Na', 'Ra',
	'Zhèng', 'Cheng', 'Zeng', 'Cheang', 'Chiang', 'Tēⁿ', 'Tīⁿ', 'Tìⁿ', 'Tēeⁿ', 'Tay', 'Teh', 'Chhang', 'Chang', 'Thàng', 'Zen', 'Zung', 'Trịnh', 'Jeong', 'Tei', 'Ty', 'Tee',
	'Liáng', 'Liang', 'Loeng', 'Leung', 'Leong', 'Lang', 'Leng', 'Niû', 'Niô͘', 'Neo', 'Liòng', 'Liōng', 'Lian', 'Lương', 'Yang', 'Ryang', 'Liong', 'Niu', 'Ryō',
	'Xiè', 'Hsieh', 'Ze', 'Tse', 'Che', 'Chiā', 'Siā', 'Sià', 'Chia', 'Cheah', 'Seah', 'Tshia', 'Chhià', 'Zhia', 'Zia', 'Tạ', 'Sa', 'Sha', 'Tsia', 'Sia', 'Saa', 'Sese', 'Shie',
	'Sòng', 'Sung', 'Sàng', 'Song', 'Soong', 'Sūng', 'Son', 'Tống', 'Sō', 'Songco',
	'Táng', "T'ang", 'Tong', 'Tn̂g', 'Tông', 'Tng', 'Tang', 'Thòng', 'Thong', 'Thóng', 'Daon', 'Daan', 'Đường', 'Dang', 'Teng', 'Tō',
	'Xǔ', 'Hsü', 'Heoi', 'Hui', 'Hoi', 'Khó͘', 'Koh', 'Khoh', 'Ko', 'Hí', 'Hee', 'Hé', 'Siu', 'Syu', 'Shiu', 'Hái', 'Hứa', 'Heo', 'Kyo', 'Kho', 'Co', 'Kaw', 'Cojuangco',
	'Dèng', 'Teng', 'Dang', 'Tang', 'Theng', 'Tēng', 'Tèng', 'Then', 'Ten', 'Thèn', 'Den', 'Đặng', 'Deung', 'Tō', 'Deang', 'Tengco', 'Tangco',
	'Hán', 'Han', 'Hon', 'Hân', 'Hang', 'Hòn', 'Hón', 'Ghoe', 'Reu', 'Hàn', 'Kan',
	'Féng', 'Feng', 'Fung', 'Fong', 'Pâng', 'Pang', 'Fùng', 'Phùng', 'Foong', 'Fūng', 'Von', 'Vong', 'Pung', 'Hō', 'Pangco',
	'Cáo', "Ts'ao", 'Cou', 'Cho', 'Tso', 'Chaw', 'Chô', 'Chô͘', 'Chow', 'Tshò', 'Tshàu', 'Chhóu', 'Zau', 'Zo', 'Tào', 'Jo', 'Sō',
	'Péng', "P'eng", 'Pang', 'Banh', 'Phêⁿ', 'Phîⁿ', 'Phêeⁿ', 'Peh', 'Phe', 'Phàng', 'Phang', 'Pháng', 'Ban', 'Bành', 'Paeng', 'Hō', 'Beng', 'Pangco', 'Pay',
	'Zēng', 'Tseng', 'Zang', 'Tsang', 'Chang', 'Dong', 'Chan', 'Tsên', 'Chen', 'Tsen', 'Tzen', 'Tsung', 'Tăng', 'Jeung', 'Sō', 'Tjan', 'Tzeng',
	'Xiāo', 'Hsiao', 'Siu', 'Shiu', 'Sio', 'Siau', 'Seow', 'Siow', 'Siâu', 'Siew', 'Siaw', 'Sieu', 'Shio', 'Tiêu', 'So', 'Siao', 'Syaw', 'Shau', 'Shao', 'Shaw', 'Shō',
	'Tián', "T'ien", 'Tin', 'Chan', 'Tiân', 'Chang', 'Thièn', 'Thien', 'Then', 'Thién', 'Di', 'Dee', 'Điền', 'Jeon', 'Tian', 'Tien', 'Ten',
	'Dǒng', 'Tung', 'Dung', 'Tong', 'Táng', 'Tóng', 'Túng', 'Tûng', 'Ton', 'Toong', 'Đổng', 'Dong', 'Tō',
	'Pān', "P'an", 'Pun', 'Poon', 'Phoaⁿ', 'Phua', 'Phân', 'Pan', 'Phan', 'Phon', 'Phoe', 'Poe', 'Ban', 'Han', 'Pua',
	'Yuán', 'Yüan', 'Jyun', 'Yuen', 'Wan', 'Oân', 'Wang', 'Yèn', 'Yen', 'Iōn', 'Yoe', 'Yoo', 'Yeu', 'Viên', 'Won', 'En', 'Yan',
	'Cài', "Ts'ai", 'Coi', 'Choi', 'Choy', 'Tsoi', 'Toy', 'Chhoà', 'Chua', 'Chhai', 'Chai', 'Chhói', 'Tsa', 'Thái', 'Sái', 'Chae', 'Sai', 'Chuah', 'Cua', 'Choa', 'Tsai', 'Tsay',
	'Jiǎng', 'Chiang', 'Zoeng', 'Tseung', 'Cheung', 'Chiúⁿ', 'Chióⁿ', 'Cheoh', 'Chioh', 'Tsiòng', 'Cheong', 'Chiông', 'Cian', 'Jian', 'Tưởng', 'Jang', 'Shō', 'Chio', 'Chiu', 'Chung',
	'Yú', 'Yü', 'Jyu', 'Yu', 'Yue', 'U', 'Yee', 'Î', 'Û', 'Îr', 'Ee', 'Eu', 'Yì', 'Uī', 'Dư', 'Yeo', 'Yo', 'Ie', 'Iman', 'Oe',
	'Sū', 'Su', 'Sou', 'So', 'So͘', 'Soh', 'Sû', 'Soo', 'Tô', 'Solon',
	'Lǚ', 'Lü', 'Leoi', 'Lui', 'Loi', 'Lū', 'Lī', 'Lǐr', 'Lee', 'Leu', 'Ler', 'Loo', 'Lî', 'Liê', 'Li', 'Lữ', 'Lã', 'Yeo', 'Ryeo', 'Ryo', 'Lu', 'Luy',
	'Dīng', 'Ting', 'Ding', 'Teng', 'Tén', 'Ten', 'Tiang', 'Tin', 'Đinh', 'Jeong', 'Tei',
	'Rén', 'Jen', 'Jam', 'Yam', 'Iam', 'Yum', 'Jîm', 'Lîm', 'Līm', 'Jim', 'Ngim', 'Yim', 'Nìm', 'Nin', 'Nying', 'Nhiệm', 'Nhậm', 'Im', 'Jin',
	'Lú', 'Lu', 'Lou', 'Lo', 'Lô͘', 'Loh', 'Lù', 'Loo', 'Lū', 'Lư', 'Lô', 'No', 'Ro',
	'Yáo', 'Yao', 'Jiu', 'Yiu', 'Yeow', 'Io', 'Iu', 'Iâu', 'Yeo', 'Yào', 'Yow', 'Iēu', 'Yau', 'Diêu', 'Yo', 'Yō',
	'Shěn', 'Shen', 'Sam', 'Shum', 'Sum', 'Sham', 'Sím', 'Sim', 'Shím', 'Sen', 'Sung', 'Thẩm', 'Trầm', 'Shim', 'Shin',
	'Zhōng', 'Chung', 'Zung', 'Chong', 'Chiong', 'Cheng', 'Chûng', 'Tsung', 'Tung', 'Tson', 'Tzon', 'Jong', 'Shō',
	'Jiāng', 'Chiang', 'Goeng', 'Keung', 'Geung', 'Keong', 'Khiang', 'Khiong', 'Khiuⁿ', 'Kiang', 'Kiông', 'Kiong', 'Cian', 'Jian', 'Khương', 'Kang', 'Kyō',
	'Cuī', "Ts'ui", 'Ceoi', 'Chui', 'Choi', 'Chhui', 'Chwee', 'Tshûi', 'Chooi', 'Chhoi', 'Tsoe', 'Tseu', 'Thôi', 'Sai', 'Tseui',
	'Tán', "T'an", 'Taam', 'Tam', 'Tom', 'Ham', 'Hom', 'Thâm', 'Tham', 'Thàm', 'Thóm', 'De', 'Dae', 'Đàm', 'Dam', 'Tan',
	'Lù', 'Lu', 'Luk', 'Lok', 'Lio̍k', 'Loke', 'Lek', 'Liu̍k', 'Liuk', 'Loh', 'Loq', 'Lục', 'Yuk', 'Ryuk', 'Riku', 'Diokno',
	'Fàn', 'Fan', 'Faan', 'Hoān', 'Hoǎn', 'Hwan', 'Huang', 'Hoan', 'Fam', 'Ve', 'Vae', 'Phạm', 'Beom', 'Han', 'Juan',
	'Wāng', 'Wang', 'Wong', 'Ong', 'Óng', 'Vong', 'Uong', 'Waon', 'Whang', 'Uông', 'Ō', 'Ang',
	'Liào', 'Liao', 'Liu', 'Lew', 'Leow', 'Liew', 'Lio', 'Liāu', 'Liàu', 'Liau', 'Liow', 'Lièu', 'Liêu', 'Liệu', 'Ryo', 'Ryō',
	'Shí', 'Shih', 'Sek', 'Shek', 'Seac', 'Seak', 'Chio̍h', 'Chioh', 'Cheoh', 'Sha̍k', 'Sak', 'Shak', 'Zah', 'Zaq', 'Thạch', 'Seok', 'Seki',
	'Jīn', 'Chin', 'Gam', 'Kam', 'Gum', 'Kim', 'Kîm', 'Cin', 'Jin', 'Kin',
	'Wéi', 'Wei', 'Wai', 'Vai', 'Ûi', 'Úi', 'Wee', 'Vúi', 'Vì', 'Wooi', 'Uī', 'We', 'Vi', 'Wi', 'I', 'Uy',
	'Jiǎ', 'Chia', 'Gaa', 'Ka', 'Ga', 'Ká', 'Kée', 'Kia', 'Kâ', 'Cia', 'Jia', 'Giả', 'Go',
	'Xià', 'Hsia', 'Haa', 'Ha', 'Hē', 'Hā', 'Hà', 'Hēe', 'Hah', 'Hay', 'Gho', 'Ya', 'Wo', 'Hạ', 'Ka',
	'Fù', 'Fu', 'Foo', 'Pò͘', 'Poh', 'Phó', 'Bu', 'Po',
	'Fāng', 'Fang', 'Fong', 'Hong', 'Png', 'Puiⁿ', 'Pung', 'Fông', 'Faon', 'Faan', 'Phương', 'Bang', 'Hō',
	'Zōu', 'Tsou', 'Zau', 'Chau', 'Chow', 'Jao', 'Cho͘', 'Cho', 'Che', 'Chou', 'Choh', 'Tsêu', 'Chew', 'Chiew', 'Chiu', 'Tseu', 'Tzeu', 'Châu', 'Chu', 'Shū',
	'Xióng', 'Hsiung', 'Hung', 'Hong', 'Hîm', 'Him', 'Yùng', 'Yoong', 'Hiūng', 'Yon', 'Hùng', 'Ung', 'Yū',
	'Bái', 'Pai', 'Baak', 'Pak', 'Bahk', 'Pe̍h', 'Pe̍k', 'Peh', 'Pha̍k', 'Phak', 'Bah', 'Baq', 'Bạch', 'Baek', 'Haku', 'Bo',
	'Mèng', 'Meng', 'Maang', 'Mang', 'Bēng', 'Bèng', 'Men', 'Màng', 'Man', 'Mạnh', 'Maeng', 'Mō',
	'Qín', "Ch'in", 'Ceon', 'Chun', 'Tseun', 'Tseon', 'Chon', 'Chîn', 'Ching', 'Tshìn', 'Chin', 'Chhín', 'Zhin', 'Zin', 'Tần', 'Jin', 'Shin',
	'Qiū', "Ch'iu", 'Jau', 'Yau', 'Iao', 'Iau', 'Khu', 'Khoo', 'Kho', 'Khiû', 'Hiû', 'Hew', 'Khew', 'Khiu', 'Chieu', 'Khâu', 'Gu', 'Kyū', 'Hiew', 'Chiew', 'Coo', 'Chiou',
	'Hóu', 'Hou', 'Hau', 'Hao', 'Hô͘', 'Hâu', 'Kâu', 'Hoh', 'Hèu', 'Hew', 'Héu', 'Gheu', 'Roe', 'Hầu', 'Hu', 'Kō', 'Caw', 'Ho',
	'Jiāng', 'Chiang', 'Gong', 'Kong', 'Kang', 'Kông', 'Kaon', 'Giang', 'Gang', 'Kō', 'Kiang',
	'Yǐn', 'Yin', 'Wan', 'Ún', 'Ín', 'Un', 'Eun', 'Eung', 'Yún', 'Yoon', 'Doãn', 'Yun', 'In', 'Unson',
	'Xuē', 'Hsüeh', 'Sit', 'Sih', 'Siet', 'Set', 'Siot', 'Shih', 'Siq', 'Tiết', 'Seol', 'Setsu',
	'Yán', 'Yen', 'Jim', 'Yim', 'Im', 'Giâm', 'Ngiam', 'Ngiàm', 'Yam', 'Iēm', 'Ni', 'Gni', 'Nyi', 'Diêm', 'Yeom', 'En',
	'Duàn', 'Tuan', 'Dyun', 'Tuen', 'Tun', 'Toān', 'Toàn', 'Tng', 'Teung', 'Thon', 'Ton', 'Thòn', 'Doe', 'Deu', 'Đoàn', 'Dan',
	'Léi', 'Lei', 'Leoi', 'Lui', 'Loi', 'Lûi', 'Lùi', 'Looi', 'Lōi', 'Le', 'Lae', 'Lôi', 'Roe', 'Noe', 'Rai', 'Luy', 'Hoisan',
	'Lóng', 'Lung', 'Loong', 'Long', 'Lêng', 'Liông', 'Leng', 'Liong', 'Liùng', 'Liūng', 'Lon', 'Yong', 'Ryong', 'Ryō', 'Leong', 'Wee',
	'Lí', 'Li', 'Lai', 'Lê', 'Loy', 'Loi', 'Lì', 'Lài', 'Lee', 'Lī', 'Yeo', 'Ryeo', 'Rei',
	'Shǐ', 'Shih', 'Si', 'Sze', 'Sú', 'Sái', 'Sír', 'Ser', 'Seu', 'Sṳ́', 'Soo', 'Sî', 'Sy', 'Sử', 'Sa', 'Shi',
	'Táo', "T'ao", 'Tou', 'To', 'Tao', 'Tow', 'Tô', 'Tô͘', 'Thô', 'Thàu', 'Thò', 'Thóu', 'Dau', 'Do', 'Đào', 'Tō',
	'Hè', 'Hê', 'Ho', 'Hō', 'Hò', 'Hor', 'Fo', 'Wu', 'Woo', 'Hạ', 'Ha', 'Ka',
	'Máo', 'Mao', 'Mou', 'Mo', 'Mô͘', 'Mor', 'Mô', 'Mâu', 'Mōu', 'Mau', 'Bō',
	'Hǎo', 'Hao', 'Kok', 'Hok', 'Hak', 'Khok', 'Heh', 'Heq', 'Hác', 'Kaku',
	'Gù', 'Ku', 'Gu', 'Goo', 'Khoo', 'Kò͘', 'Koh', 'Koo', 'Kū', 'Cố', 'Go', 'Ko', 'Coo',
	'Gōng', 'Kung', 'Gung', 'Kwong', 'Kéng', 'Kiong', 'Kiûng', 'Kong', 'Kiung', 'Cion', 'Jiong', 'Jun', 'Cung', 'Gong', 'Kyō',
	'Shào', 'Shao', 'Siu', 'Shiu', 'Shaw', 'Sio', 'Siō', 'Siāu', 'Siàu', 'Seow', 'Sioh', 'Shau', 'Sau', 'Sèu', 'Zau', 'Zo', 'Thiệu', 'So', 'Shō', 'Siao', 'Syaw',
	'Wàn', 'Wan', 'Maan', 'Man', 'Meng', 'Bān', 'Bàn', 'Buang', 'Van', 'Màn', 'Vae', 'Mae', 'Ve', 'Me', 'Vạn', 'Ban',
	'Tán', 'Qín', "T'an", 'Taam', 'Tam', 'Thâm', 'Thàm', 'Thóm', 'Dae', 'De', 'Dam', 'Tan',
	'Wǔ', 'Wu', 'Mou', 'Mo', 'Bú', 'Boo', 'Vú', 'Moo', 'Woo', 'Mú', 'Ghu', 'Vũ', 'Võ', 'Mu', 'Bu',
	'Qián', "Ch'ien", 'Cin', 'Chin', 'Chee', 'Chîⁿ', 'Tshièn', 'Chen', 'Chhién', 'Zhi', 'Zee', 'Tiền', 'Jeon', 'Sen', 'Chi',
	'Dài', 'Tai', 'Daai', 'Tè', 'Tèr', 'Thài', 'Ta', 'Da', 'Đái', 'Đới', 'Dae', 'Te',
	'Yán', 'Yen', 'Jim', 'Yim', 'Im', 'Giâm', 'Ngiam', 'Ngiàm', 'Yam', 'Ngiēm', 'Ni', 'Gni', 'Nyi', 'Nghiêm', 'Eom', 'Gen', 'Gan',
	'Ōu', 'Ou', 'Au', 'Eu', 'Ō',
	'Mò', 'Mo', 'Mok', 'Bo̍h', 'Bo̍k', 'Mo̍k', 'Moh', 'Moq', 'Mạc', 'Baku',
	'Kǒng', "K'ung", 'Hung', 'Khóng', 'Kong', 'Khong', 'Khúng', 'Koong', 'Khoong', 'Khon', 'Kung', 'Khổng', 'Kyō', 'Consunji',
	'Xiàng', 'Hsiang', 'Hoeng', 'Heung', 'Hiòng', 'Hiàng', 'Hiang', 'Hióng', 'Shian', 'Hian', 'Hưởng', 'Hyang', '향', 'Kyō',
	'Cháng', "Ch'ang", 'Soeng', 'Sheung', 'Siông', 'Siâng', 'Sioh', 'Seoh', 'Sòng', 'Song', 'Sōng', 'Zan', 'Thường', 'Sang', 'Shō', 'Thōng',
	'Tāng', "T'ang", 'Tong', 'Thng', 'Tng', 'Teung', 'Thông', 'Thong', 'Thaon', 'Thaan', 'Thang', 'Tō', 'Tang',
	'Kāng', 'Kang', 'Hong', 'Khng', 'Khang', 'Không', 'Khong', 'Kong', 'Khaon', 'Khaan', 'Gang', 'Kō',
	'Yì', 'Yi', 'Yik', 'E̍k', 'Ia̍k', 'Ek', 'Yit', 'Iak', 'I', 'Yih', 'Yiq', 'Dịch', 'Yee', 'Eki',
	'Qiáo', "Ch'iao", 'Kiu', 'Kiâu', 'Keow', 'Kiao', 'Khiàu', 'Kiew', 'Khiew', 'Khiéu', 'Jiau', 'Djio', 'Jioh', 'Kiều', 'Kyo', 'Kyō',
	'Kē', 'kʻo', 'O', 'Ngo', 'Koa', 'Kho', 'Ko', 'Ker', 'Quah', 'Kwa', 'Khô', 'Ko´', 'Khu', 'Koo', 'Kha', 'Ga', 'Ka', 'Cua', 'Kua', 'Co', 'Coson',
	'Lài', 'Lai', 'Laai', 'Lay', 'Lōa', 'Lòa', 'Nai', 'La', 'Le', 'Lae', 'Lại', 'Roe', '뢰', 'Noe', 'Rai',
	'Wén', 'Wen', 'Man', 'Bûn', 'Boon', 'Vùn', 'Voon', 'Mūn', 'Ven', 'Vung', 'Văn', 'Moon', 'Bun',
	'Shī', 'Shih', 'Si', 'Xi', 'Soa', 'Sy', 'Sua', 'Sṳ̂', 'Sii´', 'Thí', 'Shi', 'I', 'See', 'Sze',
	'Hóng', 'Hung', 'Huhng', 'Âng', 'Hông', 'Ang', 'Hong', 'Fùng', 'Fung', 'Ghon', 'Won', 'Ung', 'Hồng', 'Hòng', 'Kō',
	'Xīn', 'Hsin', 'San', 'Sen', 'Sîn', 'Sin', 'Xin´', 'Sîng', 'Shin', 'Tân', 'Sing', 'Singson',
	'Zhuāng', 'Chuang', 'Zong', 'Tsong', 'Chong', 'Jong', 'Chng', 'Cheng', 'Chông', 'Zong´', 'Tsaon', 'Tsaan', 'Tzaon', 'Trang', 'Đồ', 'Dưa', 'Chan', 'Chang', 'Jang', 'Shō', 'Sō', 'Ching', 'Chung',

	'An', 'Ang', 'Ao', 'Au', 'Au_Yeung', 'Ba', 'Bai', 'Ban', 'Bao', 'Bau', 'Bi', 'Bo', 'Bu', 'Cai', 'Cao', 'Cha', 'Chai', 'Cham', 'Chan', 'Chang', 'Chao', 'Chau', 'Che',
	'Cheah', 'Chee', 'Chen', 'Cheng', 'Cheong', 'Chern', 'Cheung', 'Chew', 'Chi', 'Chia', 'Chiang', 'Chiao', 'Chien', 'Chim', 'Chin', 'Ching', 'Chiong',
	'Chiou', 'Chiu', 'Cho', 'Choi', 'Chong', 'Choo', 'Chou', 'Chow', 'Choy', 'Chu', 'Chua', 'Chuang', 'Chui', 'Chun', 'Chung', 'Cong', 'Cui', 'Dai', 'Dang',
	'Dea', 'Deng', 'Ding', 'Do', 'Dong', 'Doo', 'Du', 'Duan', 'Dung', 'Eng', 'Fan', 'Fang', 'Fei', 'Feng', 'Fok', 'Fong', 'Foo', 'Fu', 'Fung', 'Gan', 'Gang', 'Gao',
	'Gau', 'Ge', 'Geng', 'Go', 'Goh', 'Gong', 'Gu', 'Guan', 'Guo', 'Ha', 'Hai', 'Han', 'Hang', 'Hao', 'Hau', 'He', 'Ho', 'Hoh', 'Hom', 'Hon', 'Hong', 'Hoo', 'Hou', 'Hsi',
	'Hsia', 'Hsiao', 'Hsieh', 'Hsiung', 'Hsu', 'Hsueh', 'Hu', 'Hua', 'Huang', 'Hui', 'Huie', 'Hum', 'Hung', 'Huo', 'Hwang', 'Hy', 'Ing', 'Ip', 'Jan', 'Jang',
	'Jen', 'Jeng', 'Jeung', 'Jew', 'Jia', 'Jian', 'Jiang', 'Jiao', 'Jim', 'Jin', 'Jing', 'Jo', 'Joe', 'Jong', 'Joo', 'Jou', 'Jow', 'Ju', 'Jue', 'Jung', 'Kam', 'Kan',
	'Kang', 'Kao', 'Kau', 'Ke', 'Keng', 'Kho', 'Khoo', 'Kiang', 'King', 'Ko', 'Koh', 'Kong', 'Koo', 'Kook', 'Kou', 'Ku', 'Kuan', 'Kuang', 'Kuk', 'Kung', 'Kuo', 'Kwan',
	'Kwock', 'Kwok', 'Kwon', 'Kwong', 'Lai', 'Lam', 'Lan', 'Lang', 'Lao', 'Lau', 'Lee', 'Lei', 'Leng', 'Leong', 'Leung', 'Lew', 'Li', 'Lian', 'Liang', 'Liao', 'Liaw',
	'Lien', 'Liew', 'Lim', 'Lin', 'Ling', 'Liou', 'Liu', 'Lo', 'Loh', 'Lok', 'Long', 'Loo', 'Lu', 'Lua', 'Lui', 'Luk', 'Lum', 'Lung', 'Luo', 'Ma', 'Mah', 'Mai', 'Mak', 'Man',
	'Mao', 'Mar', 'Mau', 'Mei', 'Meng', 'Miao', 'Min', 'Ming', 'Miu', 'Mo', 'Mok', 'Mon', 'Mou', 'Moy', 'Mu', 'Mui', 'Na', 'Ng', 'Ngai', 'Ngan', 'Ngo', 'Ni', 'Nie', 'Ning', 'Niu',
	'On', 'Ong', 'Ou', 'Ou_Yang', 'Ow', 'Owyang', 'Pan', 'Pang', 'Pao', 'Pau', 'Pei', 'Peng', 'Pi', 'Ping', 'Po', 'Pon', 'Pong', 'Poon', 'Pu', 'Pun', 'Qi', 'Qian', 'Qiao',
	'Qin', 'Qiu', 'Qu', 'Quan', 'Que', 'Rao', 'Ren', 'Rong', 'Ruan', 'San', 'Sang', 'Seto', 'Sha', 'Sham', 'Shan', 'Shang', 'Shao', 'Shaw', 'Shek', 'Shen', 'Sheng',
	'Sheu', 'Shi', 'Shiau', 'Shieh', 'Shih', 'Shing', 'Shiu', 'Shu', 'Shum', 'Shy', 'Shyu', 'Si', 'Sieh', 'Sin', 'Sing', 'Sit', 'Situ', 'Siu', 'So', 'Soh', 'Song',
	'Soo', 'Soo_Hoo', 'Soon', 'Soong', 'Su', 'Suen', 'Sui', 'Sum', 'Sun', 'Sung', 'Sze', 'Szeto', 'Tai', 'Tam', 'Tan', 'Tang', 'Tao', 'Tay', 'Te', 'Teh', 'Teng', 'Teo',
	'Tian', 'Tien', 'Tin', 'Ting', 'Tiu', 'To', 'Toh', 'Tong', 'Tsai', 'Tsang', 'Tsao', 'Tsay', 'Tse', 'Tseng', 'Tso', 'Tsoi', 'Tsou', 'Tsu', 'Tsui', 'Tu', 'Tuan',
	'Tung', 'Tzeng', 'U', 'Un', 'Ung', 'Wah', 'Wai', 'Wan', 'Wang', 'Wee', 'Wei', 'Wen', 'Weng', 'Wing', 'Wong', 'Woo', 'Woon', 'Wu', 'Xi', 'Xia', 'Xiang', 'Xiao', 'Xie',
	'Xin', 'Xing', 'Xiong', 'Xu', 'Xue', 'Yam', 'Yan', 'Yang', 'Yao', 'Yap', 'Yau', 'Yaw', 'Ye', 'Yee', 'Yeh', 'Yen', 'Yep', 'Yeung', 'Yi', 'Yim', 'Yin', 'Ying', 'Yip', 'Yiu',
	'Yong', 'Yoon', 'You', 'Young', 'Yu', 'Yuan', 'Yue', 'Yuen', 'Yun', 'Yung', 'Zang', 'Zeng', 'Zha', 'Zhan', 'Zhang', 'Zhao', 'Zhen', 'Zheng', 'Zhong', 'Zhou', 'Zhu',
	'Zhuang', 'Zhuo', 'Zong', 'Zou'
]

family_names_korean = \
[
	'가', '價', '賈',
	'간', '簡', '間',
	'갈', '葛',
	'감', '甘',
	'강', '姜', '康', '強', '剛', '江', '㝩',
	'견', '堅', '甄',
	'경', '京', '慶', '景', '耿',
	'계', '季', '桂',
	'고', '顧', '高',
	'곡', '曲', '谷',
	'공', '公', '孔',
	'곽', '廓', '槨', '郭',
	'관', '管', '關',
	'교', '喬', '橋',
	'구', '丘', '仇', '具', '邱',
	'국', '國', '菊', '鞠', '鞫', '麴',
	'궁', '宮', '弓',
	'궉', '鴌',
	'권', '權', '勸', '㩲', '券',
	'근', '斤',
	'금', '琴', '禁', '芩', '金',
	'기', '奇', '寄', '箕', '紀',
	'길', '吉',
	'김', '金',
	'나', '라', '羅', '蘿', '邏', '那',
	'난', '란', '欒',
	'남', '南', '男',
	'남궁', '南宫', '南宮',
	'낭', '랑', '浪',
	'내', '乃', '奈',
	'노', '로', '努', '卢', '盧', '蘆', '虜', '路', '魯',
	'뇌', '뢰', '雷',
	'다', '多',
	'단', '單', '段', '端',
	'담', '譚',
	'당', '唐',
	'대', '代', '大', '戴',
	'도', '到', '度', '桃', '覩', '道', '都', '陶',
	'독고', '獨孤',
	'돈', '頓',
	'동', '東', '童', '董', '蕫', '薫',
	'동방', '東方',
	'두', '杜',
	'등', '滕', '鄧',
	'등정', '藤井',
	'라', '羅', '蘿', '邏',
	'란', '欒',
	'랑', '浪',
	'려', '呂',
	'로', '盧', '路', '魯',
	'뢰', '雷',
	'류유', '㧕', '劉', '柳',
	'리', '李',
	'림', '林',
	'마', '馬', '麻',
	'만',
	'망절', '網切',
	'매', '梅',
	'맹', '孟',
	'명', '明',
	'모', '慕', '毛', '牟',
	'목', '睦', '穆',
	'묘', '苗',
	'무', '武',
	'무본', '武本',
	'묵', '墨',
	'문', '文', '門',
	'미', '米',
	'민', '悶', '敏', '旻', '民', '珉', '閔',
	'박', '博', '朴',
	'반', '潘', '班',
	'방', '房', '方', '旁', '芳', '邦', '防', '龐',
	'배', '培', '背', '裵', '輩', '配',
	'백', '伯', '柏', '白', '百',
	'번', '樊',
	'범', '範', '范',
	'변', '卞', '變', '邊',
	'보', '保', '寶', '甫',
	'복', '卜',
	'복호', '卜扈',
	'봉', '奉', '鳳',
	'부', '付', '傅', '夫', '富',
	'비', '丕',
	'빈', '彬', '濱', '貧', '賓', '賔',
	'빙', '氷',
	'부여', '夫餘',
	'사', '史', '司', '沙', '舍', '謝',
	'사공', '司公', '司空',
	'산', '山',
	'삼', '杉', '森',
	'상', '商', '尙', '尚', '常',
	'서', '俆', '徐', '書', '緖', '西',
	'서문', '西問', '西門',
	'석', '席', '昔', '石', '釋',
	'선', '善', '宣', '鮮',
	'선우', '蘚于', '鮮于', '鮮宇', '鮮牛',
	'설', '偰', '卨', '楔', '薛', '辥', '雪',
	'섭', '葉',
	'성', '城', '宬', '成', '星', '盛',
	'소', '卲', '小', '所', '昭', '簫', '肖', '蕭', '蘇', '邵',
	'손', '孫', '損', '蓀', '遜',
	'송', '宋', '松', '送',
	'수', '水', '洙', '隋',
	'순', '淳', '筍', '舜', '荀', '順', '旬',
	'승', '承', '昇',
	'시', '施', '時', '柴',
	'신', '伸', '信', '愼', '新', '申', '莘', '辛',
	'심', '心', '沁', '沈', '深',
	'아', '阿',
	'안', '安', '案', '顔',
	'애', '艾',
	'야', '夜',
	'양', '량', '揚', '梁', '楊', '樑', '樣', '洋', '粱', '陽',
	'어', '漁', '魚',
	'어금', '魚金',
	'엄', '㘙', '儼', '嚴',
	'여', '려', '余', '呂', '黎', '予',
	'연', '련', '延', '涎', '燕', '連',
	'염', '렴', '廉', '簾', '閻',
	'엽', '葉',
	'영', '影', '榮',
	'예', '倪', '禮', '芮', '藝',
	'오', '五', '伍', '吳', '吾', '晤',
	'옥', '玉',
	'온', '溫',
	'옹', '邕', '雍',
	'완', '阮',
	'왕', '汪王',
	'요', '姚',
	'용', '룡', '龍',
	'우', '于', '偶', '宇', '寓', '尤', '愚', '牛', '禹', '遇',
	'운', '芸', '雲',
	'원', '元', '原', '圓', '苑', '袁', '阮', '院',
	'위', '偉', '衛', '韋', '魏',
	'유', '류', '兪', '劉', '庾', '有', '杻', '枊', '柳', '楡', '由', '裕',
	'육', '륙', '陸',
	'윤', '尹', '允', '潤',
	'은', '殷', '恩', '隱', '銀', '誾',
	'음', '陰',
	'이', '리', '李', '㛅', '伊', '利', '怡', '異',
	'인', '印',
	'임', '림', '任', '壬', '恁', '林',
	'자', '慈',
	'장', '張', '場', '壯', '將', '庄', '漿', '章', '臧', '莊', '葬', '蔣', '藏', '裝', '長',
	'전', '全', '戰', '田', '錢',
	'점', '佔',
	'정', '鄭', '丁', '定', '情', '政', '桯', '正', '程',
	'제', '諸', '齊',
	'제갈', '諸葛', '諸曷', '諸渴',
	'조', '趙', '刁', '曺', '朝', '調', '造', '曹',
	'종', '宗', '鍾',
	'좌', '佐', '左',
	'주', '主', '周', '朱', '株', '珠',
	'증', '增', '曾',
	'지', '地', '智', '池', '遲',
	'진', '䄅', '晋', '珍', '眞', '秦', '蔯', '進', '陣', '陳',
	'차', '車', '次',
	'창', '倉', '昌',
	'채', '菜', '蔡', '采',
	'천', '千', '天', '川',
	'초', '初', '楚',
	'최', '催', '寉', '崔', '最',
	'추', '秋', '鄒',
	'탁', '卓',
	'탄', '彈',
	'태', '太', '泰',
	'판', '判',
	'팽', '彭',
	'편', '片',
	'평', '平',
	'포', '包',
	'표', '俵', '表',
	'풍', '馮',
	'피', '皮',
	'필', '弼', '畢',
	'하', '何', '夏', '河',
	'학', '郝',
	'한', '恨', '汗', '漢', '韓',
	'함', '咸',
	'해', '海', '解',
	'허', '許',
	'현', '玄', '賢',
	'형', '刑', '形', '邢',
	'호', '扈', '湖', '胡', '虎', '鎬',
	'홍', '㤨', '䜤', '哄', '弘', '洪', '烘', '紅',
	'화', '化',
	'황', '晃', '潢', '煌', '皇', '簧', '荒', '黃',
	'황목', '荒木',
	'황보', '皇甫', '黃甫',
	'후', '侯', '候', '后',
	'료',
	'웅'
]

family_names_korean_roman = \
[
	'Ga', 'Ka', 'Kar', 'Gar', 'Kah', 'Gah', 'Ca', 'Cah', 'Car',
	'Gan', 'Kan', 'Gahn', 'Kahn',
	'Gal', 'Kal', 'Karl', 'Garl', 'Gahl', 'Kahl', 'Cahl', 'Carl', 'Cal',
	'Gam', 'Kam', 'Kahm', 'Gahm', 'Cam',
	'Gang', 'Kang', 'Kahng', 'Khang',
	'Gyeon', 'Kyŏn', 'Kyun', 'Kyeon', 'Kyoun', 'Kyon',
	'Gyeong', 'Kyŏng', 'Kyung', 'Kyoung', 'Kyeong', 'Kyong',
	'Gye', 'Kye', 'Kyeh', 'Kay', 'Kie', 'Kae', 'Gae',
	'Go', 'Ko', 'Koh', 'Goh', 'Kho', 'Gho', 'Kor', 'Co',
	'Gok', 'Kok', 'Kog', 'Gog', 'Cock', 'Gogh', 'Cough',
	'Gong', 'Kong', 'Kohng', 'Koung', 'Goung', 'Khong', 'Cong',
	'Gwak', 'Kwak', 'Kwag', 'Kwack', 'Gwag', 'Koak', 'Kuark', 'Quack', 'Quark',
	'Gwan', 'Kwan', 'Quan', 'Kuan', 'Guan',
	'Gyo', 'Kyo', 'Kyoh', 'Gyoh',
	'Gu', 'Ku', 'Koo', 'Goo', 'Kou', 'Kuh', 'Khoo', 'Khu',
	'Guk', 'Kuk', 'Kook', 'Gook', 'Kug', 'Gug', 'Cook',
	'Gung', 'Kung', 'Koong', 'Kwoong',
	'Gwok', 'Kwŏk', 'Kwog', 'Gwog', 'Quock',
	'Gwon', 'Kwŏn', 'Kwon', 'Kweon', 'Kwun',
	'Geun', 'Kŭn', 'Keun', 'Kuen', 'Guen',
	'Geum', 'Kŭm', 'Keum', 'Kum', 'Gum', 'Guem', 'Kuem',
	'Gi', 'Ki', 'Kee', 'Key', 'Gee', 'Ky', 'Khee', 'Kie',
	'Gil', 'Kil', 'Gill', 'Khil', 'Keel', 'Kihl', 'Kiehl', 'Kill',
	'Gim', 'Kim', 'Ghim', 'Kym', 'Keem', 'Gym',
	'Na', 'Ra', 'Nah', 'La', 'Rha', 'Rah', 'Law',
	'Nan', 'Ran', 'Nahn', 'Rahn', 'Nhan', 'Rhan', 'Lan', 'Lahn',
	'Nam', 'Nahm', 'Nham', 'Narm',
	'Namgung', 'Namkung', 'Namgoong', 'Namkoong', 'Namkuhng', 'Namguhng',
	'Nang', 'Rang', 'Nahng', 'Lang',
	'Nae', 'Nai', 'Nay', 'Nea',
	'No', 'Ro', 'Noh', 'Roh', 'Nau', 'Rau',
	'Noe', 'Roe', 'Roi', 'Noi',
	'Da', 'Ta',
	'Dan', 'Tan', 'Dahn', 'Than',
	'Dam', 'Tam', 'Tham', 'Dham', 'Dahm', 'Tahm',
	'Dang', 'Tang', 'Dhang', 'Thang',
	'Dae', 'Tae', 'Dai', 'Dea', 'Day', 'Tai', 'Tay', 'Tea',
	'Do', 'To', 'Dho', 'Doh', 'Toe', 'Doe', 'Toh',
	'Dokgo', 'Tokko', 'Dokko', 'Toko', 'Doko', 'Dockko', 'Dogko', 'Togko', 'Tokgo',
	'Don', 'Ton', 'Dohn', 'Tohn',
	'Dong', 'Tong', 'Dhong', 'Thong',
	'Dongbang', 'Tongbang', 'Tongpang', 'Dongpang',
	'Du', 'Tu', 'Doo', 'Do', 'Dou', 'Tou', 'To', 'Too',
	'Deung',
	'Deungjeong',
	'Ra', 'Rah',
	'Ran', 'Rahn',
	'Rang',
	'Ryeo', 'Ryuh',
	'Roh',
	'Roe', 'Roi',
	'Ryu', 'Ryou', 'Rou', 'Ryoo', 'Yu', 'Yoo', 'You', 'Yuh',
	'Ree',
	'Rim', 'Leem',
	'Ma', 'Mah', 'Mar',
	'Man', 'Mann', 'Mahn',
	'Mangjeol', 'Mangjŏl', 'Mangjul', 'Mangjuhl', 'Mangjoul',
	'Mae', 'May', 'Mea', 'Mai',
	'Maeng', 'Maing', 'Meang',
	'Myeong', 'Myŏng', 'Myung', 'Myoung', 'Myong',
	'Mo', 'Moh', 'Moe',
	'Mok', 'Mock', 'Mog', 'Mork',
	'Myo', 'Myoh', 'Mio',
	'Mu', 'Moo',
	'Mubon',
	'Muk', 'Mook',
	'Mun', 'Moon', 'Muhn',
	'Mi', 'Mee', 'Mih', 'Meeh', 'Me',
	'Min', 'Minn', 'Mihn', 'Mean',
	'Bak', 'Pak', 'Park', 'Back', 'Bahk', 'Pahk',
	'Ban', 'Pan', 'Bahn', 'Pahn', 'Bhan', 'Van',
	'Bang', 'Pang', 'Bhang', 'Bahng', 'Pahng', 'Phang',
	'Bae', 'Pae', 'Bai', 'Bea', 'Pai', 'Bay', 'Pay',
	'Baek', 'Paek', 'Baik', 'Back', 'Paik', 'Pack', 'Beak',
	'Beon', 'Bun', 'Burn',
	'Beom', 'Pŏm', 'Bum', 'Bom', 'Peom', 'Pum', 'Puhm', 'Buhm',
	'Byeon', 'Pyŏn', 'Byun', 'Byon', 'Pyun', 'Byoun', 'Pyon', 'Pyoun', 'Pyeon',
	'Bo', 'Po', 'Boh', 'Poh',
	'Bok', 'Pok', 'Pock', 'Bog', 'Pog', 'Bock',
	'Bokho', 'Pokho', 'Pockhoh', 'Boghoh', 'Poghoh', 'Bockhoh',
	'Bong', 'Pong', 'Bhong', 'Bohng', 'Pohng', 'Vong',
	'Bu', 'Pu', 'Boo', 'Bou', 'Poo', 'Booh', 'Buh', 'Pou', 'Pooh',
	'Bi', 'Pi', 'Bee', 'Pee', 'Bih', 'Bhi', 'Pih', 'Phi',
	'Bin', 'Pin', 'Been', 'Pihn', 'Phin', 'Bean', 'Bihn', 'Pean',
	'Bing', 'Ping',
	'Buyeo', 'Puyŏ',
	'Sa', 'Sah', 'Sar',
	'Sagong', 'Sakong', 'Sagoung', 'Sakoung',
	'San', 'Sahn', 'Sarn',
	'Sam', 'Sahm', 'Sarm',
	'Sang', 'Sahng',
	'Seo', 'Sŏ', 'Suh', 'Surh', 'Su', 'Sur', 'So', 'Seoh',
	'Seomun', 'Sŏmun', 'Suhmun', 'Suhmoon', 'Seomoon', 'Somoon',
	'Seok', 'Sŏk', 'Suk', 'Sok', 'Suck', 'Sek', 'Such',
	'Seon', 'Sŏn', 'Sun', 'Son', 'Suhn', 'Sen',
	'Seonu', 'Sŏnu', 'Sunwoo', 'Seonwoo', 'Sonu', 'Sunoo', 'Sunwou', 'Seonwu', 'Sonwu',
	'Seol', 'Sŏl', 'Sul', 'Seul', 'Sol', 'Sull',
	'Seob', 'Sub', 'Subb', 'Sup', 'Seop',
	'Seong', 'Sŏng', 'Sung', 'Soung', 'Song', 'Shèng',
	'So', 'Soh', 'Sou', 'Sow',
	'Son', 'Sohn', 'Soun',
	'Song', 'Soung',
	'Su', 'Soo', 'Sooh',
	'Sun', 'Soon',
	'Seung', 'Sŭng', 'Sung',
	'Si', 'Shi', 'Shie', 'Shee', 'Sie', 'Sea', 'See',
	'Sin', 'Shin', 'Shinn', 'Sheen', 'Seen', 'Sinn', 'Cynn',
	'Sim', 'Shim', 'Seem', 'Sheem', 'Sihm',
	'A', 'Ah', 'Ar',
	'An', 'Ahn', 'Arn', 'Aan',
	'Ae', 'Ay', 'Ai', 'Ea',
	'Ya', 'Yah', 'Yar',
	'Yang', 'Ryang', 'Lyang',
	'Eo', 'Ŏ', 'Uh', 'Urh', 'Eoh',
	'Eogeum', 'Ŏgŭm', 'Eokeum', 'Okeum', 'Okum', 'Ukeum', 'Ugeum', 'Ukum', 'Uhgeum', 'Uhkuem',
	'Eom', 'Ŏm', 'Um', 'Uhm', 'Oum', 'Ohm',
	'Yeo', 'Ryeo', 'Yŏ', 'Ryŏ', 'Yu', 'Yo', 'Yeu', 'Yuh', 'Yoh',
	'Yeon', 'Ryeon', 'Yŏn', 'Ryŏn', 'Youn', 'Yun', 'Yon', 'Yeun', 'Yeoun', 'Yuhn',
	'Yeom', 'Ryeom', 'Yŏm', 'Ryŏm', 'Yum', 'Youm', 'Yeum', 'Yom', 'Yeoum',
	'Yeop', 'Yŏp', 'Yeob', 'Youb', 'Yub', 'Yup', 'Yob',
	'Yeong', 'Yŏng', 'Young', 'Yung',
	'Ye', 'Yeh',
	'O', 'Oh', 'Oe', 'Au', 'Ou', 'Awh',
	'Ok', 'Ock', 'Ohk', 'Oak', 'Og', 'Ohg', 'Oag', 'Ogh',
	'On', 'Ohn', 'Ohnn',
	'Ong', 'Ohng', 'Oung',
	'Wan', 'Warn',
	'Wang',
	'Yo', 'You',
	'Yong', 'Ryong', 'Lyong',
	'U', 'Woo', 'Wu', 'Ou', 'Wo', 'Uh',
	'Un', 'Woon', 'Wun', 'Whun', 'Wuhn',
	'Won', 'Wŏn', 'Weon', 'Woen', 'Wone', 'Wun', 'One', 'Worn', 'Warn',
	'Wi', 'Wee', 'We', 'Wie',
	'Yu', 'Ryu', 'Yoo', 'You',
	'Yuk', 'Ryuk', 'Yook', 'Youk', 'Yug', 'Yuck',
	'Yun', 'Yoon', 'Youn', 'Yune', 'Yeun',
	'Eun', 'Ŭn', 'Ehn', 'Enn', 'Unn', 'En', 'Un',
	'Eum', 'Ŭm', 'Um', 'Em', 'Yeum', 'Uem',
	'I', 'Ri', 'Yi', 'Lee', 'Rhee', 'Ree', 'Reeh', 'Ee', 'Rie', 'Rhie',
	'In', 'Ihn', 'Yin', 'Inn', 'Lin', 'Ean',
	'Im', 'Rim', 'Lim', 'Yim', 'Leem', 'Rhim', 'Eam',
	'Ja', 'Cha', 'Jar',
	'Jang', 'Chang', 'Jahng', 'Jhang', 'Zang',
	'Jeon', 'Chŏn', 'Jun', 'Chun', 'Chon', 'Cheon',
	'Jeom', 'Chŏm', 'Jum',
	'Jeong', 'Chŏng', 'Chung', 'Jung', 'Joung', 'Chong', 'Cheong', 'Choung',
	'Je', 'Che', 'Jae', 'Jea', 'Jei', 'Jhe',
	'Jegal', 'Chegal', 'Jaegal', 'Jekal', 'Jeagal', 'Jikal', 'Chekal',
	'Jo', 'Cho', 'Joe', 'Joh', 'Jou',
	'Jong', 'Chong',
	'Jwa', 'Chwa', 'Joa', 'Choa',
	'Ju', 'Chu', 'Joo', 'Choo', 'Chow', 'Jou', 'Zoo', 'Jew', 'Zu',
	'Jeung', 'Chŭng', 'Jung', 'Cheung', 'Chung',
	'Ji', 'Chi', 'Jee', 'Gi', 'Chee', 'Gee', 'Jhi',
	'Jin', 'Chin', 'Jeen', 'Gin',
	'Cha', "Ch'a", 'Char', 'Chah',
	'Chang', "Ch'ang", 'Chahng',
	'Chae', "Ch'ae", 'Chai', 'Che', 'Chea', 'Chay',
	'Cheon', "Ch'ŏn", 'Chun', 'Chon', 'Choun',
	'Cho', "Ch'o", 'Chu', 'Chou', 'Choh',
	'Choe', "Ch'oe", 'Choi', 'Che', 'Choy', 'Chwe', 'Chey',
	'Chu', "Ch'u", 'Choo', 'Chou', 'Chyu',
	'Tak', "T'ak", 'Tark', 'Tag', 'Tack', 'Tahk',
	'Tan', "T'an", 'Tahn', 'Tann',
	'Tae', "T'ae", 'Tai', 'Tay', 'Tea', 'Thae',
	'Pan', "P'an", 'Pahn', 'Phan', 'Parn', 'Pann',
	'Paeng', "P'aeng", 'Pang', 'Paing', 'Peng', 'Peang',
	'Pyeon', "P'yŏn", 'Pyun', 'Pyon', 'Pyoun', 'Pyen',
	'Pyeong', "P'yŏng", 'Pyung', 'Pyong', 'Pyoung', 'Pyeng',
	'Po', "P'o", 'Pho', 'Poh', 'Paul', 'For', 'Four',
	'Pyo', "P'yo", 'Phyo', 'Pio', 'Peo', 'Pyoh', 'Pyou',
	'Pung', "P'ung", 'Poong', 'Puhng', 'Poohng',
	'Pi', "P'i", 'Pee', 'Phee', 'Phi', 'Phy', 'Pih', 'Fee',
	'Pil', "P'il", 'Phil', 'Peel', 'Fill', 'Feel',
	'Ha', 'Hah', 'Har',
	'Hak', 'Hag', 'Hahk', 'Hahg', 'Hack',
	'Han', 'Hahn', 'Hann', 'Hanh',
	'Ham', 'Hahm', 'Hamm', 'Haam', 'Harm',
	'Hae', 'Hay', 'Hai', 'Hea',
	'Heo', 'Hŏ', 'Hur', 'Huh', 'Her', 'Hu', 'Ho', 'Hoh', 'Heoh',
	'Hyeon', 'Hyŏn', 'Hyun', 'Hyon', 'Hyoun',
	'Hyeong', 'Hyŏng', 'Hyung', 'Hyoung', 'Hyong', 'Hyeung',
	'Ho', 'Hoh',
	'Hong', 'Houng', 'Hoong', 'Hung',
	'Hwa', 'Howa', 'Hoa', 'Wha', 'Hua',
	'Hwang', 'Whang', 'Whong',
	'Hwangmok', 'Whangmock', 'Wangmok',
	'Hwangbo', 'Hwangpo', 'Whangpoh',
	'Hu', 'Hoo', 'Hooh', 'Huh'
]

family_names_vietnamese = \
[
	'Nguyễn', 'Nguyen', 'Trần', 'Tran', 'Lê', 'Le', 'Phạm', 'Hoàng', 'Hoang', 'Huỳnh', 'Huynh', 'Vũ', 'Võ', 'Vu', 'Vo', 'Phan', 'Trương', 'Truong',
	'Bùi', 'Bui', 'Đặng', 'Dang', 'Đỗ', 'Do', 'Ngô', 'Ngo', 'Hồ', 'Dương', 'Duong', 'Đinh', 'Dinh', 'Ái', 'An', 'Ân', 'Bạch', 'Bành', 'Bao', 'Biên', 'Biện',
	'Cam', 'Cảnh', 'Cảnh', 'Cao', 'Cái', 'Cát', 'Chân', 'Châu', 'Chiêm', 'Chu', 'Chung', 'Chử', 'Cổ', 'Cù', 'Cung', 'Cung', 'Củng', 'Cừu', 'Dịch', 'Diệp',
	'Doãn', 'Dũ', 'Dung', 'Dư', 'Dữu', 'Đái', 'Đàm', 'Đào', 'Đậu', 'Điền', 'Đoàn', 'Đồ', 'Đồng', 'Đổng', 'Đường', 'Giả', 'Giải', 'Gia_Cát', 'Giản', 'Giang',
	'Giáp', 'Hà', 'Hạ', 'Hậ', 'Hác', 'Hàn', 'Hầu', 'Hình', 'Hoa', 'Hoắc', 'Hoạn', 'Hồng', 'Hứa', 'Hướng', 'Hy', 'Kha', 'Khâu', 'Khổng', 'Khuất', 'Kiều', 'Kim',
	'Kỳ', 'Kỷ', 'La', 'Lạc', 'Lại', 'Lam', 'Lăng', 'Lãnh', 'Lâm', 'Lận', 'Lệ', 'Liên', 'Liêu', 'Liễu', 'Long', 'Lôi', 'Lục', 'Lư', 'Lữ', 'Lương', 'Lưu', 'Mã', 'Mạc',
	'Mạch', 'Mai', 'Mạnh', 'Mao', 'Mẫn', 'Miêu', 'Minh', 'Mông', 'Ngân', 'Nghê', 'Nghiêm', 'Ngư', 'Ngưu', 'Nhạc', 'Nhan', 'Nhâm', 'Nhiếp', 'Nhiều',
	'Nhung', 'Ninh', 'Nông', 'Ôn', 'Ổn', 'Ông', 'Phí', 'Phó', 'Phong', 'Phòng', 'Phù', 'Phùng', 'Phương', 'Quách', 'Quan', 'Quản', 'Quang', 'Quảng',
	'Quế', 'Quyền', 'Sài', 'Sầm', 'Sử', 'Tạ', 'Tào', 'Tăng', 'Tân', 'Tần', 'Tất', 'Tề', 'Thạch', 'Thai', 'Thái', 'Thang', 'Thành', 'Thảo', 'Thân', 'Thi', 'Thích',
	'Thiện', 'Thiệu', 'Thôi', 'Thủy', 'Thư', 'Thường', 'Tiền', 'Tiết', 'Tiêu', 'Tiêu', 'Tô', 'Tôn', 'Tôn_Thất', 'Tông', 'Tống', 'Trác', 'Trạch', 'Trại',
	'Trang', 'Trầm', 'Trâu', 'Trì', 'Triệu', 'Trịnh', 'Từ', 'Tư_Mã', 'Tưởng', 'Úc', 'Ứng', 'Vạn', 'Văn', 'Vân', 'Vi', 'Vĩnh', 'Vũ_Văn', 'Vương', 'Vưu', 'Xà',
	'Xầm', 'Xế', 'Yên', 'Yến'
]

# Japanese Kanji family name probabilities (Enamdict)

family_name_japanese_probabilities = \
{
	'一': 0.1658, '丁': 0.7938, '七': 0.2536, '万': 0.2146, '丈': 0.1965, '三': 0.3021, '上': 0.9772,
	'下': 0.9876, '不': 0.4061, '与': 0.2753, '丑': 0.6923, '且': 0.3750, '世': 0.1556, '丘': 0.5838,
	'丙': 0.0385, '丞': 0.0061, '両': 0.8679, '並': 0.8824, '中': 0.9236, '串': 1.0000, '丸': 0.8272,
	'丹': 0.6935, '主': 0.5837, '乃': 0.0767, '久': 0.4980, '之': 0.1936, '乕': 0.6296, '乗': 0.6857,
	'乘': 0.9583, '乙': 0.3917, '九': 0.4545, '也': 0.0252, '乳': 0.6818, '乾': 0.4881, '亀': 0.6402,
	'了': 0.1449, '予': 0.0905, '事': 0.5319, '二': 0.2442, '五': 0.4545, '井': 0.9549, '亘': 0.1158,
	'亜': 0.0206, '亞': 0.0000, '交': 0.6061, '亥': 0.3368, '亦': 0.8226, '亨': 0.0309, '享': 0.0400,
	'京': 0.5118, '亭': 0.5000, '亮': 0.0061, '人': 0.0839, '仁': 0.2734, '今': 0.7922, '介': 0.0157,
	'仏': 0.9146, '仕': 0.8250, '他': 0.2500, '付': 0.9565, '仙': 0.4380, '代': 0.2340, '令': 0.0481,
	'以': 0.0531, '仮': 0.9310, '仰': 0.2500, '仲': 0.8539, '任': 0.3540, '企': 0.1667, '伊': 0.5423,
	'伍': 0.1417, '伎': 0.0513, '伏': 0.9634, '休': 0.6377, '会': 0.4764, '伝': 0.5445, '伯': 0.3187,
	'伴': 0.4348, '伶': 0.0000, '伸': 0.0593, '似': 0.2211, '伽': 0.0456, '但': 0.9412, '位': 0.5843,
	'住': 0.8587, '佐': 0.4643, '佑': 0.0049, '何': 0.5000, '余': 0.5268, '佛': 1.0000, '作': 0.3308,
	'佳': 0.0191, '使': 0.6182, '侃': 0.0455, '來': 0.5030, '侍': 0.4211, '侑': 0.0023, '供': 0.8214,
	'依': 0.0529, '俊': 0.0427, '保': 0.5632, '信': 0.2871, '俣': 0.9915, '修': 0.0890, '俵': 0.9722,
	'俶': 0.0000, '倉': 0.9350, '倍': 0.7500, '倖': 0.0411, '倫': 0.0106, '倭': 0.1348, '倶': 0.2857,
	'偉': 0.0260, '健': 0.0694, '偲': 0.0000, '側': 1.0000, '傍': 0.9565, '傑': 0.1818, '備': 0.6190,
	'傳': 0.8254, '像': 0.7143, '僧': 0.7727, '儀': 0.4135, '億': 0.5000, '優': 0.0076, '允': 0.0189,
	'元': 0.6627, '兄': 0.3158, '充': 0.0134, '兆': 0.0513, '先': 0.8802, '光': 0.3106, '克': 0.0229,
	'免': 0.9474, '兎': 0.2105, '児': 0.4258, '兒': 0.7838, '兜': 0.8276, '入': 0.9395, '全': 0.2011,
	'八': 0.5451, '公': 0.1103, '六': 0.4123, '共': 0.1351, '兵': 0.2637, '其': 0.5577, '具': 0.4929,
	'典': 0.0193, '兼': 0.6098, '内': 0.9778, '円': 0.4808, '冠': 0.5111, '冨': 0.8081, '冬': 0.1176,
	'冲': 0.8065, '冴': 0.0483, '冶': 0.4144, '冷': 0.5641, '凌': 0.1458, '凖': 0.0000, '凛': 0.0028,
	'凜': 0.0000, '凡': 0.0395, '処': 0.6667, '凪': 0.0292, '凱': 0.0217, '出': 0.8735, '刀': 0.6973,
	'刃': 0.2703, '分': 0.9895, '切': 0.9519, '刈': 0.9533, '初': 0.3094, '判': 0.7727, '別': 0.9711,
	'利': 0.2102, '制': 0.0455, '刺': 0.9286, '則': 0.2444, '剋': 0.0000, '前': 0.9697, '剛': 0.1011,
	'剣': 0.4557, '副': 0.8902, '剱': 1.0000, '割': 1.0000, '創': 0.0312, '力': 0.6284, '功': 0.0632,
	'加': 0.3689, '助': 0.0866, '努': 0.0263, '励': 0.0833, '勅': 0.6875, '勇': 0.1873, '勉': 0.0312,
	'動': 0.8485, '勘': 0.4552, '務': 0.4918, '勝': 0.3671, '勢': 0.6526, '勤': 0.1714, '勧': 0.5909,
	'勲': 0.0000, '匂': 0.8936, '包': 0.5065, '化': 0.5862, '北': 0.9076, '匠': 0.3023, '匡': 0.0143,
	'十': 0.4098, '千': 0.2144, '升': 0.7707, '午': 0.4079, '半': 0.6821, '卓': 0.0592, '協': 0.0741,
	'南': 0.4035, '博': 0.0337, '卜': 0.7500, '占': 0.8846, '卯': 0.3624, '印': 0.9265, '卿': 0.0357,
	'厚': 0.2563, '原': 0.9792, '厨': 0.8462, '厳': 0.2258, '去': 0.7500, '参': 0.4769, '又': 0.6948,
	'叉': 0.1190, '及': 0.6600, '友': 0.2072, '双': 0.4510, '反': 0.9905, '収': 0.0476, '叔': 0.0278,
	'取': 0.9700, '受': 0.7292, '叡': 0.1429, '口': 0.9860, '古': 0.8066, '句': 0.0879, '只': 0.6389,
	'叫': 0.0294, '可': 0.1165, '台': 0.8133, '史': 0.0120, '右': 0.2033, '叶': 0.2295, '司': 0.2443,
	'合': 0.6818, '吉': 0.4427, '同': 0.6923, '名': 0.5460, '后': 0.2642, '吏': 0.0000, '吐': 0.4000,
	'向': 0.8933, '君': 0.4562, '吟': 0.0893, '吹': 0.6739, '吾': 0.1646, '呂': 0.4609, '呉': 0.8058,
	'告': 0.8095, '呑': 0.8056, '周': 0.2638, '味': 0.6022, '呼': 0.0734, '命': 0.2716, '和': 0.3276,
	'咲': 0.0575, '哀': 0.2800, '品': 0.8085, '哉': 0.0168, '員': 0.1600, '哲': 0.0204, '唄': 0.3103,
	'唐': 0.9293, '唯': 0.0518, '唱': 0.0286, '問': 0.8462, '啓': 0.0163, '善': 0.2550, '喜': 0.2678,
	'喬': 0.0513, '喰': 1.0000, '嗣': 0.0236, '嘉': 0.3016, '器': 0.3953, '四': 0.4178, '回': 0.8077,
	'因': 0.6667, '団': 0.4808, '図': 0.6024, '固': 0.3514, '国': 0.6788, '囿': 1.0000, '圀': 0.0625,
	'圃': 0.2826, '國': 0.8939, '園': 0.8175, '圓': 0.9365, '團': 0.7727, '土': 0.8482, '在': 0.6059,
	'圭': 0.0148, '地': 0.9318, '坂': 0.9865, '均': 0.0141, '坊': 0.8866, '坐': 0.8684, '坡': 0.3182,
	'坦': 0.1143, '坪': 0.9491, '垂': 0.7808, '垢': 0.0976, '垣': 0.9942, '垰': 1.0000, '城': 0.7956,
	'埜': 0.9535, '埴': 0.9167, '執': 0.8065, '基': 0.0976, '埼': 0.9646, '堀': 0.9939, '堂': 0.7529,
	'堅': 0.5440, '堤': 0.9062, '堰': 1.0000, '場': 0.9915, '堺': 1.0000, '塔': 0.7467, '塗': 0.9615,
	'塘': 0.7719, '塙': 0.9697, '塚': 0.9957, '塩': 0.9764, '塲': 1.0000, '境': 0.9326, '増': 0.8227,
	'墨': 0.7119, '壁': 0.9633, '士': 0.3738, '壬': 0.4000, '壮': 0.0463, '声': 0.0794, '壱': 0.0719,
	'売': 0.7917, '壷': 0.6863, '壺': 0.9143, '壽': 0.3662, '夏': 0.0720, '夕': 0.0476, '外': 0.6524,
	'夘': 0.7586, '多': 0.4494, '夛': 0.9194, '夜': 0.0698, '夢': 0.0244, '大': 0.7798, '天': 0.5101,
	'太': 0.1522, '夫': 0.0358, '央': 0.0169, '夷': 0.6905, '奇': 0.4062, '奈': 0.0714, '奉': 0.1714,
	'奎': 0.0204, '奏': 0.0203, '契': 0.1364, '奚': 0.0400, '奥': 0.9554, '奧': 1.0000, '奨': 0.0233,
	'女': 0.1715, '奴': 0.4545, '好': 0.2197, '如': 0.1902, '妃': 0.0084, '妙': 0.3122, '妥': 0.0000,
	'妹': 0.4906, '妻': 0.9623, '姉': 0.6250, '始': 0.1803, '姓': 0.9872, '委': 0.0220, '姥': 0.9714,
	'姫': 0.0533, '姿': 0.0455, '威': 0.1092, '娘': 0.0541, '婁': 0.1071, '婦': 0.2549, '媛': 0.0159,
	'嬉': 0.1039, '子': 0.0542, '孔': 0.1067, '字': 0.7263, '存': 0.0208, '孚': 0.0417, '孝': 0.0908,
	'孟': 0.0727, '季': 0.0426, '孤': 0.3478, '学': 0.2044, '孫': 0.4771, '宅': 0.8545, '宇': 0.6215,
	'守': 0.6033, '安': 0.3869, '完': 0.2019, '宍': 0.9429, '宏': 0.0181, '宗': 0.4094, '官': 0.8312,
	'宙': 0.0143, '定': 0.4294, '宜': 0.2402, '宝': 0.6372, '実': 0.0529, '宣': 0.0673, '室': 0.9673,
	'宥': 0.0247, '宮': 0.8776, '宰': 0.2679, '宵': 0.1579, '家': 0.8860, '容': 0.0172, '宿': 0.9371,
	'寂': 0.0435, '寄': 0.9356, '寅': 0.3223, '密': 0.5000, '富': 0.5654, '寒': 0.6855, '寛': 0.0562,
	'實': 0.7055, '寧': 0.0265, '寳': 1.0000, '寶': 1.0000, '寸': 0.5246, '寺': 0.9888, '対': 0.8727,
	'寿': 0.1136, '専': 0.3714, '射': 0.9000, '将': 0.0717, '尉': 0.0400, '尊': 0.2061, '尋': 0.2308,
	'對': 1.0000, '導': 0.2609, '小': 0.7936, '少': 0.7188, '尚': 0.0289, '尭': 0.0413, '就': 0.0698,
	'尹': 0.2857, '尺': 0.8571, '尻': 0.9949, '尼': 0.8286, '尾': 0.9477, '居': 0.9316, '屋': 0.9881,
	'展': 0.0086, '屡': 0.0000, '山': 0.8866, '岐': 0.5167, '岑': 0.4681, '岡': 0.9823, '岩': 0.9191,
	'岬': 0.4444, '岱': 0.1786, '岳': 0.4806, '岸': 0.9338, '峠': 0.9765, '峡': 0.3824, '峨': 0.8250,
	'峪': 1.0000, '峯': 0.8017, '峰': 0.4933, '島': 0.9774, '峻': 0.0328, '崇': 0.1180, '崎': 0.9864,
	'嵐': 0.7349, '嵜': 1.0000, '嵩': 0.4757, '嵯': 0.3019, '嶋': 0.9893, '嶌': 1.0000, '嶺': 0.5867,
	'嶽': 0.9943, '巌': 0.4538, '巖': 0.8056, '川': 0.9670, '州': 0.3702, '巣': 0.8351, '工': 0.7798,
	'左': 0.2711, '巧': 0.0563, '巨': 0.2705, '巫': 0.3810, '差': 0.6607, '己': 0.0618, '已': 0.1538,
	'巳': 0.0681, '巴': 0.0978, '巻': 0.8657, '巾': 0.3115, '市': 0.3678, '布': 0.5509, '帆': 0.0723,
	'希': 0.0162, '帝': 0.2593, '師': 0.7918, '帯': 0.8438, '帰': 0.5349, '常': 0.5218, '幅': 1.0000,
	'幡': 0.9612, '幣': 0.9667, '干': 0.7763, '平': 0.6338, '年': 0.2606, '幸': 0.1831, '幹': 0.0310,
	'幽': 0.1136, '幾': 0.3158, '広': 0.4810, '庄': 0.6942, '床': 0.9839, '底': 0.8667, '店': 0.9524,
	'庚': 0.1481, '府': 0.9128, '度': 0.7381, '座': 0.9211, '庫': 0.5286, '庭': 0.9125, '庵': 0.5475,
	'康': 0.0722, '庸': 0.0065, '廉': 0.2178, '廣': 0.8132, '延': 0.4914, '廷': 0.4545, '建': 0.3944,
	'廻': 0.9540, '廼': 0.8889, '廿': 0.8846, '弁': 0.4154, '弌': 0.0303, '式': 0.5698, '弐': 0.2727,
	'弓': 0.3391, '引': 0.9697, '弘': 0.1763, '弥': 0.0942, '弦': 0.2328, '張': 0.8744, '強': 0.2500,
	'弼': 0.0000, '弾': 0.6957, '彌': 0.3731, '当': 0.8424, '彗': 0.0179, '形': 0.9813, '彦': 0.0397,
	'彩': 0.0155, '彪': 0.0000, '彬': 0.0080, '彰': 0.0063, '影': 0.5249, '役': 0.9268, '彼': 0.6250,
	'往': 0.5000, '征': 0.0455, '径': 0.0476, '待': 0.7812, '律': 0.0227, '後': 0.9779, '徐': 0.8333,
	'従': 0.2000, '得': 0.3557, '御': 0.8493, '復': 0.2121, '微': 0.0612, '徳': 0.4286, '徹': 0.0429,
	'心': 0.0317, '忍': 0.4565, '志': 0.2891, '応': 0.4379, '忠': 0.1215, '快': 0.0581, '念': 0.6462,
	'怒': 0.8696, '怜': 0.0000, '思': 0.0818, '怡': 0.1905, '性': 0.5918, '恋': 0.0388, '恒': 0.2397,
	'恕': 0.0000, '恩': 0.4714, '恭': 0.0119, '息': 0.5238, '恵': 0.0650, '悌': 0.0000, '悟': 0.1053,
	'悠': 0.0107, '悦': 0.1026, '悳': 0.1154, '情': 0.2667, '惇': 0.0000, '惟': 0.0698, '惠': 0.1977,
	'惣': 0.5787, '想': 0.0597, '愁': 0.0000, '愉': 0.0000, '意': 0.0600, '愚': 0.1250, '愛': 0.0385,
	'愼': 0.1333, '慈': 0.1366, '慎': 0.0932, '慧': 0.0062, '慶': 0.3150, '憂': 0.0342, '憲': 0.0050,
	'應': 0.9412, '懐': 0.3043, '懸': 0.9259, '戎': 0.9574, '成': 0.3610, '我': 0.7072, '戒': 0.5161,
	'戸': 0.9760, '房': 0.4586, '所': 0.9320, '扇': 0.5227, '手': 0.9628, '才': 0.6375, '打': 0.9606,
	'扶': 0.0493, '承': 0.0145, '抄': 0.0000, '折': 0.8286, '抜': 0.9273, '抱': 0.3421, '押': 0.9787,
	'拓': 0.0420, '拝': 0.9211, '拡': 0.0000, '拳': 0.0476, '拾': 0.4783, '持': 0.9061, '指': 0.9565,
	'挙': 0.3200, '振': 0.7119, '挽': 0.8000, '捨': 0.2444, '捷': 0.0105, '捺': 0.0225, '掘': 1.0000,
	'掛': 1.0000, '採': 0.1818, '提': 0.8182, '揖': 0.9688, '揚': 0.6220, '揮': 0.0400, '揺': 0.0256,
	'摂': 0.2045, '摘': 0.0753, '摩': 0.3720, '摺': 1.0000, '撫': 0.6970, '播': 0.9661, '操': 0.2447,
	'支': 0.2436, '改': 0.8367, '放': 0.4828, '政': 0.3346, '故': 0.7778, '敏': 0.0235, '教': 0.0873,
	'敞': 0.1071, '敦': 0.1648, '敬': 0.0233, '数': 0.5363, '整': 0.0000, '敷': 0.9725, '數': 0.9667,
	'文': 0.1368, '斉': 0.6160, '斌': 0.0000, '斎': 0.5015, '斐': 0.3737, '斗': 0.1788, '料': 0.9565,
	'斤': 0.0000, '斧': 0.9062, '斯': 0.8182, '新': 0.8147, '方': 0.7347, '於': 0.2604, '施': 0.7778,
	'旗': 0.7379, '日': 0.4771, '旦': 0.3611, '旧': 0.8095, '旨': 0.4412, '早': 0.2579, '旬': 0.0000,
	'旭': 0.3118, '旺': 0.0449, '昂': 0.0303, '昆': 0.8966, '昇': 0.1238, '昊': 0.0909, '昌': 0.0689,
	'明': 0.2639, '易': 0.5000, '星': 0.2372, '映': 0.0018, '春': 0.2088, '昭': 0.0946, '是': 0.5112,
	'昴': 0.0000, '昼': 0.6400, '晁': 0.0833, '時': 0.4711, '晃': 0.0318, '晋': 0.0909, '晏': 0.0236,
	'晟': 0.0000, '晧': 0.0000, '晨': 0.0441, '晩': 0.1667, '普': 0.4086, '景': 0.2292, '晴': 0.0762,
	'晶': 0.0222, '智': 0.0969, '暁': 0.0397, '暉': 0.0394, '暎': 0.0000, '暖': 0.0083, '暢': 0.0055,
	'暮': 0.6269, '曙': 0.0323, '曜': 0.0732, '曲': 0.8983, '曳': 0.9730, '更': 0.3800, '書': 0.4242,
	'曹': 0.3125, '曽': 0.9298, '曾': 0.9861, '替': 1.0000, '最': 0.6064, '會': 0.9070, '月': 0.3472,
	'有': 0.1865, '朋': 0.0355, '服': 0.9130, '朔': 0.1800, '朗': 0.0016, '望': 0.0664, '朝': 0.3933,
	'期': 0.5909, '木': 0.8872, '未': 0.0176, '末': 0.7300, '本': 0.9669, '札': 0.9048, '朱': 0.2142,
	'朴': 0.6892, '朽': 0.8684, '杉': 0.8851, '李': 0.0530, '杏': 0.0273, '材': 0.6667, '村': 0.9171,
	'杖': 0.6111, '杜': 0.1833, '束': 0.6832, '条': 0.8556, '杢': 0.7949, '杣': 0.9600, '来': 0.3321,
	'杭': 0.9250, '東': 0.7831, '杵': 0.9123, '松': 0.7548, '板': 0.9822, '林': 0.8200, '枚': 0.8095,
	'果': 0.0051, '枝': 0.1921, '枡': 0.9773, '枦': 1.0000, '枩': 0.9000, '架': 0.0462, '柄': 0.8315,
	'柊': 0.3878, '柏': 0.8629, '柑': 0.3429, '染': 0.6934, '柔': 0.0357, '柘': 0.9355, '柚': 0.1511,
	'柱': 0.6897, '柳': 0.8225, '柴': 0.9182, '柵': 0.9310, '柾': 0.4146, '柿': 0.9119, '栂': 0.9697,
	'栃': 0.9901, '栄': 0.2079, '栖': 0.7222, '栗': 0.8659, '栞': 0.0536, '栢': 0.9524, '株': 0.9444,
	'根': 0.8448, '格': 0.3077, '桁': 0.9130, '桂': 0.2456, '桃': 0.1960, '案': 0.4615, '桐': 0.6818,
	'桑': 0.8166, '桜': 0.1647, '桝': 0.9669, '桧': 0.8932, '桶': 1.0000, '梁': 0.8627, '梅': 0.6301,
	'梓': 0.0744, '條': 0.8800, '梠': 0.9524, '梢': 0.0366, '梧': 0.2157, '梨': 0.0406, '梯': 0.7273,
	'梶': 0.9381, '棒': 0.9630, '棚': 0.9895, '棟': 0.7474, '森': 0.9185, '椋': 0.8409, '植': 0.8660,
	'椎': 0.6825, '椙': 0.9643, '椛': 0.8222, '椰': 0.1000, '椿': 0.7654, '楊': 0.5714, '楓': 0.0458,
	'楚': 0.5405, '楠': 0.6517, '楢': 0.7215, '楫': 0.8148, '業': 0.3243, '楯': 0.7647, '楳': 0.8846,
	'極': 0.6866, '楼': 0.2024, '楽': 0.4026, '榊': 0.9722, '榎': 0.9111, '榛': 0.6197, '榮': 0.5502,
	'槁': 1.0000, '槇': 0.8507, '構': 0.9600, '槌': 0.7397, '槍': 1.0000, '槙': 0.7609, '槻': 0.5969,
	'樂': 0.8182, '樋': 0.9874, '樗': 0.8485, '樟': 0.6400, '模': 0.4643, '権': 0.5584, '横': 0.9864,
	'樫': 0.9781, '樵': 0.1739, '樹': 0.1117, '樺': 0.3131, '樽': 0.9737, '橋': 0.9257, '橘': 0.6667,
	'橙': 0.2857, '機': 0.3125, '檀': 0.9429, '檜': 0.9818, '櫃': 1.0000, '櫛': 0.9841, '櫨': 0.9615,
	'櫻': 0.7424, '欠': 0.9655, '次': 0.2047, '欣': 0.0141, '欧': 0.1774, '欽': 0.0112, '歌': 0.0912,
	'歓': 0.1395, '止': 0.3833, '正': 0.2672, '此': 0.9412, '武': 0.5746, '歩': 0.0388, '歳': 0.5564,
	'殉': 0.0000, '殊': 0.1786, '段': 0.9328, '殿': 0.9700, '毅': 0.0098, '母': 0.6197, '毎': 0.5000,
	'比': 0.5360, '毛': 0.9685, '毬': 0.0694, '氏': 0.6890, '民': 0.2150, '気': 0.4516, '氣': 0.9487,
	'水': 0.5230, '氷': 0.4609, '永': 0.5978, '汀': 0.0921, '求': 0.1552, '汎': 0.0000, '汐': 0.4027,
	'江': 0.3658, '池': 0.9473, '汪': 0.2381, '汰': 0.0702, '汲': 0.6786, '沓': 0.9773, '沖': 0.8911,
	'沙': 0.0225, '沢': 0.9652, '河': 0.9368, '油': 0.9579, '治': 0.2315, '沼': 0.9813, '泉': 0.5789,
	'泊': 0.8548, '泓': 0.6818, '法': 0.5827, '泡': 0.3333, '波': 0.5880, '泥': 0.7333, '泰': 0.0921,
	'泳': 0.0000, '洋': 0.0795, '洗': 0.7027, '洙': 0.0909, '洞': 0.7368, '津': 0.5458, '洪': 0.3333,
	'洲': 0.6311, '洵': 0.0000, '洸': 0.0125, '活': 0.1143, '流': 0.2208, '浄': 0.3664, '浅': 0.7419,
	'浜': 0.9421, '浦': 0.9310, '浩': 0.0103, '浪': 0.7859, '浮': 0.8288, '浴': 0.8750, '海': 0.3723,
	'涌': 0.9020, '涙': 0.0000, '涛': 0.2766, '涯': 0.3333, '涼': 0.0563, '淀': 0.9412, '淑': 0.0101,
	'淡': 0.5556, '深': 0.3750, '淳': 0.1821, '淵': 0.9467, '淺': 0.9091, '添': 0.9604, '清': 0.3677,
	'済': 0.5114, '渉': 0.1250, '渋': 0.9375, '渓': 0.4057, '渕': 0.9825, '渚': 0.0225, '渡': 0.9003,
	'渥': 0.3400, '渦': 0.8571, '温': 0.1182, '港': 0.8085, '湊': 0.8916, '湖': 0.1507, '湛': 0.2692,
	'湧': 0.2967, '湯': 0.9289, '満': 0.3553, '源': 0.4828, '準': 0.0000, '溜': 0.9318, '溝': 1.0000,
	'溪': 0.8085, '滉': 0.0000, '滋': 0.1344, '滑': 0.9756, '滝': 0.9118, '滿': 0.8571, '漁': 0.7742,
	'漆': 0.9524, '演': 0.4000, '漢': 0.5833, '潔': 0.0000, '潟': 1.0000, '潤': 0.0625, '潮': 0.5057,
	'澁': 0.9630, '澄': 0.1838, '澗': 0.8571, '澤': 0.9919, '澪': 0.0190, '濃': 0.8129, '濤': 0.5833,
	'濱': 0.9908, '瀧': 0.9442, '瀬': 0.8266, '灘': 0.9420, '火': 0.3257, '灯': 0.0798, '灰': 0.8689,
	'炎': 0.0625, '炭': 0.9394, '為': 0.3625, '烈': 0.0769, '烏': 0.4463, '無': 0.4950, '然': 0.0820,
	'焼': 0.9250, '煌': 0.1071, '煕': 0.0000, '煙': 0.8125, '照': 0.2152, '熊': 0.8219, '熱': 0.5556,
	'燈': 0.2593, '燎': 0.0000, '燕': 0.1842, '燦': 0.0000, '燿': 0.0333, '爪': 1.0000, '爲': 0.8909,
	'父': 0.8974, '爽': 0.0000, '爾': 0.0813, '片': 0.9588, '牛': 0.7826, '牟': 0.9648, '牧': 0.7516,
	'物': 0.9639, '犬': 0.8690, '狐': 0.7407, '狩': 0.9237, '独': 0.2222, '狭': 0.7903, '猛': 0.0500,
	'猪': 0.7801, '猫': 0.6957, '猶': 0.6042, '猷': 0.0476, '猿': 0.7232, '獅': 0.7879, '玄': 0.2528,
	'玉': 0.6882, '王': 0.6381, '玖': 0.0498, '玲': 0.0021, '珂': 0.1026, '珍': 0.4833, '珠': 0.0609,
	'現': 0.4098, '球': 0.0625, '理': 0.0403, '琉': 0.0204, '琢': 0.0702, '琳': 0.0506, '琴': 0.2412,
	'瑚': 0.0056, '瑛': 0.0054, '瑞': 0.1367, '瑠': 0.0130, '瑩': 0.0800, '瑳': 0.0211, '瑶': 0.0833,
	'璃': 0.0754, '璋': 0.0426, '環': 0.0519, '瓜': 0.8816, '瓢': 0.3043, '瓦': 0.8611, '瓶': 0.5930,
	'甘': 0.7535, '甚': 0.3398, '生': 0.4306, '産': 0.7586, '用': 0.7400, '甫': 0.1571, '田': 0.9789,
	'由': 0.0875, '甲': 0.6819, '申': 0.3281, '男': 0.0456, '町': 0.9570, '界': 0.4872, '畑': 0.9933,
	'畔': 0.8962, '留': 0.3915, '畝': 0.5442, '畠': 0.9968, '畦': 0.8116, '番': 0.9394, '異': 0.2609,
	'當': 0.9496, '疋': 0.9600, '癒': 0.0000, '発': 0.5714, '登': 0.3192, '白': 0.6949, '百': 0.3998,
	'的': 0.7872, '皆': 0.7791, '皇': 0.2188, '皐': 0.0513, '皓': 0.0081, '皮': 0.9615, '皿': 0.9714,
	'盈': 0.0400, '益': 0.4809, '盛': 0.5663, '盟': 0.0385, '盤': 0.7826, '目': 0.9538, '直': 0.1493,
	'相': 0.7758, '省': 0.0075, '眉': 0.1750, '県': 0.9667, '眞': 0.4473, '真': 0.2036, '眠': 0.1034,
	'眸': 0.0385, '眼': 0.6071, '着': 0.9000, '督': 0.0870, '睦': 0.0922, '瞬': 0.0000, '瞭': 0.0000,
	'瞳': 0.0183, '矢': 0.6916, '知': 0.2298, '矩': 0.0437, '石': 0.8433, '砂': 0.2735, '研': 0.1885,
	'砥': 0.9024, '破': 0.7317, '硯': 0.4167, '硲': 1.0000, '碇': 0.9512, '碓': 0.9600, '碕': 0.9697,
	'碧': 0.0638, '碩': 0.1067, '確': 0.1818, '磐': 0.5857, '磨': 0.2783, '磯': 0.8000, '礒': 0.9037,
	'示': 0.2418, '礼': 0.1478, '社': 0.9405, '祇': 0.4800, '祈': 0.0254, '祐': 0.0605, '祖': 0.8286,
	'祝': 0.4956, '神': 0.8916, '祢': 0.5690, '祥': 0.0268, '祭': 0.5312, '禄': 0.1250, '禅': 0.1818,
	'禎': 0.0345, '福': 0.7758, '禧': 0.0500, '禮': 0.7344, '禰': 0.6667, '禾': 0.2500, '禿': 0.8261,
	'秀': 0.0819, '秋': 0.3248, '科': 0.7640, '秦': 0.6145, '秩': 0.3226, '称': 0.4500, '移': 0.6250,
	'稀': 0.0489, '程': 0.8085, '税': 0.8710, '稔': 0.0370, '稗': 1.0000, '稚': 0.0210, '稜': 0.0571,
	'種': 0.5925, '稲': 0.8371, '穀': 0.6800, '穂': 0.1159, '穆': 0.1364, '積': 0.6790, '穎': 0.2727,
	'穏': 0.0698, '穐': 0.9574, '穗': 0.4250, '穣': 0.0000, '穴': 0.9358, '空': 0.1463, '窓': 0.2429,
	'窪': 0.9916, '立': 0.7903, '竜': 0.4636, '章': 0.0180, '童': 0.2895, '竪': 0.9167, '端': 0.8806,
	'竹': 0.7785, '竿': 0.8205, '笑': 0.0249, '笙': 0.0435, '笛': 0.4912, '笠': 0.9321, '符': 0.6667,
	'笹': 0.9026, '筆': 0.8627, '等': 0.3625, '筋': 0.9333, '筑': 0.9057, '筒': 0.9512, '策': 0.0227,
	'箇': 0.9524, '箕': 0.9029, '管': 0.9375, '箭': 0.9600, '箱': 0.9828, '箸': 0.9512, '節': 0.1453,
	'篁': 0.2400, '範': 0.0449, '築': 0.8964, '篠': 0.9522, '篤': 0.0591, '篭': 0.9560, '簑': 0.9286,
	'簗': 0.9655, '簾': 0.9565, '籏': 0.9804, '籐': 0.9831, '籔': 1.0000, '籠': 0.9900, '米': 0.7864,
	'籾': 0.9615, '粂': 0.6275, '粉': 0.8235, '粋': 0.0588, '粒': 0.8182, '粕': 0.9792, '粟': 0.9552,
	'粥': 0.5556, '粧': 0.1786, '精': 0.0995, '糟': 1.0000, '糠': 1.0000, '糸': 0.5101, '系': 0.4783,
	'紀': 0.0879, '紅': 0.2030, '紋': 0.1119, '納': 0.8105, '純': 0.0155, '紗': 0.0039, '紘': 0.0046,
	'紙': 0.9130, '素': 0.1295, '紫': 0.1789, '紬': 0.0455, '細': 0.9489, '紳': 0.0196, '紹': 0.0541,
	'紺': 0.8500, '絃': 0.0000, '組': 0.9180, '経': 0.3016, '結': 0.0728, '絢': 0.0388, '給': 0.9714,
	'統': 0.0734, '絵': 0.0303, '絹': 0.3394, '継': 0.3275, '続': 0.7800, '綜': 0.0303, '維': 0.0277,
	'綱': 0.5275, '網': 0.9783, '綸': 0.0000, '綺': 0.0173, '綾': 0.1933, '綿': 0.7879, '緋': 0.0942,
	'総': 0.2463, '緑': 0.2216, '緒': 0.0709, '編': 0.5000, '緩': 0.1111, '緯': 0.0435, '練': 0.5102,
	'縁': 0.5806, '縄': 0.9278, '縣': 0.9655, '縫': 0.3922, '績': 0.3462, '繁': 0.4067, '織': 0.2309,
	'繩': 1.0000, '繪': 0.5357, '繭': 0.0351, '繰': 0.2553, '置': 0.9067, '羅': 0.2105, '羊': 0.0597,
	'美': 0.0706, '群': 0.5581, '義': 0.1393, '羽': 0.4505, '翁': 0.3689, '翔': 0.0509, '翠': 0.0689,
	'翼': 0.0800, '耀': 0.0288, '老': 0.9006, '考': 0.1129, '者': 0.9348, '而': 0.0323, '耒': 0.9459,
	'耕': 0.1095, '耳': 0.5455, '耶': 0.0278, '耿': 0.1111, '聖': 0.0526, '聞': 0.5588, '聡': 0.0081,
	'聰': 0.0476, '聴': 0.1200, '肇': 0.0000, '肖': 0.1071, '股': 1.0000, '肥': 0.9357, '育': 0.0329,
	'背': 0.8696, '胡': 0.4100, '胤': 0.1020, '能': 0.6012, '脇': 0.9843, '脩': 0.0000, '腰': 0.9927,
	'膳': 0.9130, '臣': 0.1346, '臥': 0.4783, '臨': 0.2692, '自': 0.2381, '至': 0.0769, '致': 0.0769,
	'臺': 0.9706, '臼': 0.9583, '與': 0.7213, '興': 0.3634, '舎': 0.8661, '舗': 0.9091, '舘': 0.9966,
	'舛': 0.9862, '舜': 0.0278, '舞': 0.0966, '舟': 0.5872, '舩': 1.0000, '航': 0.0278, '船': 0.9704,
	'良': 0.3034, '色': 0.5071, '艶': 0.1220, '艸': 0.6500, '芋': 0.7838, '芙': 0.0234, '芝': 0.8346,
	'芥': 0.5366, '芦': 0.8481, '芭': 0.1667, '花': 0.1949, '芳': 0.2335, '芸': 0.1636, '芹': 0.3723,
	'芽': 0.0453, '苅': 1.0000, '苑': 0.2212, '苔': 0.5000, '苗': 0.3194, '若': 0.7249, '苧': 0.8966,
	'苫': 0.9804, '英': 0.0301, '苺': 0.0408, '茂': 0.4269, '茄': 0.0938, '茅': 0.4651, '茉': 0.0011,
	'茗': 0.7407, '茜': 0.1023, '茨': 0.8667, '茶': 0.5986, '草': 0.5751, '荏': 0.6818, '荒': 0.9344,
	'荘': 0.5112, '荷': 0.9067, '荻': 0.9120, '莉': 0.0000, '莞': 0.1026, '莱': 0.2286, '菅': 0.9487,
	'菊': 0.5447, '菓': 0.3750, '菖': 0.3617, '菜': 0.0173, '菫': 0.0625, '華': 0.0514, '菰': 0.8571,
	'菱': 0.8904, '萌': 0.0053, '萠': 0.1724, '萩': 0.7452, '萬': 0.8080, '萱': 0.9412, '落': 0.9341,
	'葉': 0.2870, '葛': 0.9013, '董': 0.1364, '葦': 0.6981, '葭': 0.8308, '葵': 0.0253, '蒔': 0.5062,
	'蒜': 0.9048, '蒲': 0.9118, '蒼': 0.0697, '蓉': 0.0625, '蓑': 0.8529, '蓬': 0.8182, '蓮': 0.3504,
	'蓼': 0.5200, '蔦': 0.7013, '蔭': 0.7864, '蔵': 0.4332, '蕗': 0.1500, '蕪': 0.8182, '薄': 0.9512,
	'薇': 0.0400, '薔': 0.0204, '薗': 0.9747, '薙': 0.6286, '薩': 0.8293, '薫': 0.0361, '薬': 0.9184,
	'薮': 1.0000, '藁': 1.0000, '藍': 0.2093, '藏': 0.9191, '藤': 0.8851, '藪': 0.9915, '藻': 0.4667,
	'蘆': 0.7222, '蘇': 0.6351, '蘓': 1.0000, '蘭': 0.0878, '虎': 0.3415, '虚': 0.1034, '虫': 0.7105,
	'虹': 0.0188, '蛇': 0.9239, '蛍': 0.0256, '蛭': 0.9455, '蛯': 0.9655, '蜂': 0.8000, '蜜': 0.4444,
	'蝶': 0.2234, '融': 0.0682, '螺': 0.4091, '蟹': 0.8378, '蟻': 0.9405, '衆': 0.1905, '行': 0.3488,
	'街': 0.6923, '衛': 0.1074, '衡': 0.1935, '衣': 0.0430, '表': 0.9577, '衿': 0.0690, '袈': 0.0800,
	'袋': 0.9778, '袖': 0.8980, '袴': 0.9583, '裏': 0.9529, '裕': 0.0187, '補': 0.4783, '裟': 0.0494,
	'裸': 0.1071, '襄': 0.0000, '西': 0.9615, '要': 0.3411, '覇': 0.5690, '見': 0.6445, '規': 0.0471,
	'視': 0.0191, '覚': 0.3476, '覧': 0.5185, '親': 0.2412, '観': 0.1882, '角': 0.9165, '解': 0.6857,
	'言': 0.1346, '計': 0.3490, '訓': 0.0571, '記': 0.1168, '訪': 0.8409, '設': 0.8000, '許': 0.8060,
	'証': 0.1429, '詔': 0.0000, '詞': 0.0769, '詠': 0.0333, '詩': 0.0137, '詮': 0.0303, '詰': 0.9785,
	'話': 0.0000, '誉': 0.0750, '誌': 0.0000, '誓': 0.0597, '語': 0.4688, '誠': 0.0226, '説': 0.1935,
	'調': 0.4082, '諄': 0.0000, '談': 0.5185, '請': 0.9394, '諌': 0.7143, '諏': 0.9464, '諒': 0.0000,
	'論': 0.2381, '諦': 0.0435, '諭': 0.0500, '諸': 0.9251, '謙': 0.0592, '講': 0.6333, '謝': 0.9815,
	'謹': 0.0000, '識': 0.2703, '譜': 0.5714, '譲': 0.1970, '護': 0.5169, '讃': 0.7500, '谷': 0.9771,
	'豆': 0.8500, '豊': 0.4321, '象': 0.1636, '豪': 0.0849, '貝': 0.9509, '貞': 0.3125, '財': 0.9500,
	'貢': 0.0571, '貫': 0.6623, '貴': 0.1421, '賀': 0.7236, '資': 0.0606, '賛': 0.1071, '賢': 0.0477,
	'赤': 0.8860, '赦': 0.0037, '赫': 0.2500, '走': 0.7692, '起': 0.1145, '超': 0.1304, '越': 0.9207,
	'足': 0.8500, '跡': 0.8333, '路': 0.5161, '踏': 0.4762, '身': 0.2946, '躬': 0.0625, '車': 0.8532,
	'軌': 0.0286, '軍': 0.4200, '軒': 0.5462, '軽': 0.8226, '輔': 0.0113, '輝': 0.0444, '輪': 0.6510,
	'輿': 0.9750, '辛': 0.8966, '辰': 0.3650, '農': 0.7651, '辺': 0.9569, '辻': 0.9820, '込': 0.9899,
	'迅': 0.0645, '迎': 0.9787, '近': 0.8085, '返': 0.8571, '迦': 0.7436, '迪': 0.0149, '迫': 0.9923,
	'追': 0.9589, '透': 0.0849, '途': 0.3438, '通': 0.2854, '速': 0.6508, '造': 0.1638, '逢': 0.4444,
	'連': 0.6111, '進': 0.1948, '逸': 0.0881, '遊': 0.2411, '運': 0.2644, '道': 0.5679, '達': 0.3944,
	'遙': 0.0294, '遠': 0.7107, '遥': 0.0299, '遵': 0.0000, '遼': 0.0185, '邉': 1.0000, '邊': 1.0000,
	'邑': 0.7551, '那': 0.1431, '邦': 0.0793, '邨': 0.8065, '郁': 0.0297, '郎': 0.0122, '郡': 0.9276,
	'部': 0.9779, '郭': 0.3824, '郷': 0.6889, '都': 0.2159, '酉': 0.3462, '酒': 0.9409, '酔': 0.3000,
	'醇': 0.0000, '釆': 0.8800, '采': 0.1946, '釈': 0.8627, '釋': 1.0000, '里': 0.1709, '重': 0.4383,
	'野': 0.8409, '量': 0.1414, '金': 0.8096, '釘': 0.9459, '釜': 0.9839, '針': 0.9362, '釣': 0.8481,
	'釼': 0.9167, '鈴': 0.1756, '鉄': 0.4027, '鉢': 0.9259, '鉦': 0.2069, '鉱': 0.1786, '鉾': 0.9070,
	'銀': 0.3514, '銅': 0.9394, '銘': 0.6792, '銭': 0.9296, '鋤': 0.8108, '鋪': 0.9429, '鋭': 0.0000,
	'鋳': 0.6538, '鋼': 0.1333, '錠': 0.2553, '錦': 0.5909, '錫': 0.3636, '錬': 0.0741, '録': 0.4231,
	'鍋': 0.9677, '鍛': 0.9630, '鍜': 1.0000, '鍬': 0.8659, '鍵': 0.8434, '鎌': 0.8917, '鎗': 0.9000,
	'鎮': 0.2019, '鏡': 0.4000, '鐘': 0.4435, '鐵': 0.8529, '鑑': 0.2241, '鑓': 1.0000, '長': 0.7032,
	'門': 0.5506, '開': 0.7525, '閑': 0.6159, '間': 0.9814, '関': 0.9221, '關': 1.0000, '阪': 0.9926,
	'防': 0.9302, '阿': 0.3341, '陀': 0.7917, '附': 0.9810, '降': 0.8723, '院': 0.9720, '陣': 0.7864,
	'除': 1.0000, '陰': 0.8000, '陳': 0.7500, '陵': 0.3256, '陶': 0.3875, '陸': 0.4500, '陽': 0.0719,
	'隅': 0.9408, '隆': 0.0672, '隈': 0.9688, '階': 0.9474, '随': 0.6410, '際': 0.9737, '隠': 0.8182,
	'隣': 0.4138, '隼': 0.1379, '雀': 0.4493, '雁': 0.7143, '雄': 0.0555, '雅': 0.0346, '集': 0.5844,
	'雉': 0.7143, '雍': 0.0000, '雑': 0.9706, '雛': 0.2195, '難': 0.8621, '雨': 0.3583, '雪': 0.1603,
	'雫': 0.2609, '雲': 0.4883, '零': 0.0000, '雷': 0.2468, '霊': 0.5397, '霜': 0.8462, '霞': 0.1073,
	'霧': 0.3370, '露': 0.3163, '青': 0.4051, '靖': 0.0219, '静': 0.1088, '靜': 0.2683, '面': 0.9565,
	'鞆': 0.6098, '鞍': 0.8028, '鞠': 0.1739, '音': 0.0783, '韶': 0.0000, '響': 0.1056, '頂': 0.6190,
	'順': 0.0654, '須': 0.6611, '頌': 0.0484, '頓': 0.9429, '領': 0.8043, '頭': 0.9735, '頴': 0.3478,
	'頼': 0.3169, '額': 0.9143, '顔': 0.5185, '顕': 0.0496, '願': 0.7600, '類': 0.6944, '風': 0.2442,
	'颯': 0.0613, '飛': 0.4940, '食': 1.0000, '飯': 0.9755, '飴': 0.8148, '飼': 0.9512, '飽': 1.0000,
	'餅': 0.9630, '養': 0.5285, '餘': 1.0000, '館': 0.9741, '饒': 0.8485, '饗': 0.9048, '首': 0.9683,
	'香': 0.0644, '馨': 0.0066, '馬': 0.7552, '駄': 0.9412, '駒': 0.7619, '駿': 0.2143, '騎': 0.1143,
	'骨': 0.1379, '高': 0.7596, '鬼': 0.7339, '魁': 0.2917, '魅': 0.0000, '魔': 0.1304, '魚': 0.5000,
	'魯': 0.2667, '鮎': 0.3333, '鮫': 0.9259, '鯉': 0.2970, '鯛': 0.6923, '鯨': 0.8214, '鱒': 0.7941,
	'鳥': 0.7920, '鳩': 0.6176, '鳳': 0.2042, '鳴': 0.5316, '鴇': 0.8966, '鴨': 0.9126, '鴫': 0.9667,
	'鴬': 0.5000, '鴻': 0.5137, '鵜': 0.8012, '鵬': 0.4242, '鶏': 0.4516, '鶴': 0.4600, '鷲': 0.9103,
	'鷹': 0.7265, '鷺': 0.7000, '鹿': 0.8182, '麒': 0.1667, '麗': 0.0317, '麟': 0.0926, '麦': 0.4757,
	'麻': 0.1486, '麿': 0.0602, '黄': 0.4954, '黎': 0.2687, '黒': 0.9533, '黙': 0.0385, '鼎': 0.0741,
	'鼓': 0.1507, '鼻': 0.9789, '齊': 0.9481, '齋': 0.9577, '龍': 0.4541, '龝': 0.9730
}

# Return the supplied full/given/family name with the case fixed

def namecase(name, mode='full', given_names=none):

	# Without a name, do nothing
	if name is none:
		return none

	# Uppercase at start of word (after space, apostrophe, or hyphen)
	name = lc(nametrim(name))
	name = s('\\b(\w)', lambda m: uc(p(m, 1)), name)

	# Lowercase after apostrophes that follow more than 1 letter (e.g. Oso'ese but not O'Brien)
	name = s('(?<=\w{2}|' + apostrophe + '\w)(' + apostrophe + '\w)', lambda m: lc(p(m, 1)), name)
	# Lowercase after apostrophes that follow one letter that isn't O, V or D
	# (e.g. T'ang, but not O'Brien or d'Iapico  or v'Rachel)
	name = s('(?<=\\b[^ODV])(' + apostrophe + '\w)', lambda m: lc(p(m, 1)), name)

	# Uppercase after "Mc" and "Fitz" ("Mac" is done selectively with built-in exceptions)
	name = s('\\b(Mc|Fitz)(\w)', lambda m: p(m, 1) + uc(p(m, 2)), name)

	# Lowercase some grammatical/aristocratic/patronymic prefixes.
	# Note: This should only be done for family names because
	# "Van" is also a Vietnamese given name which is fixed below.

	# Family name prefixes

	if mode != 'given':

		# French/Italian/Spanish/Portuguese: d', dall', dell', de', de, de la,
		#   del, dela, dels, della, delle, dal, dalla, degli,
		#   di, du, da, do, dos, das
		# Spanish/Catalan/Portuguese: y, i, e (conjunctions)
		# German/Dutch: von, zu, von und zu, van, der, ter, den, van de,
		#   van der, van den, van het, tot, 'sSomething, 'tSomething
		# Danish/Swedish/Norwegian: af, av, til
		# Welsh: ap, ab, ferch, verch
		# Arabic/Hebrew/Malaysian: ibn, bin, bint, binti, binte, ben[1], bat,
		#   mibeit, mimishpachat, el-, al-, ut-, ha-, v'
		# Zulu: ka
		# English/Scottish: of
		# Irish: Prefix case normal except: Ó hUiginn, Ó hAodha
		# Note1: "ben" is only detected when unambiguous

		name = s('\\b(d' + apostrophe + '|(?:de(?: la|' + apostrophe + ')?|del|dela|dels|della|delle|dal|dalla|degli|di|du|da|do|dos|das|y|i|e|von und zu|von|zu|van het|van|der|ter|den|tot|af|av|til|ap|ab|ferch|verch|ibn|bin|bint|binti|binte|bat|mibeit|mimishpachat|ka|of)\s)', lambda m: lc(p(m, 1)), name, 'i')
		name = s('\\b(dall|dell)(' + apostrophe + ')(\w)', lambda m: lc(p(m, 1)) + p(m, 2) + uc(p(m, 3)), name, 'i') # Italian: dall'Agnese
		name = s('((?:^|\s)' + apostrophe + ')([st])(\w)', lambda m: p(m, 1) + lc(p(m, 2)) + uc(p(m, 3)), name, 'i') # Dutch: 'sGravesande
		name = s('\\b(' + irish_o_re + ' )(h)(' + irish_vowel_re + ')', lambda m: p(m, 1) + lc(p(m, 2)) + uc(p(m, 3)), name, 'i') # Irish: Ó hUiginn
		name = s('\\b(el|al|ut|ha)(?=' + hyphen + ')', lambda m: lc(p(m, 1)), name, 'i') # Arabic/Hebrew: el- al- ut- ha-
		name = s('\\b(v)(?=' + apostrophe + ')', lambda m: lc(p(m, 1)), name, 'i') # Hebrew: v'Rachel
		if mode == 'family' or name.find(',') != -1:
			name = s('^(ben\s)', lambda m: lc(p(m, 1)), name, 'i') # Hebrew: ben if family
		if m(' v' + apostrophe + '| ha' + hyphen + '(?:Kohein|Levi|Rav)\\b', name) is not none:
			name = s('(?<=\s)\\b(ben)\\b(?=\s)', lambda m: lc(p(m, 1)), name, 'i', count=1) # Hebrew: ben if v' or ha-

		if mode == 'full' and namecase_exceptions_full is not none:
			kcfull = kc(name)
			if kcfull in namecase_exceptions_full:
				name = namecase_exceptions_full[kcfull]

		if mode == 'family' and given_names is not none and fnamecase_exceptions_full is not none:
			kcfull = kc(name + ', ' + given_names)
			if kcfull in fnamecase_exceptions_full:
				name = fnamecase_exceptions_full[kcfull]

	# If this is a full name, the given name is either after a comma
	# or at the start. Fix "van" there.

	if mode == 'full':
		if name.find(',') != -1:
			name = s(', van\\b', ', Van', name)
		else:
			name = s('^van\\b', 'Van', name)

	# With some exceptions (builtin ones and user-supplied ones)

	global need_case_update
	global namecase_exceptions
	global namecase_exceptions_re
	if need_case_update:
		if namecase_exceptions is none:
			namecase_exceptions = { kc(_):_ for _ in namecase_exceptions_builtin }
		namecase_exceptions_re = '|'.join(namecase_exceptions.keys())
		need_case_update = 0

	name = s('\\b(' + namecase_exceptions_re + ')\\b', lambda m: namecase_exceptions[kc(p(m, 1))], name, 'i')

	return name

# Return the supplied given name(s) with the case fixed

def gnamecase(given_names):
	return namecase(given_names, 'given')

# Return the supplied family name with the case fixed

def fnamecase(family_name, given_names=none):
	return namecase(family_name, 'family', given_names)

# Add a case exception (family-wide or individual)

def namecase_exception(name):

	if name is none:
		return 0

	name = nametrim(name)
	if name == '':
		return 0

	has_comma = (name.find(',') != -1)
	kcname = kc(name)

	global namecase_exceptions_full
	global fnamecase_exceptions_full
	global namecase_exceptions
	if has_comma: # Individual exception
		(f, g) = split(', ', name)
		kcnatural = kc(g + ' ' + f)
		if namecase_exceptions_full is none:
			namecase_exceptions_full = {}
		namecase_exceptions_full[kcname] = name
		namecase_exceptions_full[kcnatural] = name
		if fnamecase_exceptions_full is none:
			fnamecase_exceptions_full = {}
		fnamecase_exceptions_full[kcname] = f
	else: # Family-wide exception
		if namecase_exceptions is none:
			namecase_exceptions = { kc(_):_ for _ in namecase_exceptions_builtin }
		namecase_exceptions[kcname] = name

	global need_case_update
	need_case_update = 1
	return 1

# Split exceptions hash. Keys are foldcase full names in
# ambiguous form ("Given Family"). Values are unambiguous.

namesplit_exceptions = none

# Return the supplied full name as "family_name, given_names", guessing if
# necessary, which part of the supplied full name is the family name, and
# which part is the given name or names. It's reasonably good at identifying
# family names containing grammatical constructions (i.e.,
# aristocratic/patronymic) in various languages, but if that doesn't work,
# trickier names that can't be programmatically determined can be added to
# the namesplit_exceptions hash to specify the correct name splitting for
# specific individual names. Many names require this. The letter case of the
# result is also corrected via namecase().

def namesplit(name):

	# Without a name, do nothing

	if name is none:
		return none
	if name == '':
		return ''

	# Prepare the name for matching (any normalization must have already been done)

	name = nametrim(name)
	kcname = kc(name)

	# Lookup exceptions first

	if namesplit_exceptions is not none and kcname in namesplit_exceptions:
		name = namesplit_exceptions[kcname]

	# Accept existing commas

	if name.find(',') != -1:
		return namecase(name)

	# Load hash of family name starter words

	global split_starter
	if split_starter is none:
		split_starter = { kc(_): 1 for _ in split_starter_list }
	global split_starter_re
	if split_starter_re is none:
		split_starter_re = '(?:' + '|'.join(split_starter.keys()) + ')'

	# Load family name hashes/regexes for Chinese, Korean, Vietnamese

	global family_names_ck
	global family_names_ck_re
	if family_names_ck is none:
		family_names_ck = { _: 1 for(_) in family_names_chinese + [ _ for _ in family_names_korean if m('\p{Hangul}', _) is not none ] }
		family_names_ck_re = '(?:' + '|'.join(family_names_ck.keys()) + ')'

	global family_names_ck_roman
	global family_names_ck_roman_re
	if family_names_ck_roman is none:
		family_names_ck_roman = { s("'", apostrophe, kc(_)): 1 for _ in family_names_chinese_roman + family_names_korean_roman if m('^' + split_starter_re + '$', _, 'i') is none }
		family_names_ck_roman_re = '(?:' + '|'.join(family_names_ck_roman.keys()) + ')'

	global family_names_v_roman
	global family_names_v_roman_re
	if family_names_v_roman is none:
		family_names_v_roman = { kc(_): 1 for _ in family_names_vietnamese }
		family_names_v_roman_re = '(?:' + '|'.join(family_names_v_roman.keys()) + ')'

	# Identify Vietnamese names (before Dutch names)

	match = m('^(' + family_names_v_roman_re + ') (.+)$', name, 'i')
	if match is not none:
		(f, g) = p(match)
		return namecase(f + ', ' + g)

	match = m('^(.+) (' + family_names_v_roman_re + ')$', name, 'i')
	if match is not none:
		(g, f) = p(match)
		return namecase(f + ', ' + g)

	# Identify plausible multi-word family names (in Latin scripts)

	words = split(' ', name)
	if len(words) < 2 and m('^[\p{Han}\p{Hangul}\p{Hiragana}\p{Katakana}]+$', name) is none:
		return namecase(name)

	for i in range(1, len(words)):
		kcstarter = kc(words[i])
		if kcstarter not in split_starter:
			continue
		if kcstarter == 'ben' and m(' v' + apostrophe + '| ha' + hyphen + '(?:Kohein|Levi|Rav)\\b', name, 'i') is none: # Hebrew
			continue
		if kcstarter == 'bean' and m('\\bbean ' + irish_post_bean_re + '\\b', name, 'i') is none: # Irish
			continue
		if i == len(words) - 1:
			continue

		if i > 1 and m('^[yie]$', kcstarter, 'i') is not none: # Spanish/Catalan/Portuguese
			i -= 1
		return namecase(' '.join(words[i:]) + ', ' + ' '.join(words[0:i]))

	# Identify Chinese, Korean, and Vietnamese family names (and some misidentified Japanese names) :-(
	# Note: When romanized, these family names can appear first or last

	match = m('^('  + family_names_ck_re + ')(.+)$', name)
	if match is not none:
		(f, g) = p(match)
		return f + ', ' + g

	# Note: Family names can appear first or last. Luckily, for Chinese,
	# the two given name characters are usually romanized as a single word,
	# so there's less chance of misinterpreting a given name as a family
	# name. Unfortunately, Korean names are romanized as separate names,
	# all of which might look like a family name, so it's likely that the
	# name that appears first will be recognized as a family name, even
	# if the real family name is at the end (in English-speaking places).
	# This can only be fixed with split exceptions (or by encouraging
	# Koreans to not put their family name last).

	match = m('^(' + family_names_ck_roman_re + ') (.+)$', name, 'i')
	if match is not none:
		(f, g) = p(match)
		return namecase(f + ', ' + g)

	match = m('^(.+) (' + family_names_ck_roman_re + ')$', name, 'i')
	if match is not none:
		(g, f) = p(match)
		return namecase(f + ', ' + g)

	# Identify Japanese names

	if m('^[\p{Han}\p{Hiragana}\p{Katakana}]+$', name) is not none:
		return ', '.join(namesplit_ja(name))

	# Assume a single-word family name
	# Note: Non-hyphenated multi-name family names must be handled via split exceptions

	return namecase(words[-1] + ', ' + ' '.join(words[0:len(words) - 1]))

# Adapted from Lingua::JA::Name::Splitter by Ben Bullock <bkb@cpan.org>
# https://github.com/benkasminbullock/Lingua-JA-Name-Splitter
# http://www.sljfaq.org/afaq/names-for-people.html
# http://www.edrdg.org/enamdict/enamdict_doc.html

# The weight to give the position in the kanji if it is a known kanji
length_weight = 0.735 # 42030 successes
# The probability cutoff for splitting the name
split_cutoff = 0.5

def namesplit_ja(name):

	length = len(name)

	# Only one character, so there is nothing to split
	if length == 1:
		return [name]

	# Only two characters, so there is only one possibility
	if length == 2:
		return [name[0], name[1]]

	# Probability that each character is part of the family name.
	# First character is definitely part of the family name.
	# Last character is definitely part of the given name.
	prob = [ 1 - i / (length - 1) for i in range(length) ]

	# Loop from the second kanji to the second-from-last kanji
	for i in range(1, length - 1):

		# Improve on the default probability if possible
		if m('^[\p{Hiragana}\p{Katakana}]$', name[i]) is not none:
			prob[i] = 0 # Assume that kana is not part of the surname (not correct in practice)
		elif name[i] in family_name_japanese_probabilities:
			prob[i] = length_weight * prob[i] + (1 - length_weight) * family_name_japanese_probabilities[name[i]]
		elif name[i] == '々':
			prob[i] = prob[i - 1] # This repeated kanji has the same probability as the original kanji

		# Have we reached the given name?
		if prob[i] < split_cutoff:
			return [name[0:i], name[i:]]

	return [name[0:-1], name[-1]]

# Add a split exception

def namesplit_exception(name):

	if name is none:
		return 0

	name = nametrim(name)
	if name == '':
		return 0

	has_comma = (name.find(',') != -1)
	if not has_comma:
		return 0

	(f, g) = split(', ?', name)

	global namesplit_exceptions
	if namesplit_exceptions is none:
		namesplit_exceptions = {}
	if m('^[\p{Han}\p{Hangul}\p{Hiragana}\p{Katakana}]+$', f + g) is not none:
		natural = f + g
		namesplit_exceptions[name] = name
		namesplit_exceptions[natural] = name
	else:
		kcname = kc(name)
		kcnatural = kc(g + ' ' + f)
		namesplit_exceptions[kcname] = name
		namesplit_exceptions[kcnatural] = name

	return 1

# Like namesplit() but returns the name as a list containing
# two items: the family name followed by the given names.

def nameparts(name):

	if name is none or name == "":
		return []

	return split(', ?', namesplit(name), maxsplit=1)

# Format a full name in Eastern or Western name order as appropriate

def namejoin(f, g):

	if g is none:
		return f
	if f is none:
		return g

	if m('^[\p{Han}\p{Hangul}\p{Hiragana}\p{Katakana}]+$', f + g) is not none:
		return f + g

	return ' '.join([g, f])

# Trim the supplied name

def nametrim(name):

	if name is none:
		return none

	name = s('^\s+', '', name)                               # Remove leading spaces
	name = s('\s+$', '', name)                               # Remove trailing spaces
	name = s('\s+', ' ', name)                               # Squash multiple spaces
	name = s('(' + hyphen + ') ', lambda m: p(m, 1), name)   # Remove space after hyphen
	name = s(' (,|' + hyphen + ')', lambda m: p(m, 1), name) # Remove space before comma and hyphen
	name = s(',(?! )', ', ', name)                           # Add space after - if missing

	return name

# Normalise internal hash keys and data with the supplied normalization function

def normalize(func):

	global apostrophe 
	apostrophe = func(apostrophe)

	global hyphen 
	hyphen = func(hyphen)

	global namecase_exceptions 
	if namecase_exceptions is not none:
		namecase_exceptions = { func(_): func(namecase_exceptions[_]) for _ in namecase_exceptions.keys() }

	global namecase_exceptions_full 
	if namecase_exceptions_full is not none:
		namecase_exceptions_full = { func(_): func(namecase_exceptions_full[_]) for _ in namecase_exceptions_full.keys() }

	global fnamecase_exceptions_full 
	if fnamecase_exceptions_full is not none:
		fnamecase_exceptions_full = { func(_): func(fnamecase_exceptions_full[_]) for _ in fnamecase_exceptions_full.keys() }

	global namecase_exceptions_re
	if namecase_exceptions_re is not none:
		namecase_exceptions_re = func(namecase_exceptions_re)

	global namesplit_exceptions 
	if namesplit_exceptions is not none:
		namesplit_exceptions = { func(_): func(namesplit_exceptions[_]) for _ in namesplit_exceptions.keys() }

	global split_starter_list
	split_starter_list = [ func(_) for _ in split_starter_list ]

	global split_starter 
	if split_starter is not none:
		split_starter = { func(_): 1 for _ in split_starter.keys() }

	global split_starter_re
	if split_starter_re is not none:
		split_starter_re = '(?:' + '|'.join(split_starter.keys()) + ')'

	global irish_o 
	irish_o = [ func(_) for _ in irish_o ]

	global irish_o_re 
	irish_o_re = '(?:' + '|'.join(irish_o) + ')'

	global irish_vowel 
	irish_vowel = [ func(_) for _ in irish_vowel ]

	global irish_vowel_re 
	irish_vowel_re = '(?:' + '|'.join(irish_vowel) + ')'

	global irish_post_bean 
	irish_post_bean = [ func(_) for _ in irish_post_bean ]

	global irish_post_bean_re 
	irish_post_bean_re = '(?:' + '|'.join(irish_post_bean) + ')'

	global family_names_ck 
	if family_names_ck is not none:
		family_names_ck = { func(_): 1 for _ in family_names_ck.keys() }

	global family_names_ck_re 
	if family_names_ck_re is not none:
		family_names_ck_re = '(?:' + '|'.join(family_names_ck.keys()) + ')'

	global family_names_ck_roman 
	if family_names_ck_roman is not none:
		family_names_ck_roman = { func(_): 1 for _ in family_names_ck_roman.keys() }

	global family_names_ck_roman_re 
	if family_names_ck_roman_re is not none:
		family_names_ck_roman_re = '(?:' + '|'.join(family_names_ck_roman.keys()) + ')'

	global family_names_v_roman 
	if family_names_v_roman is not none:
		family_names_v_roman = { func(_): 1 for _ in family_names_v_roman.keys() }

	global family_names_v_roman_re 
	if family_names_v_roman_re is not none:
		family_names_v_roman_re = '(?:' + '|'.join(family_names_v_roman.keys()) + ')'

	global family_names_chinese 
	family_names_chinese = [ func(_) for _ in family_names_chinese ]

	global family_names_chinese_roman 
	family_names_chinese_roman = [ func(_) for _ in family_names_chinese_roman ]

	global family_names_korean 
	family_names_korean = [ func(_) for _ in family_names_korean ]

	global family_names_korean_roman 
	family_names_korean_roman = [ func(_) for _ in family_names_korean_roman ]

	global family_names_vietnamese 
	family_names_vietnamese = [ func(_) for _ in family_names_vietnamese ]

# Reset internal data for test coverage purposes

def nameutils_reset_data():

	global namecase_exceptions 
	namecase_exceptions = none # This is the only one that matters (initialized in two places)
	global namecase_exceptions_full 
	namecase_exceptions_full = none
	global fnamecase_exceptions_full 
	fnamecase_exceptions_full = none
	global need_case_update 
	need_case_update = 1
	global namecase_exceptions_re 
	namecase_exceptions_re = none
	global split_starter 
	split_starter = none
	global split_starter_re 
	split_starter_re = none
	global family_names_ck 
	family_names_ck = none
	global family_names_ck_re 
	family_names_ck_re = none
	global family_names_ck_roman 
	family_names_ck_roman = none
	global family_names_ck_roman_re 
	family_names_ck_roman_re = none
	global family_names_v_roman 
	family_names_v_roman = none
	global family_names_v_roman_re 
	family_names_v_roman_re = none

import regex as re

#_re_cache = {}
#_re_cacheing = 0
#def re_cacheing(yesno):
#	# Turn regexp caching on or off for r(), m(), s() and split().
#	global _re_cacheing
#	global _re_cache
#	_re_cacheing = yesno
#	if not yesno:
#		_re_cache = {}

def r(pattern, opts=''):
	# r(pattern, opts='') -> compiled regular expression object
	#
	# Like re.compile() but with more compact options. opts is a string containing
	# any of the characters 'ilmsxu' each of which corresponds to re.I, re.L etc.
	# If the pattern is a unicode object, the option re.U is automatically included.
	#
	# usage:
	# pattern = r('([a-e])\d', 'i')

#	# Not a string? Must already be compiled
#	if not isinstance(pattern, str):
#		return pattern
#	# Check cache
#	if _re_cacheing:
#		key = pattern + '\0\0\0' + opts
#		if key in _re_cache:
#			return _re_cache[key]
	flags, odict = 0, { 'i': re.I, 'l': re.L, 'm': re.M, 's': re.S, 'x': re.X, 'u': re.U }
	for o in opts:
		flags |= odict[o]
	flags |= re.U
	recomp = re.compile(pattern, flags)
#	if _re_cacheing:
#		_re_cache[key] = recomp
	return recomp

def m(pattern, text, opts='', pos=0, endpos=none):
	# m(pattern, text, opts='', pos=0, endpos=None) -> re.MatchObject
	#
	# Like re.search() but with more compact options. See r().
	#
	# usage:
	# match = m(pattern, text)

#	if endpos is none:
	endpos = len(text)
	return r(pattern, opts).search(text, pos, endpos)

def s(pattern, rep, text, opts='', count=0):
	# s(pattern, rep, text, opts='', count=0) -> str
	#
	# Alias for re.sub().
	#
	# usage:
	# text = s('\s+', ' ', text)

	return r(pattern, opts).sub(rep, text, count)

def p(match, index=none):
	# p(match, index=None) -> a string or a list of strings
	#
	# When index is supplied, it's the same as match.group(index).
	# Otherwise, it's the same as match.groups().
	#
	# usage:
	# match = m('a(b)c', 'abc')
	# print(len(p(match)), p(match, 0))

#	if match is none:
#		return [] if index is none else none
	return match.group(index) if index is not none else match.groups()

#def pm(pattern, text, opts='', pos=0, endpos=None, index=none):
#	# Combination of m() and p() for use in lambda functions.
#	# Returns None when m() fails to find a match.
#	#
#	# usage: parts = pm('a(b)(c)', 'abc')          # parts == ('b', 'c')
#	# usage: parts = pm('a(b)(c)', 'abc', index=1) # parts == 'b'
#	# usage: parts = pm('a(b)(c)', 'abc', index=2) # parts == 'c'
#
#	match = m(pattern, text, opts, pos, endpos)
#	return p(match, index) if match is not none else [] if index is none else none

#regex, like, subst, part, likepart = r, m, s, p, pm

def split(pattern, text, opts='', maxsplit=0):
	# split(pattern, text, opts='', maxsplit=0) -> list
	#
	# Alias for re.split().
	#
	# usage:
	# parts = split(pattern, text)

	return r(pattern, opts).split(text, maxsplit)

def uc(s):
	# Return the uppercase version of the given string. If it is None, return None.
	return s.upper() if s is not none else s

#def ucfirst(s):
#	# Return the the given string with the first character in uppercase. If it is None, return None.
#	return s[:1].upper() + s[1:] if s is not none else s

def lc(s):
	# Return the lowercase version of the given string. If it is None, return None.
	return s.lower() if s is not none else s

#def lcfirst(s):
#	# Return the the given string with the first character in lowercase. If it is None, return None.
#	return s[:1].lower() + s[1:] if s is not none else s

# vim:set ts=4 sw=4 fenc=utf8:
