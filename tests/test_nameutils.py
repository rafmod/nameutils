#!/usr/bin/env python3

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

import sys
sys.path.insert(0, 'src')

# Lower-case versions of built-in constants

true = True
false = False
none = None

# Test nameutils

from nameutils import *

# Test cases are either:
#
# - "strings" containing an unambiguous full name:
#   tested as supplied, and as ambiguous, and both uppercased,
#   and both lowercased, with namecase, gnamecase, fnamecase,
#   namesplit, and nameparts.
#
# - [arrayref] containing two items: an unambiguous full name,
#   followed by the expected incorrect namesplit result.
#   The same tests as above for "strings" are performed.
#   These demonstrate known limitations.
#
# - {hashref} containing a "name" string, a "case" string showing
#   the expected possibly incorrect namecase result, and a "split"
#   string showing the expected possibly incorrect namesplit result.
#   These demonstrate known limitations.
#
# - "strings" containing a single (given or family) name:
#   tested as supplied, and as uppercased, and as lowercased, with
#   namecase, gnamecase, fnamecase, namesplit, and nameparts.

test_cases = \
[
	none,
	"",

	"Smith, John Peter",
	"of Lethington, William Maitland", # Split wrong by default (would need an exception)

	"McAdam, Shaun",
	"MacDonald, Fergus",
	"Macquarie, Lachlan",
	"FitzPatrick, James",
	"O'Brian, Patrick",
	"St Clair, Kelly",
	"St. Clair, Kelly",
	"Ste Clair, Kelly",
	"Ste. Clair, Kelly",

	"Le Page, David",
	"La Tour, Pierre",
	"Li Donni, Rochelle",
	"Lo Giudice, Giovanni",
	"d'Iapico-Bien, Estella",
	"dall'Agnese, Bruno",
	"dell'Agnese, Bruno",
	"de’ Medici, Lorenzo",
	"de' Medici, Lorenzo",
	"de Groot, John",
	"de la Pierre, Pierre",
	"del Mar, Maria",
	"dela Mar, Maria",
	"dels Àngels, Maria",
	"della Vella, Giaccomo",
	"delle Velle, Giovanni",
	"dal Santos, Maria",
	"dalla Vella, Marco",
	"degli Castelli, Lorenza",
	"di Francesco, Maria",
	"di Lampedusa, Tomasi Giuseppe",
	"du Page, Pierre",
	"da Silva, Jorge",
	"do Santo, Filipe",
	"dos Santos, Abilio",
	"das Costas, Adriana",
	"San Jose, Oscar",
	"Santa Gutierrez, Catalina",
	"Santos Bernal, Monica",

	"Ruiz y Picasso, Pablo Diego",
	"Puigdemont i Casamajó, Carles",
	"da Silva dos Santos da Costa de Sousa, João Duarte",
	"da Silva Santos Costa e Sousa, João Duarte",

	"von Pappenhim, Hans",
	"von der Trave, Thomas",
	"zu Pappenhim, Hans",
	"von und zu Pappenhim, Hans",

	"van Haag, Bram",
	"der Haag, Jeroen",
	"ter Horst, Johanne",
	"den Haag, Sanne",
	"van de Horst, Laura",
	"van der Haag, Eva",
	"van den Haag, Willem",
	"van het Horst, Mees",
	"van Voorst tot Voorst, Henrik",
	"'sGravesande, Willem",
	"van 'sHertogenbosch, Gemeente",
	"van 'tHoen, Gemeente",

	"av Morgenstierne, Sigurd",
	"von Munthe af Morgenstierne, Maja",
	["Jonsson til Sudreim, Lars", "til Sudreim, Lars Jonsson"], # Split wrong without exception

	"DaSilva, James",
	"DuBois, Jack",
	"LaForge, Daniel",
	"LeFevre, Sally",
	"VanZandt, Kristine",

	"O Donoghue, Patrick",
	"Ó Dónaill, Niall",
	"Ni Fhoghlua, Saoirse",
	"Ní Fhoghlua, Saoirse",
	"Mac Donnchada, Michael",
	"Nic Fhoghlua, Saoirse",
	"Ua Donoghue, Michael",
	"Ua Duinnín, Pádraig",
	"Bean Ui Fhoghlua, Aisling",
	"Bean Uí Fhoghlua, Aisling",
	"Bean Mhic Fhoghlua, Saoirse",
	"Fhoghlua, Saoirse Bean Other", # Incorrect name correctly not identified
	"Ui Fhoghlua, Saoirse",
	"Uí Fhoghlua, Saoirse",
	"Mhic Fhoghlua, Saoirse",

	"Ó hAodha, Micheál",
	"Ó hEiggín, Micheál",
	"Ó hIiggín, Micheál",
	"Ó hOiggín, Micheál",
	"Ó hUiggín, Micheál",
	"O hAodha, Micheál",
	"O hEiggín, Micheál",
	"O hIiggín, Micheál",
	"O hOiggín, Micheál",
	"O hUiggín, Micheál",
	"Ó hÁodha, Micheál",
	"Ó hÉiggín, Micheál",
	"Ó hÍiggín, Micheál",
	"Ó hÓiggín, Micheál",
	"Ó hÚiggín, Micheál",
	"O hÁodha, Micheál",
	"O hÉiggín, Micheál",
	"O hÍiggín, Micheál",
	"O hÓiggín, Micheál",
	"O hÚiggín, Micheál",
	"Ó Hnotreal, Micheál",
	"O Hnotreal, Micheál",

	"ap Dafydd, Rhys",
	"ab Owain, Maredudd",
	"ferch Maredudd, Myfanwy",
	"verch Maredudd, Myfanwy",

	"El Ali, Camilla",
	"Al Musawi, Mariam",
	"el-Bayeh, Bazif",
	"al-Nassar, Nariman",
	"ut-Tahrir, Haqq",
	"ibn Hab, Aziz",
	"bin Hab, Charbel",
	"bint Aziz, Angela",
	"binti Othman, Fatima",
	"binte Othman, Nadia",

	# Right when technically unambiguous
	{ 'name': "ben Joseph, David", 'case': "ben Joseph, David", 'split': "ben Joseph, David" },
	{ 'name': "Peters, John Ben", 'case': "Peters, John Ben", 'split': "Peters, John Ben" },
	# Right sometimes when technically ambiguous
	{ 'name': "John Ben Peters", 'case': "John Ben Peters", 'split': "Peters, John Ben" },
	"Peters, John Ben",
	# Wrong sometimes when technically ambiguous
	{ 'name': "David ben Joseph", 'case': "David Ben Joseph", 'split': "Joseph, David Ben" },
	# Right when practically unambiguous (presence of v' and/or ha-)
	{ 'name': "David ben Joseph v'Rachel", 'case': "David ben Joseph v'Rachel", 'split': "ben Joseph v'Rachel, David" },
	{ 'name': "David ben Joseph v' Rachel", 'case': "David ben Joseph v' Rachel", 'split': "ben Joseph v' Rachel, David" },
	{ 'name': "David ben Joseph ha-Kohein", 'case': "David ben Joseph ha-Kohein", 'split': "ben Joseph ha-Kohein, David" },
	{ 'name': "David ben Joseph ha-Levi", 'case': "David ben Joseph ha-Levi", 'split': "ben Joseph ha-Levi, David" },
	{ 'name': "David ben Joseph ha-Rav", 'case': "David ben Joseph ha-Rav", 'split': "ben Joseph ha-Rav, David" },
	{ 'name': "David ben Joseph v'Rachel ha-Rav", 'case': "David ben Joseph v'Rachel ha-Rav", 'split': "ben Joseph v'Rachel ha-Rav, David" },

	"ben Joseph v'Rachel, David",
	"bat Moshe, Leah",
	"bat Moshe v'Rachel ha-Rav, Leah",
	"bat Mordecai v' Tzipporah, Devorah Rut",
	"mibeit Moshe v'Rachel ha-Levi, Leah",
	"mimishpachat Moshe v'Rachel ha-Kohein, Leah",

	"Te Whare, Natalie",

	"ka Nolwazi, Ayize",

	"Oso'ese",
	"Ya'akov",
	"Y'honatan",
	"Sh'mu'el",
	"Onosaʻi",
	"Tausa’afia",
	"Ka’ana’ana",
	"S’thembiso",

	"Tran, Van Man",
	"Morrison, Van",
	"Der, Joseph",

	'Pushkin, Alexander Sergeevich',
	'Пушкин, Александр Сергеевич',

	'Dostoevsky, Fyodor Mikhailovich',
	'Достоевский, Федор Михайлович',

	'Akhmatova, Anna Andreevna',
	'Ахматова, Анна Андреевна',

	'Tolstoy, Lev Nikolayevich',
	'Толстой, Лев Николаевич',

	'Dostoevsky, Fyodor Mikhailovich',
	'Достоевский, Фёдор Михайлович',

	'Akhmatova, Anna',
	'Gorenko, Anna Andreyevna',
	'Горенко, Анна Андреевна',

	'Pavlova, Anna Pavlovna',
	'Pavlova, Anna Matveyevna',
	'Павлова, Анна Павловна'
]

