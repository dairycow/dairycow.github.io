---
layout: post
title: 'Third crypto rotation'
date: 2021-02-08 19:40:00 +1100
---

I came across the following definition for Cryptocurrencies on Friday night

"Cryptocurrencies - bullshit internet tokens with no intrinsic value and prices based entirely on arbitrary speculative hype that nobody with any common sense should place large amounts of money into"

Sounds about right.

It feels like I am taking part in the greater fool theory.

On the other hand, the rate of development and introduction of new products is astonishing. Zero regulation has some benefits? 

The portfolio finished at $5,631.96. I don't have the exact figure for what it started the month with but it was about $2,200. In that case, we achieved a 155.98% return for the *month*. Obviously, the conditions were very favourable.

I need to address the issue with leveraged coins. It is common for assets in the cryptosphere to have drawdowns of 90%, inevitably wiping out some of these tokens (assuming that's how it actually works). Additionally, this month we have more than *doubled* exposure to the SUSHI token as we are invested in the token itself and the SUSHIUP token. 

I think I will have to remove them going forward. I don't believe you need nor want leverage in this space at the moment.

{% assign mydata=site.data.2021-02-08-cryptomomo %}

<table>
    <caption>Third crypto rotation</caption>
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

Doge on.