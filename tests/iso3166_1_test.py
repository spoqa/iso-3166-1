from iso3166 import Country


def test_member_name_must_be_equal_to_alpha2_code():
    for member_name, e in Country.__members__.items():
        assert member_name == getattr(e, 'alpha2').lower()


def test_number_of_country():
    assert len(Country.__members__) == 249


def test_kr_is_korea_republic_of():
    assert Country.kr.english_short_name == 'Korea (Republic of)'
    assert Country.kr.alpha3 == 'KOR'
    assert Country.kr.numeric == 410
