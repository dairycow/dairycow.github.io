---
layout: post
title: 'Second smord rotation'
date: 2021-01-04 19:40:00 +1100
---

At the end of the first rotation I had $9,921.43. This means that the fund was down -0.7877% for the month after transaction costs. Not bad considering at one point it was down over 7%. 

###### A drastic change to the smord portfolio. 

I switched broker to Invast which means I'll be using CFDs for the interim. Since I am doing 24 transactions/month this has the potential to save in transaction costs up until a certain portfolio value - I did some napkin math. Financing rates are approximately 3% per annum which is rediculously low. 

The main downfall to using a CFD broker is the credit risk if the broker goes under (which they often do). I figured that if they survived the liquidity event in March 2020 then they should be okay. To reduce some of this risk I can use a *responsible* amount of leverage (less money will be lost in case they go under). However, now I will have to seriously consider the portfolio's drawdowns. With 2x leverage a 50% drawdown will wipe me out. Past simulations of similar models to what I am running have shown maximum drawdowns between 50-70%. I have index and stock filters in my model so I hope to avoid this. 

{% assign mydata=site.data.2021-01-04-smordmomo %}

<table>
    <caption>End of first rotation and OpenTrader</caption>
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