# Test cases for nametrim() are two-element arrayrefs containing the input
# string and the expected result string.

nametrim_cases = \
[
	[none, none],
	["", ""],
	["JohnSmith", "JohnSmith"],
	["John Smith", "John Smith"],
	["Smith, John", "Smith, John"],
	["    John       Smith    ", "John Smith"],
	["    Smith   ,  John     ", "Smith, John"],
	["    Smith   ,John     ", "Smith, John"],
	[" 		   Smith 	  , 	 John  	   ", "Smith, John"],
	["  Peter Smith - Jones  ", "Peter Smith-Jones"],
	[" Smith - Jones ,Peter ", "Smith-Jones, Peter"]
]

# Test cases for namecase_exception() are strings containing
# the exception. It can either be a family name, or an
# unambiguous full name: "Family_name, Given_names".

case_exception_cases = \
[
	"d'Family, Given",
	"D'Family, Given",
	"D'family, Given",
	"d'family, Given",
	"d'FaMiLy, GiVeN",
	"Macdonald",
	"MacdonalD",
	"MacOther, Bruce",
	"mArrier D'uNiEnViLlE, aLiX",
	"MacDhòmhnaill",
	"NicDhonnchaidh"
]

# Test cases for namesplit_exceptions() are strings containing
# the exception. It must be a full name in unambiguous form:
# "Family_name, Given Names".

