---
layout: post
title: 'Second crypto rotation'
date: 2021-01-11 20:10:00 +1100
---

An interesting month in the Crypto space. Bitcoin doubled, Ripple died and the Cryptomomo portfolio finished up 10.91%. It probably would have been pretty hard to lose money given the current market conditions. 

Good thing I have this portfolio to keep me invested in the space.

I doubled down and moved ~800 USDT from my market making account to this account. One thing I excluded last rotation was leveraged positions like BTCUPUSDT. I have left them in this rotation but will be reviewing them. 

Last month I coded the rebalance using the [python-binance](https://github.com/sammchardy/python-binance) library. This is simply an unofficial Python wrapper which made life a bit easier. I still had to convert dust manually and tinker around with the code to fill the last position. Nevertheless, in the future I aim to have this fully automated. 

I also intend on including some performance statistics but as this is a personal project the arrival of such things may take some time. 

{% assign mydata=site.data.2021-01-11-cryptomomo %}

<table>
    <caption>Second rotation - crpytomomo</caption>
    <thead>
    {% for column in mydata[0] %}
        <th>{{ column[0] }}</th>
    {% endfor %}
    </thead>
    <tbody>
    {% for row in mydata %}
        <tr>
        {% for cell in row %}
            <td>{{ cell[1] }}</td>
        {% endfor %}
        </tr>
    {% endfor %}
    </tbody>
</table>
