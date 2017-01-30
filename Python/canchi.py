#!/usr/bin/env python
# -*- coding: utf-8 -*-

zhi_map = {
    0: "Thân", 1: "Dậu", 2: "Tuất", 3: "Hợi", 4: "Tí", 5: "Sửu",
    6: "Dần", 7: "Mão", 8: "Thìn", 9: "Tỵ", 10: "Ngọ", 11: "Mùi"
}


def get_branch(year):
    # 12 con giáp
    # zhi - branch - chi
    return zhi_map[year % 12]


print get_branch(2017)
