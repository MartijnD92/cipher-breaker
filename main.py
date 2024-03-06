#! /usr/bin/env python3

import re
import pprint

def generate_freq_table(input_txt: str) -> dict[str]:
    table = {}
    for i, char in enumerate(input_txt):
        lchar = char.lower()
        
        # skip non-word characters
        if re.match(r'\W', char):
            continue
        
        try:
            prev_char = input_txt[i-1].lower() if re.match(r'\w', input_txt[i-1]) else 'wb'
            next_char = input_txt[i+1].lower() if re.match(r'\w', input_txt[i+1]) else 'wb'
        except IndexError:
            prev_char = 'wb'
            next_char = 'wb'
        
        # First occurence; initialization
        if lchar not in table:
            table[lchar] = {
                'occurrences': 1,
                'percentage': round(1 / len(input_txt) * 100, 2),
                'neighbors': { prev_char: 1, next_char: 1 }
            }
        else:
            table[lchar]['occurrences'] += 1
            table[lchar]['percentage'] = round(table[lchar]['occurrences'] / len(input_txt) * 100, 2)
            
            for c in [prev_char, next_char]:
                if c not in table[lchar]['neighbors']:
                    table[lchar]['neighbors'][c] = 1
                else:
                    table[lchar]['neighbors'][c] += 1
                
    return table
                

def main():
    plain_input = "Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time tozz get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me."
    
    cipher_input = "PCQ VMJYPD LBYK LYSO KBXBJXWXV BXV ZCJPO EYPD KBXBJYUXJ LBJOO KCPK. CP LBO LBCMKXPV XPV IYJKL PYDBL, QBOP KBO BXV OPVOV LBO LXRO CI SX'XJMI, KBO JCKO XPV EYKKOV LBO DJCMPV ZOICJO BYS, KXUYPD: DJOXL EYPD, ICJ X LBCMKXPV XPV CPO PYDBLK Y BXNO ZOOP JOACMPLYPD LC UCM LBO IXZROK CI FXKL XDOK XPV LBO RODOPVK CI XPAYOPL EYPDK. SXU Y SXEO KC ZCRV XK LC AJXNO X IXNCMJ CI UCMJ SXGOKLU? OFYRCDMO, LXROK IJCS LBO LBCMKXPV XPV CPO PYDBLK"
    
    freq_org = generate_freq_table(plain_input)
    freq_ciph = generate_freq_table(cipher_input)
    
    
    three_commonest_org = sorted(freq_org.items(), key=lambda item: item[1]['occurrences'], reverse=True)[:3]
    three_commonest_ciph = sorted(freq_ciph.items(), key=lambda item: item[1]['occurrences'], reverse=True)[:3]
    
    pprint.pp(three_commonest_org)
    pprint.pp(three_commonest_ciph)
    
    
  
         
if __name__ == '__main__':
    main()