split_exception_cases = \
[
	"Abdul Aziz, Jenny",
	"Ah Fat, Peter",
	"Ali Khan, Liban",
	"Assis de Queiroz, Vinicius",
	"Castano Mendoza, Luiza",
	"de Gois, Maria de Sousa",
	"Gautam Adhikari, Devi",
	"Marrier d’Unienville, Pierre", # Non-ASCII apostrophe
	"Nom de Nom–Nom, Prénom" # Non-ASCII dash
]

# Test preservation/non-preservation of non-ASCII apostrophe-like and
# hyphen-like characters (case and split). Each case is an arrayref. The
# first item is the case and split exception. The remaining items are cases
# that must match the exception.

nonascii_punctuation_cases = \
[
	[
		"fAm d'Fam-Fam, Giv", # ascii hyphen-dash
		"fAm d’Fam-Fam, Giv", # U+2019 Right Single Quotation Mark
		"fAm dʼFam-Fam, Giv", # U+02BC Modifier Letter Apostrophe Unicode Character
		"fAm dʻFam-Fam, Giv", # U+02BB Modifier Letter Turned Comma
		"fAm d'Fam־Fam, Giv", # U+05BE Hebrew Punctuation Maqaf
		"fAm d’Fam‐Fam, Giv", # U+2010 Hyphen
		"fAm dʼFam‑Fam, Giv", # U+2021 Non-Breaking Hyphen
		"fAm dʻFam–Fam, Giv", # U+2013 En Dash
		"fAm dʻFam—Fam, Giv"  # U+2014 Em Dash
	],
	[
		"Ka’ana’ana, Giv", # Multiple
		"Ka'ana'ana, Giv",
		"Kaʼanaʼana, Giv",
		"Kaʻanaʻana, Giv"
	],
	[
		"Fim Onosa'i, Giv", # ASCII first
		"Fim Onosaʻi, Giv",
		"Fim Onosa’i, Giv",
		"Fim Onosaʼi, Giv"
	],
	[
		"Fam Onosaʻi, Giv", # ASCII not first
		"Fam Onosa’i, Giv",
		"Fam Onosaʼi, Giv",
		"Fam Onosa'i, Giv"
	]
]

# Test cases for normalize(). Each case is a full name in
# unambiguous format, used as a case exception and as a split
# exception.

normalization_cases = \
[
	"Surplus fÁmMïLy, GíBbèn",
	"Extra De’ MaDiCï, MaRcÓ" # Test %split_starter as well
]

# Chinese test cases for namesplit
# Romanized family names can appear first or last

chinese_split_cases = \
[
	['习近平', '习, 近平'],
	['胡锦涛', '胡, 锦涛'],
	['江泽民', '江, 泽民'],

	['Xi Jinping', 'Xi, Jinping'],
	['Hu Jintao', 'Hu, Jintao'],
	['Jiang Zemin', 'Jiang, Zemin'],

	['Jinping Xi', 'Xi, Jinping'],
	['Jintao Hu', 'Hu, Jintao'],
	['Zemin Jiang', 'Jiang, Zemin'],

	["T'ang Jinping", "T'ang, Jinping"],
	["Jinping T'ang", "T'ang, Jinping"],
	["T’ang Jinping", "T’ang, Jinping"],
	["Jinping T’ang", "T’ang, Jinping"],
	["Tʼang Jinping", "Tʼang, Jinping"],
	["Jinping Tʼang", "Tʼang, Jinping"],
	["Tʻang Jinping", "Tʻang, Jinping"],
	["Jinping Tʻang", "Tʻang, Jinping"]
]

# Korean test cases for namesplit
# Romanized family names can appear first or last

korean_split_cases = \
[
	['이영호', '이, 영호'],
	['임요환', '임, 요환'],
	['김택용', '김, 택용'],

	['李泳浩', '李, 泳浩'],
	['林遙煥', '林, 遙煥'],
	['金澤容', '金, 澤容'],

	['Lee Young Ho', 'Lee, Young Ho'],
	['Lim Yo Hwan', 'Lim, Yo Hwan'],
	['Kim Taek Yong', 'Kim, Taek Yong'],

	# Note: Two of these family-name-last tests fail because the
	# middle names look like (Chinese and Korean) family names as well.
	# This can be fixed with split exceptions
	# ['Young Ho Lee', 'Lee, Young Ho'],
	# ['Yo Hwan Lim', 'Lim, Yo Hwan'],
	['Taek Yong Kim', 'Kim, Taek Yong']
]

# Exceptions that correct the two commented out tests above

korean_split_exception_cases = \
[
	'Lee, Young Ho',
	'Lim, Yo Hwan'
]

# Vietnamese test cases for namesplit
# Family names can appear first or last

vietnamese_split_cases = \
[
	'Nguyễn, Kim',
	'Nguyen, Kim',
	'Phan, Văn Trường',
	'Phan, Van Truong',
	'Nguyễn, Thị Minh Khai',
	'Nguyen, Thi Minh Khai',
	'Nguyễn, Van Nam',
	'Nguyễn, Vân Anh',
	'Lê, Thi Lam',
	'Le, Thi Lam',
	'Nguyễn, Trãi',
	'Nguyen, Trai',
	'Nguyễn, Thi Hoa Diep'
]

# Japanese test cases for namesplit
# This is outsourced to Lingua::JA::Name::Splitter

