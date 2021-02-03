---
layout: post
title: 'Third smord rotation'
date: 2021-02-03 18:40:00 +1100
---

At the end of the second rotation I had $10,182.12. This means that the strategy was up 2.63% for the month after transaction costs. This month was strong, at one point we were up around 10%. Material exposures did well. We had an interesting and aggressive selloff in global markets near the end of the month. So far, things have since recovered. It was pretty funny observing the GME hype - one for the game theorists out there.

Hopefully the materials continue their strength as there is a very heavy weighting towards them in the next rotation. There is a lot of exposure to battery metals. Not sure how I feel about that but I guess that's why we have data making our decisions.  

{% assign mydata=site.data.2021-02-03-smordmomo %}

<table>
    <caption>Third rotation</caption>
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