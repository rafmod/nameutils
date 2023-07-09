# README

*nameutils* - Identify given/family names and capitalize correctly

# Description

*nameutils* is a *python* module containing functions that can split a
person's full name into their given and family names, and capitalize the
letters appropriately. It understands complex names in Latin scripts from
many different languages, and it understands Chinese, Japanese, and Korean
names, in both their own characters, and romanized.

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

This is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License version 3 or later.

# Documentation

There is a manual entry:

- <https://raf.org/nameutils/manual/nameutils.3py.html>

# Download

*nameutils* is on PyPI:

- <https://pypi.org/project/nameutils>

And can be installed using *pip*:

        python3 -m pip install nameutils

# Requirements

*nameutils* is a *python* module that should work on systems with any
version of *python3*. It doesn't depend on any non-standard modules.

--------------------------------------------------------------------------------

    URL: https://raf.org/nameutils
    GIT: https://github.com/rafmod/nameutils
    GIT: https://codeberg.org/rafmod/nameutils
    Date: 20230709
    Author: raf <raf@raf.org>

