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

"""
NAME
====

nameutils - Identify given/family names and capitalize correctly

SYNOPSIS
========

::

 from nameutils import (
     namecase, gnamecase, fnamecase, namecase_exception,
     namesplit, nameparts, namesplit_exception, namejoin,
     nametrim, normalize
 )

 # Case functions

 full_name = namecase(full_name)
 given_names = gnamecase(given_names) # i.e. Given name(s) only
 family_name = fnamecase(family_name) # i.e. Family name only
 family_name = fnamecase(family_name, given_names) # Individual exceptions

 namecase_exception("Fitzell") # Add an exception for all members of a family
 namecase_exception('DeVries', 'DiFrancesco') # Add more exceptions
 namecase_exception("Marrier D'Unienville, Jean") # Add an individual exception

 # Split functions

 full_name = namesplit(full_name) # Format as "Family_name, Given_names"

 (family_name, given_names) = nameparts(full_name) # Format as an array

 namesplit_exception("Bryant Smith, Denise") # Multi-name family names

 full_name = namejoin(family_name, given_names)

 # Trim function

 name = nametrim(name)

 # Unicode normalization of internal data (default is NFC)

 import unicodedata
 normalize(lambda s: unicodedata.normalize('NFD', s)))

DESCRIPTION
===========

This module is useful when receiving a person's name that might be all
uppercase, or in the wrong case, or it might have the given names and the
family name combined in a single string (e.g., a single spreadsheet column),
and you need to split the full name into its parts, and you want to set the
capitalization correctly so as to show each person a little respect by
taking the trouble to at least try to get their name right.

Getting the case right for people's names is difficult, and many software
systems address this problem by not even trying, and using uppercase
exclusively. It's ugly, but it's easy and consistent. We can do better. It
can't be perfect, by default, but with ongoing adjustments to suit your
evolving dataset, you can improve it to meet your needs.

People with complex grammatical aristocratic/topographic/patronymic family
names often don't know how their own names should be capitalized. Or at
least, they don't know how their own ancestors capitalized their name, or
they know, but they disagree with it. Some people insist on having it their
own way, and that's fine. This module, by default, prefers how their
ancestors would have capitalized their names, but people can do whatever
they want to their own names, and it's important to them, so this module
supports general exceptions that apply to everyone with a particular family
name, for when the default behaviour is definitely wrong, and it also
supports exceptions that apply only to individuals who report that it is
wrong for them.

Note: This module doesn't handle every name on Earth. Apart from Chinese,
Japanese, and Korean family names, it only understands names written in
Latin scripts, except perhaps by lucky accident. For example, names in
Cyrillic work. It doesn't handle honorifics, titles, joined initials, or
postnominals. It only handles names. But it does handle complex names coming
from a variety of places (e.g., British Isles, Europe, Middle East, Africa,
East Asia, Pacifika, Americas). By default, it doesn't correctly identify
unhyphenated multi-name family names (like Spanish and Catalan names, unless
the formal "y" or "i" is present). Such names need to be handled with split
exceptions. It handles some mixed case names like McAdam, MacArthur,
FitzSimmons, DeVito, VanZandt, etc., but there will be false negatives (and
arguably false positives) which can be corrected with case exceptions. Over
time, you will build up a set of case exceptions and split exceptions that
meets the needs of your dataset.

FUNCTIONS
=========

**name = namecase(name[, part[, given_names]])**
  Returns the supplied name with the capitalization fixed. See the **EXAMPLES**
  section below to see exactly what this means. This can be called in several
  ways:

  For a full name (implicitly)::

   full_name = namecase("JOHN PETER SMITH")
   full_name = namecase("SMITH, JOHN PETER")

  For a full name (explicitly)::

   full_name = namecase("JOHN PETER SMITH", 'full')
   full_name = namecase("SMITH, JOHN PETER", 'full')

  Note that the full name can be supplied in the (ambiguous) natural order,
  with the given name(s) followed by the family name, or unambiguously, with
  the family name followed by a comma followed by the given name(s).

  For a given name or names by itself (same as *gnamecase()*, see below)::

   given_names = namecase("JOHN PETER", 'given')

  For a family name by itself (same as *fnamecase()*, see below)::

   family_name = namecase("SMITH", 'family')

  For a family name by itself when you have (or might one day have) any case
  exceptions intended to only affect a single individual (same as
  *fnamecase()*, see below)::

   family_name = namecase("SMITH", 'family', "JOHN PETER")

**given_names = gnamecase(given_names)**
  Returns the supplied given name(s) with the capitalization fixed. Same as:
  ``namecase(given_names, 'given')``. Given names aren't capitalized in
  exactly the same way as family names.

**family_name = fnamecase(family_name[, given_names])**
  Returns the supplied family name with the capitalization fixed. Same as:
  ``namecase(family_name, 'family'[, given_names])``.
  
  The ``given_names`` argument is technically optional, but it should be
  supplied, just in case you ever need case exceptions that only apply to an
  individual. This enables people with the same family name to have their use
  of that family name capitalized the way they want it to be. Once you have a
  need for such individual case exceptions, the ``given_names`` argument will
  become necessary everywhere, so it's best to supply it from the start.

**namecase_exception(bespoke_capitalized_name, ...)**
  Add one or more case exceptions. Whenever the above case functions
  subsequently capitalize the supplied name, the supplied capitalization will
  be returned, rather than the default behaviour.

  There are two kinds of case exception. Some apply to everyone that shares a
  family name, and some apply to an individual.

  Family-wide exceptions contain the family name, capitalized correctly::

   namecase_exception("DiBona")

  Individual case exceptions must be supplied as unambiguous full names in the
  form: *"Family_name, Given_names"*, capitalized as specified by the
  named person::

   namecase_exception("DiBona, John")

  Returns 1 if the exception was successfully added. Returns 0 otherwise. The
  only reason for a failure is if the supplied exception is undefined or
  empty.

**full_name = namesplit(full_name)**
  Returns the supplied full name converted to the unambiguous form:
  *"Family_name, Given_names"* with the capitalization fixed.

  The ``full_name`` argument is expected to be in either form:
  *"Given_names Family_name"* or *"Family_name, Given_names"*. Note
  that a string is returned with the family name followed by a comma and space
  followed by the given name(s).

  Complex grammatical aristocratic/topographic/patronymic family names in
  Latin script are identified. See the **EXAMPLES** section below. But
  unhyphenated multi-name family names are not correctly identified by
  default. That requires split exceptions (see below). Spanish and Catalan
  multi-name family names are correctly identified when the two names are
  joined with "y" or "i", but when the joining word is not present, a split
  exception is needed.

  With Chinese, Japanese, and Korean names, the family name appears first when
  written in their own scripts/characters. When romanized, Chinese and Korean
  family names might appear first or last. The same is true for Vietnamese
  names.

  This module recognizes the 400 or so most common Chinese family names (97%
  of the population) in Chinese characters and in one romanized spelling, and
  additionally, the 100 most common Chinese family names (85% of the
  population) in pinyin and various other romanized spellings, as used in
  several countries. It also recognizes the 190 most common Korean family
  names (98% of the population) in Hangul, Hanja, and romanized. It also
  recognizes the 209 Vietnamese family names (100% of the population,
  apparently). There are too many Japanese family names (over 300,000) to
  maintain a list of them, so this module employs a statistical method to
  identify Japanese family names written in Kanji and Kana. I don't know
  what proportion of Japanese-named population it identifies.

**(family_name, given_names) = nameparts(full_name)**
  Returns the supplied full name converted to a two-element array containing
  the family name and the given name(s), with the capitalization fixed.

  The ``full_name`` argument is expected to be in either form:
  *"Given_names Family_name"* or *"Family_name, Given_names"*.

  This function converts the corresponding return value of *namesplit()* into
  a two-item array. See *namesplit()* above for more details. If the name
  contains a single "word", then it isn't splittable, and so a one-element
  array is returned. If the name is the empty string or undefined, then a
  zero-element array is returned

  Chinese, Japanese, and Korean names in their own scripts/characters contain
  multiple words even though they don't contain spaces between them. If a
  full name is supplied, this function will return a two-element array.

**namesplit_exception(full_name_in_comma_form, ...)**
  Add one or more split exceptions. The exceptions must be supplied as full
  names in the unambiguous comma-separated form with the family name followed
  by a comma and space followed by the given name(s).

  This is needed to support unhyphenated multi-name family names that aren't
  automatically identified, such as *"Ah Mu, Corie"*, and even complex
  given names that would be misrecognized, such as *"de Sousa, Fatima de Gois"*.

  This is also needed to correct the situation when this module misidentifies
  the type of name, and splits it incorrectly. For example, a Japanese name
  with a family name consisting of two characters might be misidentified as a
  Chinese name with a family name consisting of one character.

  Returns 1 if the exception was successfully added. Returns 0 otherwise. The
  only reason for a failure is if the supplied exception does not contain a
  comma.

**full_name = namejoin(family_name, given_names)**
  Returns the full name composed of the supplied family name and given names.

  Chinese, Japanese, and Korean names in their own scripts/characters are
  concatenated in Eastern name order (with the family name on the left). All
  names in Latin and other scripts are joined in Western name order (with the
  family name on the right), and with a space character added between the
  given names and the family name. Note that romanized Chinese, Japanese, and
  Korean names, and Vietnamese names, are always joined in Western name order.

**name = nametrim(name)**
  Returns the supplied name (given, family, or full name), with any leading
  and trailing spaces removed, any run of multiple spaces replaced with a
  single space, any space before a comma or around a hyphen-like character
  removed, and with a space added after any comma, if one is not already
  present there.

**normalize(func)**
  Normalize this module's internal data using the supplied Unicode
  normalization function reference so as to match your application's choice of
  normalization. A likely choice would be NFD.

  This is needed if the application's choice of Unicode normalization differs
  from whatever was used for the module's internal data in the module source
  code (i.e., NFC). A difference in normalization can lead to false negatives
  and incorrect results when matching names against internal data.

EXAMPLES
========

These examples show the default *namecase()* output for various forms of
names. They also show which name forms are automatically recognized by
*namesplit()*. Note that non-ASCII letters and punctuation in these
examples have been replaced with the closest ASCII equivalents to avoid
problems with some implementations of *\*roff*. *namesplit()* also supports
names in Chinese characters, Korean Hangul and Hanja, and Japanese Kanji and
Kana, but they are not shown here for the same reason::

 John Peter Smith
 William Maitland of Lethington

 Shaun McAdam
 Fergus MacDonald
 Lachlan Macquarie
 James FitzPatrick
 Patrick O'Brian
 Kelly St Clair

 David Le Page
 Pierre La Tour
 Rochelle Li Donni
 Giovanni Lo Giudice
 Estella d'Iapico-Bien
 Bruno dall'Agnese
 Bruno dell'Agnese
 Lorenzo de' Medici
 John de Groot
 Pierre de la Pierre
 Maria del Mar
 Maria dela Mar
 Maria dels Angels
 Giaccomo della Vella
 Giovanni delle Velle
 Maria dal Santos
 Marco dalla Vella
 Lorenza degli Castelli
 Maria di Francesco
 Giuseppe Tomasi di Lampedusa
 Pierre du Page
 Jorge da Silva
 Filipe do Santo
 Abilio dos Santos
 Adriana das Costas
 Oscar San Jose
 Catalina Santa Gutierrez
 Monica Santos Bernal

 Pablo Diego Ruiz y Picasso
 Carles Puigdemont i Casamajo
 Joao Duarte da Silva dos Santos da Costa de Sousa
 Joao Duarte da Silva Santos Costa e Sousa

 Hans von Pappenhim
 Thomas von der Trave
 Hans zu Pappenhim
 Hans von und zu Pappenhim

 Bram van Haag
 Jeroen der Haag
 Johanne ter Horst
 Sanne den Haag
 Laura van de Horst
 Eva van der Haag
 Willem van den Haag
 Mees van het Horst
 Henrik van Voorst tot Voorst 
 Willem 'sGravesande
 Gemeente van 'sHertogenbosch
 Gemeente van 'tHoen

 Sigurd av Morgenstierne
 Maja von Munthe af Morgenstierne
 Lars Jonsson til Sudreim

 James DaSilva
 Jack DuBois
 Daniel LaForge
 Sally LeFevre
 Kristine VanZandt

 Patrick O Donoghue
 Micheal O hAodha
 Saoirse Ni Fhoghlua
 Michael Mac Donnchada
 Saoirse Nic Fhoghlua
 Michael Ua Donoghue
 Aisling Bean Ui Fhoghlua
 Saoirse Bean Mhic Fhoghlua
 Saoirse Ui Fhoghlua
 Saoirse Mhic Fhoghlua

 Rhys ap Dafydd
 Maredudd ab Owain
 Myfanwy ferch Maredudd
 Myfanwy verch Maredudd

 Camilla El Ali
 Mariam Al Musawi
 Bazif el-Bayeh
 Nariman al-Nassar
 Hizb ut-Tahrir
 Aziz ibn Hab
 Charbel bin Hab
 Angela bint Aziz
 Fatima binti Aziz
 Nadia binte Aziz
 David Ben Joseph          # Incorrect when technically ambiguous
 ben Joseph, David         # Correct when technically unambiguous
 David ben Joseph v'Rachel # Correct - this is really not ambiguous
 Leah bat Moshe
 Leah bat Moshe v'Rachel ha-Rav
 Devorah Rut bat Mordecai v' Tzipporah
 Leah mibeit Moshe v'Rachel ha-Levi
 Leah mimishpachat Moshe v'Rachel ha-Kohein

 Natalie Te Whare

 Ayize ka Nolwazi

 Oso'ese
 Ya'akov
 Y'honatan
 Sh'mu'el
 Onosa'i
 Tausa'afia
 Ka'ana'ana
 S'thembiso

LIMITATIONS
===========

It's impossible to actually do what this module attempts to do in a way that
works correctly for everybody by default. There are too many people who want
their names cased incorrectly (e.g., Da Vinci rather than da Vinci),
and too many unhyphenated multi-name family names, and so many languages.
This module handles complex grammatical aristocratic/topographic/patronymic
(romanized) family names from various languages (e.g., French, Italian,
Spanish, Catalan, Portuguese, English, Irish, Welsh, Scottish, German,
Dutch, Swedish, Norwegian, Danish, Finnish, Zulu, Arabic, Hebrew), but there
are many more languages that it doesn't know about. So, in order to keep all
of your users happy, you will almost certainly need to build up your own
list of case and split exceptions in a file or database, and have your
application load them before processing any names. But if two people with
exactly the same full name both insist on having their name capitalized
differently to each other, that's not supported.

Different languages can have different case conventions for the same
"word". For example, a Greek family name can start with *el*, but a Spanish family
name can start with *El*. This module favours the most likely case (i.e.,
Spanish in this example). For other cases, this can be corrected with case
exceptions.

Similarly, a Hebrew patronymic name can start with *ben*, but an Anglo
given name can be *Ben*. That's fine if *fnamecase()* or *gnamecase()*
are used, supplied with just the given name(s) or the family name,
respectively, but *namecase()* supplied with an ambiguous full name will
favour the Anglo interpretation. That is, unless the name contains other
elements that make it obviously Hebrew, such as a matronymic component
(e.g., v'Rachel), or a suffix such as ha-Rav. That will cause a technically
ambiguous *ben* to be correctly identified as a patronymic prefix.

Similarly, when it comes to splitting/identifying the given names and the
family name within a full name with *namesplit()* or *nameparts()*, the
word *ben* is not interpreted as the start of a patronymic name (in the
absence of other clues as indicated above), because *Ben* is more likely to
be an Anglo middle name (although *bat* is always interpreted as the start
of a patronymic name). Luckily, Hebrew names aren't used much outside of
religious contexts, so this hopefully won't be much of a problem for this
module. If it is, it can be corrected with split exceptions (or with more
detailed Hebrew names).

Romanized Chinese, Korean and Vietnamese family names can appear at the
start or at the end of a full name. This module detects them in either
format. But there can be false positives when a Chinese or Korean family
name is at the end of the full name, and the given name also looks like a
Chinese or Korean family name. For example, *namesplit()* works better for
Korean names where the family name appears at the start rather than at the
end, because some Korean given names look like a family name. Other odd
cases might arise due to never knowing which language a romanized name is
from. But split exceptions should help when these cases are noticed.

CAVEAT
======

Unicode strings are complicated. Some graphemes can occur in multiple ways.
Any case and split exceptions are looked up via a hash key match. To
increase the chance of matches succeeding when they should, you should
probably normalize strings on input to your application using something like
*NFD* (or maybe even *Stringprep*) before
passing names to this module which assumes that any necessary preparation
has already been done. If necessary, you can normalize this module's
internal data (with *normalize()*) to match your application's choice of
normalization.

BUGS
====

The *nameparts()* function probably should have been called *namesplit()*,
because it returns an array, and the *namesplit()* function probably should
have been called something else, because it returns a string. But they are
the names I'm used to, and I couldn't think of anything better, and now it's
too late to change it.

Space characters are not preserved. Spaces at the start or end of a name are
removed, as are spaces before commas, and before and after hyphens. There
will always be a space after a comma. Any non-ASCII spaces are replaced with
ASCII space. Let me know if that's a problem. It can probably be fixed, but
I think it's a feature. If it's any consolation, non-ASCII apostrophe-like
characters and hyphen-like characters are preserved. But if there is a case
exception involving any apostrophe-like or hyphen-like characters, then they
too are replaced by the actual character specified in the exception.

HISTORY
=======

A (less comprehensive) version of this module (in another language) has been
in use for over fifteen years at a small company with a dataset of about
fifty thousand names. With that dataset, six generic case exceptions were
needed, two individual case exceptions, and about nine hundred split
exceptions.

It enabled the accurate identification of names in spreadsheets so as to
check against ID number columns, and it made reports containing people's
names much prettier than they would otherwise have been.

SEE ALSO
========

unicodedata, stringprep

AUTHOR
======

20230709 raf <raf@raf.org>

COPYRIGHT AND LICENSE
=====================

Copyright (C) 2023 raf <raf@raf.org>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

"""

__docformat__ = 'reStructuredText'

# This is just a module, not a package with submodules

from .nameutils import \
(
	namecase, gnamecase, fnamecase, namecase_exception,
	namesplit, nameparts, namesplit_exception, namejoin,
	nametrim, normalize,

	nameutils_reset_data # Undocumented, for test coverage purposes only
)

# vi:set ts=4 sw=4:
