ISO 3166-1
~~~~~~~~~~~~

.. image:: https://badge.fury.io/py/iso-3166-1.svg
   :target: http://badge.fury.io/py/iso-3166-1

.. image:: https://travis-ci.org/spoqa/iso-3166-1.svg
   :target: https://travis-ci.org/spoqa/iso-3166-1

define codes for the names of countries as a enum_ it supports python2.7, 3.3
with enum34_ of course support python3.4 as well.

.. _enum: https://docs.python.org/3/library/enum.html
.. _enum34: https://pypi.python.org/pypi/enum34

.. code-block::

   >>> from iso3166 import Country
   >>> Country.kr
   <Country.kr>
   >>> Country.kr.alpha2
   KR
   >>> Country.kr.alpha3
   KOR
   >>> Country.kr.numeric
   410
   >>> Country.kr.english_short_name


Written by `Kang Hyojun`_.  Distributed under Public Domain.

.. _Kang Hyojun: http://github.com/admire93
