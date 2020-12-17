---
layout: post
title: 'First smord rotation'
date: 2020-12-17 19:40:00 +1100
---

I recently decided to run a systematic momentum strategy on ASX listed equities within the All Ordinaries (excluding the ASX 100). I figured that the market was running pretty hot and there really wasn't anything that could go wrong. brrr

Already, we have been exposed to some M&A arb (WPP) which is something I would never normally consider trading personally. Today there was a revised bid approximately 20% higher. It also helped lift the share price of SWM. 

First rotation:

{% assign mydata=site.data.2020-12-01-smordmomo %}

<table>
    <caption>First rotation - smordmomo</caption>
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

I will be rebalancing on the first trading day of the month. 