japanese_split_cases = \
[
	['佐藤明実', '佐藤, 明実'],
	['佐藤あけみ', '佐藤, あけみ'],
	['佐藤アケミ', '佐藤, アケミ'],

	['佐藤博子', '佐藤, 博子'],

	['鈴木大全', '鈴木, 大全'],

	['林圭司', '林, 圭司'],
	['林けいじ', '林, けいじ'],
	['林ケイジ', '林, ケイジ'],

	['森一樹', '森, 一樹'],

	['橋本梢', '橋本, 梢'],
	['橋本こず恵', '橋本, こず恵'],
	['橋本こずえ', '橋本, こずえ'],

	['長谷川光月', '長谷川, 光月'],
	['長谷川みつき', '長谷川, みつき'],
	['長谷川ミツキ', '長谷川, ミツキ'],

	['佐佐木順平', '佐佐木, 順平'],
	['佐々木順平', '佐々木, 順平'],

	['原彩子', '原, 彩子'],

	['小山美紀夫', '小山, 美紀夫'],
	['小山みきお', '小山, みきお'],
	['小山ミキオ', '小山, ミキオ'],

	['佐', '佐'], # 1 kanji
	['佐じ', '佐, じ'], # 2 kanji

	['佐张ケイ', '佐张, ケイ'] # 1 unknown kanji
]

# CJK namesplit exceptions
# Note: These names are forced to be incorrect

cjk_split_exception_cases = \
[
	'习近, 平',
	'胡锦, 涛',
	'江泽, 民',

	'이영, 호',
	'임요, 환',
	'김택, 용',

	'高橋, 永子',
]

# Test cases for namejoin() are three-element arrayrefs containing the input
# family name and given names, and the expected resulting full name.

namejoin_cases = \
[
	[none, none, none],
	[none, 'Giv', 'Giv'],
	['Fam', none, 'Fam'],

	['Smith', 'Peter', 'Peter Smith'],
	['van Haag', 'Bram', 'Bram van Haag'],

	['胡', '锦涛', '胡锦涛'],
	['Hu', 'Jintao', 'Jintao Hu'],

	['임', '요환', '임요환'],
	['林', '遙煥', '林遙煥'],
	['Lim', 'Yo Hwan', 'Yo Hwan Lim'],

	['林', '圭司', '林圭司'],
	['林', 'けいじ', '林けいじ'],
	['林', 'ケイジ', '林ケイジ'],

	['Nguyễn', 'Thị Minh Khai', 'Thị Minh Khai Nguyễn'],
	['Nguyen', 'Thi Minh Khai', 'Thi Minh Khai Nguyen']
]

# Test cases after resetting internal data. Each case is an arrayref
# containing the case exception, and a follow-up namecase test. If the
# follow-up namecase test succeeds, that means that the built-in namecase
# exceptions were successfully initialised by namecase_exception() after
# the internal data was reset. This tests that the built-in namecase
# exceptions are initialised when namecase_exception() is called before
# namecase() is called (which also initializes the built-in namecase
# exceptions). All previous namecase tests rely on namecase() initializing
# the built-in namecase exceptions the first time it is called. This tests
# the other location where built-in namecase exceptions are initialized.

post_reset_case_exception_cases = \
[
	["Macdonald", "MacAlister"]
]

# Disable test suites temporarily

#test_cases = []
#nametrim_cases = []
#case_exception_cases = []
#split_exception_cases = []
#nonascii_punctuation_cases = []
#normalization_cases = []
#chinese_split_cases = []
#korean_split_cases = []
#korean_split_exception_cases = []
#vietnamese_split_cases = []
#japanese_split_cases = []
#cjk_split_exception_cases = []
#namejoin_cases = []
#post_reset_case_exception_cases = []

# Define some helper functions

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
#	for o in opts:
#		flags |= odict[o]
	flags |= re.U
	recomp = re.compile(pattern, flags)
#	if _re_cacheing:
#		_re_cache[key] = recomp
	return recomp

#def m(pattern, text, opts='', pos=0, endpos=none):
#	# m(pattern, text, opts='', pos=0, endpos=None) -> re.MatchObject
#	#
#	# Like re.search() but with more compact options. See r().
#	#
#	# usage:
#	# match = m(pattern, text)
#
#	if endpos is none:
#		endpos = len(text)
#	return r(pattern, opts).search(text, pos, endpos)
#
#def s(pattern, rep, text, opts='', count=0):
#	# s(pattern, rep, text, opts='', count=0) -> str
#	#
#	# Alias for re.sub().
#	#
#	# usage:
#	# text = s('\s+', ' ', text)
#
#	return r(pattern, opts).sub(rep, text, count)
#
#def p(match, index=none):
#	# p(match, index=None) -> a string or a list of strings
#	#
#	# When index is supplied, it's the same as match.group(index).
#	# Otherwise, it's the same as match.groups().
#	#
#	# usage:
#	# match = m('a(b)c', 'abc')
#	# print(len(p(match)), p(match, 0))
#
#	if match is none:
#		return [] if index is none else none
#	return match.group(index) if index is not none else match.groups()
#
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
#
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

def lc(s):
	# Return the lowercase version of the given string. If it is None, return None.
	return s.lower() if s is not none else s

# Run normalize first, before namecase_exceptions_re is defined.
# Just for branch coverage. It has no effect yet/here.

