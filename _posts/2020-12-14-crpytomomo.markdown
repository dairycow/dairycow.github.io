---
layout: post
title: 'First crypto rotation'
date: 2020-12-14 19:40:00 +1100
---

I have been out of the crypto game for a while but recently found myself reinterested after catching up with someone I hadn't seen for a while. The timing of such discussions worked well, as recently, I had been exploring systematic momentum strategies on equities. 

I decided to apply the methodology to the crypto space. I had to act quick though, as I tend to lose interest in these sort of projects very quickly. I came up with the idea on Monday, and by that evening I loaded a grand AUD into USDT and split it evenly across the following twelve assets:

{% assign mydata=site.data.2020-12-14-cryptomomo %}

<table>
    <caption>First rotation - crpytomomo</caption>
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

I will be rebalancing on the second Monday of each month. I may do an in-depth post on the methodology in the future. 