import unicodedata

def NFD(s):
	return unicodedata.normalize('NFD', s)

def NFC(s):
	return unicodedata.normalize('NFC', s)

normalize(NFC)

import unittest

class Test(unittest.TestCase):

	def eq(self, a, b):
		self.assertEqual(a, b)
		self.assertEqual(type(a) is type(b), true)

	#def ex(self, x, c, *a, **k):
	#	return self.assertRaises(x, c, *a, **k)

	def test_nameutils(self):

		# Test many cases (correct or only split wrong or case and split wrong)

		for case in test_cases:

			if case is none:

				self.eq(namecase(case), none) # 'namecase: undef'
				self.eq(gnamecase(case), none) # 'gnamecase: undef'
				self.eq(fnamecase(case), none) # 'fnamecase: undef'
				self.eq(namesplit(case), none) # 'namesplit: undef'
				self.eq(nameparts(case), []) # 'nameparts: undef'

			elif type(case) == list or type(case) == str and case.find(',') != -1:

				# An array contains the test name and the expected split failure
				expected_failure = none
				if type(case) == list:
					(case, expected_failure) = case

				(f, g) = split(', ', case)

				u1 = ', '.join([f, g]) # Unambiguous
				u2 = uc(u1)
				u3 = lc(u1)
				self.eq(namecase(u1), u1) # "namecase $u1 [$case]"
				self.eq(namecase(u2), u1) # "namecase $u2 [$case]"
				self.eq(namecase(u3), u1) # "namecase $u3 [$case]"

				a1 = ' '.join([g, f]) # Ambiguous
				a2 = uc(a1)
				a3 = lc(a1)
				self.eq(namecase(a1), a1) # "namecase $a1 [$case]"
				self.eq(namecase(a2), a1) # "namecase $a2 [$case]"
				self.eq(namecase(a3), a1) # "namecase $a3 [$case]"

				g1 = g
				g2 = uc(g)
				g3 = lc(g)
				self.eq(gnamecase(g1), g1) # "gnamecase $g1 [$case]"
				self.eq(gnamecase(g2), g1) # "gnamecase $g2 [$case]"
				self.eq(gnamecase(g3), g1) # "gnamecase $g3 [$case]"

				f1 = f
				f2 = uc(f)
				f3 = lc(f)
				self.eq(fnamecase(f1), f1) # "fnamecase $f1 [$case]"
				self.eq(fnamecase(f2), f1) # "fnamecase $f2 [$case]"
				self.eq(fnamecase(f3), f1) # "fnamecase $f3 [$case]"

				self.eq(fnamecase(f1, g1), f1) # "fnamecase $f1, $g1 [$case]" - Makes no difference without full name case exceptions
				self.eq(fnamecase(f2, g2), f1) # "fnamecase $f2, $g2 [$case]"
				self.eq(fnamecase(f3, g3), f1) # "fnamecase $f3, $g3 [$case]"

				self.eq(namesplit(u1), u1) # "namesplit $u1 [$case]"
				self.eq(namesplit(u2), u1) # "namesplit $u2 [$case]"
				self.eq(namesplit(u3), u1) # "namesplit $u3 [$case]"

				exp = expected_failure if expected_failure is not none else u1

				self.eq(namesplit(a1), exp) # "namesplit $a1 [$case]"
				self.eq(namesplit(a2), exp) # "namesplit $a2 [$case]"
				self.eq(namesplit(a3), exp) # "namesplit $a3 [$case]"

				self.eq(nameparts(u1), [f, g]) # "nameparts $u1 [$case]"
				self.eq(nameparts(u2), [f, g]) # "nameparts $u2 [$case]"
				self.eq(nameparts(u3), [f, g]) # "nameparts $u3 [$case]"

				self.eq(nameparts(a1), split(', ', exp)) # "nameparts $a1 [$case]"
				self.eq(nameparts(a2), split(', ', exp)) # "nameparts $a2 [$case]"
				self.eq(nameparts(a3), split(', ', exp)) # "nameparts $a3 [$case]"

			elif type(case) == dict:

				name = case['name']
				ncase = case['case']
				nsplit = case['split']

				n1 = name
				n2 = uc(name)
				n3 = lc(name)

				self.eq(namecase(n1), ncase) # "namecase $n1 [$ncase - expect wrong]"
				self.eq(namecase(n2), ncase) # "namecase $n2 [$ncase - expect wrong]"
				self.eq(namecase(n3), ncase) # "namecase $n3 [$ncase - expect wrong]"

				self.eq(namesplit(n1), nsplit) # "namesplit $n1 [$ncase - expect wrong]"
				self.eq(namesplit(n2), nsplit) # "namesplit $n2 [$ncase - expect wrong]"
				self.eq(namesplit(n3), nsplit) # "namesplit $n3 [$ncase - expect wrong]"

			else:

				n1 = case
				n2 = uc(case)
				n3 = uc(case)

				self.eq(namecase(n1), n1) # "namecase $n1"
				self.eq(namecase(n2), n1) # "namecase $n2"
				self.eq(namecase(n3), n1) # "namecase $n3"

				self.eq(gnamecase(n1), n1) # "gnamecase $n1"
				self.eq(gnamecase(n2), n1) # "gnamecase $n2"
				self.eq(gnamecase(n3), n1) # "gnamecase $n3"

				self.eq(fnamecase(n1), n1) # "fnamecase $n1"
				self.eq(fnamecase(n2), n1) # "fnamecase $n2"
				self.eq(fnamecase(n3), n1) # "fnamecase $n3"

				self.eq(namesplit(n1), n1) # "namesplit $n1"
				self.eq(namesplit(n2), n1) # "namesplit $n2"
				self.eq(namesplit(n3), n1) # "namesplit $n3"

				self.eq(nameparts(n1), ([n1] if len(n1) else [])) # "nameparts $n1"
				self.eq(nameparts(n2), ([n1] if len(n1) else [])) # "nameparts $n2"
				self.eq(nameparts(n3), ([n1] if len(n1) else [])) # "nameparts $n3"

		# Test nametrim

		for case in nametrim_cases:
			(input, output) = case
			self.eq(nametrim(input), output) # "nametrim '@{[$in // 'undef']}'"

		# Test case_exception

		#self.eq(namecase_exception(), 0) # "namecase_exception: noargs"
		self.eq(namecase_exception(none), 0) # "namecase_exception: undef"
		self.eq(namecase_exception(""), 0) # "namecase_exception: empty"

		for case in case_exception_cases:

			if case.find(',') != -1:
				(family, given) = split(', ', case)
			else:
				(family, given) = (case, none)

			if given is not none: # Individual case exception

				# Get the default values
				old_family = namecase(family, 'family')
				old_full = namecase(case, 'full')
				old_other = namecase(family + ', AnyBody', 'full')
				old_family_plus = fnamecase(family, given)
				old_family_plus_other = fnamecase(family, 'AnyBody')

				# Add the exception
				self.eq(namecase_exception(case), 1) # "namecase_exception: $case"

				# Get the corresponding new values
				new_family = namecase(family, 'family')
				new_full = namecase(case, 'full')
				new_other = namecase(family + ', AnyBody', 'full')

				new_family_plus_given_expected = (split(', ', case))[0] # Family part of the exception
				new_family_plus_given = fnamecase(family, given)
				new_family_plus_other = fnamecase(family, 'AnyBody')

				# Check that only the right ones are affected
				self.eq(new_family, old_family) # "namecase_exception($case): family [$new_family] should be [$old_family]"
				self.eq(new_full, case) # "namecase_exception($case): full [$new_full] should be [$case]"
				self.eq(new_other, old_other) # "namecase_exception($case): other [$new_other] should be [$old_other]"
				self.eq(new_family_plus_given, new_family_plus_given_expected) # "namecase_exception($case), fnamecase [$new_family_plus_given] should be [$new_family_plus_given_expected]"
				self.eq(new_family_plus_other, old_family_plus_other) # "namecase_exception($case), fnamecase [$new_family_plus_other] should be [$old_family_plus_other]"

				# Do the same with all uppercase
				new_family = namecase(uc(family), 'family')
				new_full = namecase(uc(case), 'full')
				new_other = namecase(uc(family + ', ' + "AnyBody"), 'full')

				new_family_plus_given = fnamecase(uc(family), uc(given))
				new_family_plus_other = fnamecase(uc(family), uc('AnyBody'))

				self.eq(new_family, old_family) # "namecase_exception($case): family [$new_family] should be [$old_family]"
				self.eq(new_full, case) # "namecase_exception($case): full [$new_full] should be [$case]"
				self.eq(new_other, old_other) # "namecase_exception($case): other [$new_other] should be [$old_other]"
				self.eq(new_family_plus_given, new_family_plus_given_expected) # "namecase_exception($case), fnamecase [$new_family_plus_given] should be [$new_family_plus_given_expected]"
				self.eq(new_family_plus_other, old_family_plus_other) # "namecase_exception($case), fnamecase [$new_family_plus_other] should be [$old_family_plus_other]"

				# Do the same with all lowercase
				new_family = namecase(lc(family), 'family')
				new_full = namecase(lc(case), 'full')
				new_other = namecase(lc(family + ", AnyBody"), 'full')

				new_family_plus_given = fnamecase(uc(family), uc(given))
				new_family_plus_other = fnamecase(uc(family), uc('AnyBody'))

				self.eq(new_family, old_family) # "namecase_exception($case): family [$new_family] should be [$old_family]"
				self.eq(new_full, case) # "namecase_exception($case): full [$new_full] should be [$case]"
				self.eq(new_other, old_other) # "namecase_exception($case): other [$new_other] should be [$old_other]"
				self.eq(new_family_plus_given, new_family_plus_given_expected) # "namecase_exception($case), fnamecase [$new_family_plus_given] should be [$new_family_plus_given_expected]"
				self.eq(new_family_plus_other, old_family_plus_other) # "namecase_exception($case), fnamecase [$new_family_plus_other] should be [$old_family_plus_other]"

			else:

				# Get the default values
				old_family = namecase(family, 'family')
				old_full = namecase(family + ", AnyBody", 'full')

				# Add the exception
				self.eq(namecase_exception(case), 1) # "namecase_exception: $case"

				# Get the corresponding new values
				new_family = namecase(family, 'family')
				new_full_expected = family + ", Anybody"
				new_full = namecase(new_full_expected, 'full')

				# Check that all uses are affected
				self.eq(new_family, family) # "namecase_exception($case): family ($new_family) should be ($family)"
				self.eq(new_full, new_full_expected) # "namecase_exception($case): other ($new_full) should be ($new_full_expected)"

				# Do the same with all uppercase
				new_family = namecase(uc(family), 'family')
				new_full = namecase(uc(new_full_expected), 'full')
				self.eq(new_family, family) # "namecase_exception(uc $case): family ($new_family) should be ($family)"
				self.eq(new_full, new_full_expected) # "namecase_exception(uc $case): other ($new_full) should be ($new_full_expected)"

				# Do the same with all lowercase
				new_family = namecase(lc(family), 'family')
				new_full = namecase(lc(new_full_expected), 'full')
				self.eq(new_family, family) # "namecase_exception(lc $case): family ($new_family) should be ($family)"
				self.eq(new_full, new_full_expected) # "namecase_exception(lc $case): other ($new_full) should be ($new_full_expected)"

		# Test split_exception

		#self.eq(namesplit_exception(), 0) # "namesplit_exception: noargs"
		self.eq(namesplit_exception(none), 0) # "namesplit_exception: undef"
		self.eq(namesplit_exception(""), 0) # "namesplit_exception: empty"
		self.eq(namesplit_exception("no comma"), 0) # "namesplit_exception: not an unambiguous full name"

		for case in split_exception_cases:

			(family, given) = split(', ', case)
			natural = given + ' ' + family
			natural_other = given + ' Anybody'

			old_split_given = namesplit(natural)
			old_split_other = namesplit(natural_other)

			namesplit_exception(case)

			self.eq(namesplit(natural), case) # "namesplit_exception($case) ($natural)"
			self.eq(namesplit(natural_other), old_split_other) # "namesplit_exception($case) ($natural_other)"

		# Test non-ASCII apostrophe/hyphen preservation/replacement for case and split

		for case in nonascii_punctuation_cases:

			first = case[0]

			namecase_exception(first)
			namesplit_exception(first)

			for next in case[1:]:

				(f, g) = split(', ', next)
				natural = g + ' ' + f

				self.eq(namecase(next), first) # "nonascii_punctuation namecase_exception($first): $next"
				self.eq(namecase(natural), first) # "nonascii_punctuation namecase_exception($first): $natural"

				self.eq(namesplit(next), first) # "nonascii_punctuation namesplit_exception($first): $next"
				self.eq(namesplit(natural), first) # "nonascii_punctuation namesplit_exception($first): $natural"

		# Test normalize

		for case in normalization_cases:

			(f, g) = split(', ', case)

			nfc_case = NFC(case)
			nfd_case = NFD(case)
			nfc_ucase = NFC(uc(case))
			nfd_ucase = NFD(uc(case))
			nfc_lcase = NFC(lc(case))
			nfd_lcase = NFD(lc(case))

			case_default = namecase(case)
			split_default = namecase(case)
			nfc_case_default = namecase(nfc_case)
			nfd_case_default = namecase(nfd_case)
			nfc_split_default = namesplit(nfc_case)
			nfd_split_default = namesplit(nfd_case)

			# Start with a known normalization (NFC matches, NFD doesn't)

			normalize(NFC)
			namecase_exception(nfc_case)
			namesplit_exception(nfc_case)

			self.eq(namecase(nfc_case), nfc_case) # "normalize(NFC) namecase(NFC $nfc_case)"
			self.eq(namecase(nfc_ucase), nfc_case) # "normalize(NFC) namecase(NFC $nfc_ucase)"
			self.eq(namecase(nfc_lcase), nfc_case) # "normalize(NFC) namecase(NFC $nfc_lcase)"

			self.eq(namesplit(nfc_case), nfc_case) # "normalize(NFC) namesplit(NFC $nfc_case)"
			self.eq(namesplit(nfc_ucase), nfc_case) # "normalize(NFC) namesplit(NFC $nfc_ucase)"
			self.eq(namesplit(nfc_lcase), nfc_case) # "normalize(NFC) namesplit(NFC $nfc_lcase)"

			self.eq(namecase(nfd_case), nfd_case_default) # "normalize(NFC) namecase(NFD $nfd_case)"
			self.eq(namecase(nfd_ucase), nfd_case_default) # "normalize(NFC) namecase(NFD $nfd_ucase)"
			self.eq(namecase(nfd_lcase), nfd_case_default) # "normalize(NFC) namecase(NFD $nfd_lcase)"

			self.eq(namesplit(nfd_case), nfd_split_default) # "normalize(NFC) namesplit(NFD $nfd_case)"
			self.eq(namesplit(nfd_ucase), nfd_split_default) # "normalize(NFC) namesplit(NFD $nfd_ucase)"
			self.eq(namesplit(nfd_lcase), nfd_split_default) # "normalize(NFC) namesplit(NFD $nfd_lcase)"

			# Renormalize and repeat (NFC doesn't match, NFD does)

			normalize(NFD)

			self.eq(namecase(nfc_case), nfc_case_default) # "normalize(NFD) namecase(NFC $nfc_case)"
			self.eq(namecase(nfc_ucase), nfc_case_default) # "normalize(NFD) namecase(NFC $nfc_ucase)"
			self.eq(namecase(nfc_lcase), nfc_case_default) # "normalize(NFD) namecase(NFC $nfc_lcase)"

			self.eq(namesplit(nfc_case), nfc_split_default) # "normalize(NFD) namesplit(NFC $nfc_case)"
			self.eq(namesplit(nfc_ucase), nfc_split_default) # "normalize(NFD) namesplit(NFC $nfc_ucase)"
			self.eq(namesplit(nfc_lcase), nfc_split_default) # "normalize(NFD) namesplit(NFC $nfc_lcase)"

			self.eq(namecase(nfd_case), nfd_case) # "normalize(NFD) namecase(NFD $nfd_case)"
			self.eq(namecase(nfd_ucase), nfd_case) # "normalize(NFD) namecase(NFD $nfd_ucase)"
			self.eq(namecase(nfd_lcase), nfd_case) # "normalize(NFD) namecase(NFD $nfd_lcase)"

			self.eq(namesplit(nfd_case), nfd_case) # "normalize(NFD) namesplit(NFD $nfd_case)"
			self.eq(namesplit(nfd_ucase), nfd_case) # "normalize(NFD) namesplit(NFD $nfd_ucase)"
			self.eq(namesplit(nfd_lcase), nfd_case) # "normalize(NFD) namesplit(NFD $nfd_lcase)"

		# Put normalization back to NFC so internal data agrees with this test source code.

		normalize(NFC)

		# Test Chinese namesplit

		for case in chinese_split_cases:

			(input, output) = case

			self.eq(namesplit(input), output) # "namesplit($in) Chinese"
			self.eq(namesplit(uc(input)), output) # "namesplit(@{[uc $in]}) Chinese"
			self.eq(namesplit(lc(input)), output) # "namesplit(@{[lc $in]}) Chinese"

			self.eq(nameparts(input), split(', ', output)) # "nameparts $in [$out] Chinese"

		# Test Korean namesplit

		for case in korean_split_cases:

			(input, output) = case

			self.eq(namesplit(input), output) # "namesplit($in) Korean"
			self.eq(namesplit(uc(input)), output) # "namesplit(@{[uc $in]}) Korean"
			self.eq(namesplit(lc(input)), output) # "namesplit(@{[lc $in]}) Korean"

			self.eq(nameparts(input), split(', ', output)) # "nameparts $in [$out] Korean"

		# Test Korean namesplit exceptions

		for case in korean_split_exception_cases:

			namesplit_exception(case)

			(f, g) = split(', ', case)

			input = g + ' ' + f
			self.eq(namesplit(input), case) # "namesplit($in) Korean exception"
			self.eq(namesplit(uc(input)), case) # "namesplit(@{[uc $in]}) Korean exception"
			self.eq(namesplit(lc(input)), case) # "namesplit(@{[lc $in]}) Korean exception"
			self.eq(nameparts(input), split(', ', case)) # "nameparts $in [$case] Korean"

			input = f + ' ' + g
			self.eq(namesplit(input), case) # "namesplit($in) Korean exception"
			self.eq(namesplit(uc(input)), case) # "namesplit(@{[uc $in]}) Korean exception"
			self.eq(namesplit(lc(input)), case) # "namesplit(@{[lc $in]}) Korean exception"
			self.eq(nameparts(input), split(', ', case)) # "nameparts $in [$case] Korean"

		# Test Vietnamese namesplit

		for case in vietnamese_split_cases:

			(f, g) = split(', ', case)

			input = f + ' ' + g
			self.eq(namesplit(input), case) # "namesplit($in) Vietnamese"
			self.eq(namesplit(uc(input)), case) # "namesplit(@{[uc $in]}) Vietnamese"
			self.eq(namesplit(lc(input)), case) # "namesplit(@{[lc $in]}) Vietnamese"

			self.eq(nameparts(input), split(', ', case)) # "nameparts $in [$case] Vietnamese"

		# Test Japanese namesplit

		for case in japanese_split_cases:

			(input, output) = case

			self.eq(namesplit(input), output) # "namesplit($in) Japanese"

			self.eq(nameparts(input), split(', ', output)) # "nameparts $in [$out] Japanese"

		# Test CJK namesplit exceptions

		for case in cjk_split_exception_cases:

			(f, g) = split(', ', case)

			namesplit_exception(case)

			self.eq(namesplit(f + g), case) # "namesplit($f$g) CJK split exception"

		# Test namejoin

		for case in namejoin_cases:

			(f, g, expected) = case

			self.eq(namejoin(f, g), expected) # "namejoin(@{[$f // 'none']}, @{[$g // 'none']})"

		# Test post-reset namecase exceptions

		nameutils_reset_data() # Undocumented internal function (for test coverage purposes only)

		for case in post_reset_case_exception_cases:

			(exception, followup) = case

			namecase_exception(exception)

			self.eq(namecase(exception), exception) # "post-reset namecase_exception: " . $exception;
			self.eq(namecase(uc(exception)), exception) # "post-reset namecase_exception: " . uc $exception;
			self.eq(namecase(lc(exception)), exception) # "post-reset namecase_exception: " . lc $exception;

			self.eq(namecase(followup), followup) # "post-reset namecase_exception follow-up: " . $followup;
			self.eq(namecase(uc(followup)), followup) # "post-reset namecase_exception follow-up: " . uc $followup;
			self.eq(namecase(lc(followup)), followup) # "post-reset namecase_exception follow-up: " . lc $followup;

unittest.main()

# vim:set ts=4 sw=4 fenc=utf8:
