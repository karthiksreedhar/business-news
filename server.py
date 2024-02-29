from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

import os
import openai
import PyPDF2

import secrets
openai.api_key = 'GPT-API-KEY'

import json
from base64 import b64decode
from pathlib import Path

headline_data = {
    "context": "",
    "ticker": "",
    "coverage": "",
    "article-1-source": "",
    "article-1-title": "",
    "article-1-date": "",
    "article-1-summary": "",
    "article-1-url": "",
    "article-2-source": "",
    "article-2-title": "",
    "article-2-date": "",
    "article-2-summary": "",
    "article-2-url": "",
    "article-3-source": "",
    "article-3-title": "",
    "article-3-date": "",
    "article-3-summary": "",
    "article-3-url": "",
    "article-4-source": "",
    "article-4-title": "",
    "article-4-date": "",
    "article-4-summary": "",
    "article-4-url": "",
    "bull-case": "",
    "bear-case": "",
    "custom": ""
}

news = {
    'nvidia': [

        {'source': 'Yahoo Finance',
        'date': 'February 28, 2024',
        'title': 'Nvidia Is Still Hot, but These 2 Artificial Intelligence (AI) Stocks Could Fizzle Out',
        'text': 'Nvidia (NASDAQ: NVDA) became one of the hottest tech stocks over the past decade as the artificial intelligence (AI) market expanded. The chipmaker, which had previously generated most of its revenue from gaming GPUs, expanded into the data center space with more powerful GPUs that made it easier to process AI tasks. That first-mover\'s advantage lit a fire under Nvidia\'s business as large companies upgraded their AI capabilities. As a result, its revenue grew at an impressive compound annual growth rate (CAGR) of 31% from fiscal 2014 to fiscal 2024 (which ended this January) while its stock skyrocketed 16,570% over the past 10 years. Analysts expect its revenue to continue growing at a CAGR of 35% from fiscal 2024 to fiscal 2027. Those growth rates suggest Nvidia remains one of the easiest ways to profit from the secular expansion of the AI market. Unfortunately, not every tech company that focuses on the AI market is destined to be a long-term winner like Nvidia. So today, I\'ll focus on two weaker AI stocks that could fizzle out even as the broader market expands: AI software maker C3.ai (NYSE: AI) and auto chipmaker Mobileye (NASDAQ: MBLY). C3.ai faces existential challenges C3.ai develops AI algorithms that can be plugged into a company\'s existing software to automate, streamline, and accelerate certain tasks. That strategy sounds promising, but it faces a lot of competition and generates about 30% of its revenue from a joint venture with the energy giant Baker Hughes. That deal is set to expire in fiscal 2025 (which ends in April 2025), and there\'s no guarantee it will be renewed. Mobileye faces a severe cyclical slowdown Mobileye, which was spun off from Intel in an IPO in 2022, is the world\'s top producer of advanced driver assistance systems (ADAS), which use chips, cameras, and sensors to help drivers park their cars, stay in the correct lane, and tap other semiautonomous driving features. These systems are powered by its own EyeQ computer vision chips, which are manufactured by its longtime partner STMicroelectronics (NYSE: STM) instead of Intel\'s own foundries. Mobileye might seem like a great way to invest in the growth of the connected and driverless vehicle markets, but it faces a rough slowdown. Its revenue rose 22% in 2022 and 11% in 2023, but it expects a 6% to 12% revenue decline in 2024. Back in 2021 and 2022, many of Mobileye\'s clients stocked up on too many EyeQ chips to insulate themselves from the supply chain headwinds. Mobileye also ramped up its chip orders from STMicroelectronics in the second half of 2022 to address its supply chain disruptions in the first half of the year. Those two factors caused Mobileye to suffer a supply glut of about 6 million to 7 million EyeQ chips at the end of 2023. Analysts expect its adjusted earnings to plunge 51% this year as it slogs through those excess inventories. Mobileye will likely recover from this cyclical downturn over the next few years, but its stock looks too expensive right now at 62 times forward earnings -- even after it lost nearly 40% of its value over the past 12 months. Intel, which still owns a majority stake in Mobileye, also sold a $1.5 billion stake in the company last year -- so it might be prudent to shun this out-of-favor chip stock until a few more green shoots appear. Should you invest $1,000 in Nvidia right now? Before you buy stock in Nvidia, consider this: The Motley Fool Stock Advisor analyst team just identified what they believe are the 10 best stocks for investors to buy now… and Nvidia wasn’t one of them. The 10 stocks that made the cut could produce monster returns in the coming years. Stock Advisor provides investors with an easy-to-follow blueprint for success, including guidance on building a portfolio, regular updates from analysts, and two new stock picks each month. The Stock Advisor service has more than tripled the return of S&P 500 since 2002.',
        'url': 'https://finance.yahoo.com/news/nvidia-still-hot-2-artificial-101500287.html'},

        {'source': 'The Economist',
        'date': 'February 27, 2024',
        'title': 'Why do Nvidia’s chips dominate the AI market?',
        'text': 'No other firm has benefited from the boom in artificial intelligence (ai) as much as Nvidia. Since January 2023 the chipmaker’s share price has surged by almost 450%. With the total value of its shares approaching $2trn, Nvidia is now America’s third-most valuable firm, behind Microsoft and Apple. Its revenues for the most recent quarter were $22bn, up from $6bn in the same period last year. Most analysts expect that Nvidia, which controls more than 95% of the market for specialist ai chips, will continue to grow at a blistering pace for the foreseeable future. What makes its chips so special? Nvidia’s ai chips, also known as graphics processor units (gpus) or “accelerators”, were initially designed for video games. They use parallel processing, breaking each computation into smaller chunks, then distributing them among multiple “cores”—the brains of the processor—in the chip. This means that a gpu can run calculations far faster than it would if it completed tasks sequentially. This approach is ideal for gaming: lifelike graphics require countless pixels to be rendered simultaneously on the screen. Nvidia’s high-performance chips now account for four-fifths of gaming gpus. Happily for Nvidia, its chips have found much wider uses: cryptocurrency mining, self-driving cars and, most important, training of ai models. Machine-learning algorithms, which underpin ai, use a branch of deep learning called artificial neural networks. In these networks computers extract rules and patterns from massive datasets. Training a network involves large-scale computations—but because the tasks can be broken into smaller chunks, parallel processing is an ideal way to speed things up. A high-performance gpu can have more than a thousand cores, so it can handle thousands of calculations at the same time. Once Nvidia realised that its accelerators were highly efficient at training ai models, it focused on optimising them for that market. Its chips have kept pace with ever more complex ai models: in the decade to 2023 Nvidia increased the speed of its computations 1,000-fold. But Nvidia’s soaring valuation is not just because of faster chips. Its competitive edge extends to two other areas. One is networking. As ai models continue to grow, the data centres running them need thousands of gpus lashed together to boost processing power (most computers use just a handful). Nvidia connects its gpus through a high-performance network based on products from Mellanox, a supplier of networking technology that it acquired in 2019 for $7bn. This allows it to optimise the performance of its network of chips in a way that competitors can’t match. Nvidia’s other strength is cuda, a software platform that allows customers to fine tune the performance of its processors. Nvidia has been investing in this software since the mid-2000s, and has long encouraged developers to use it to build and test AI applications. This has made cuda the de facto industry standard.',
        'url': 'https://www.economist.com/the-economist-explains/2024/02/27/why-do-nvidias-chips-dominate-the-ai-market'},

        {'source': 'Investor\'s Business Daily',
        'date': 'February 28, 2024',
        'title': 'Nvidia Takes Next Steps; Is Nvidia A Buy?',
        'text': 'Nvidia (NVDA) soared after earnings were announced Feb. 21, and the stock went on to clear the 800 level. But shares of the artificial intelligence giant have faltered since, and fallen back below the 800 threshold. So is Nvidia a buy now? Nvidia delivered yet another beat-and-raise quarter Wednesday. Earnings of $5.16 per share on sales of $22.1 billion beat views of $4.59 earnings per share and $20.4 billion in sales. On Wednesday, the AI leader partnered with ServiceNow (NOW) to release an open-access platform for coders. Earlier, the company observed that limited supply of AI chips as the biggest challenge to growth. Customers may also wait for the next generation B100 chip that is expected in the coming quarters. On Tuesday, Baird analysts  saw this as a good thing. B100 chips will have better performance and will likely have a higher average selling price. The AI-chip maker also disclosed its recent stakes in several smaller AI plays in a filing with the Securities and Exchange Commission. Also in February, Chief Executive Jensen Huang gave a rosy outlook for data center spending — a key segment for Nvidia. Does that mean Nvidia stock is a buy now? At the World Government Summit in Dubai, Huang said that \"over the course of the next four or five years we\'ll have \$2 trillion worth of data centers that will be powering software around the world, and all of i\'s going to be accelerated.\" Huang added that countries can now \"create computing technologies that nobody has to program.\" \"Everybody in the world is now a programmer.\" Next Steps So what is next for the stock? On Monday, Nvidia announced that its advanced chips will be available in portable workstations and will accelerate video streaming and other content related tasks. The chips will be available on workstations made by Dell Technologies (DELL), Lenovo (LNVGY) and other companies. Charting Nvidia\'s Price Targets IBD MarketSmith\'s chart tools show that shares of the \"Magnificent Seven\" stock rose after analysts at KeyBanc raised their price target for the artificial intelligence leader to 740 from 650. Also in January, quarterly reports from Taiwan Semiconductor (TSM) and ASML (ASML) gave chip stocks a boost. Earlier in January, the leading maker of artificial intelligence chips disclosed at CES new GeForce graphic processors. The chips are designed  for AI-enabled laptops and PCs. It also said electric vehicles are using its automated driving system. Li Auto (LI) and other EV makers have selected Nvidia Drive Thor for their fleets. The leader in AI chips rallied 239% in 2023 and hit an all-time high 505.48 just before the year ended. Then it topped, the 505.48 buy point of its base in heavy volume on Jan. 8. Nvidia Stock: Third-Quarter Earnings Shares broke out of a double-bottom base just ahead of third-quarter earnings in November. A week before reporting results, Nvidia announced at the SC23 supercomputing conference in Denver a new artificial intelligence computing platform and an advanced data-center chip. Despite a blockbuster quarter, shares fell after the earnings report. The company said profits came in at $4.02 a share. That came on sales of $18.12 billion for the period ended Oct. 29. Analysts polled by FactSet had expected earnings of $3.37 a share on sales of $16.19 billion. Compared with the year-ago quarter, Nvidia earnings soared 593%, while sales saw a 206% spike. Demand from data centers was the chief reason. Nvidia\'s data-center sales jumped 279% from the year-earlier period to a record $14.51 billion. Data-center sales also increased 41% from the second quarter. AI Products Drive Growth Nvidia has earned a reputation for being a trailblazer. The company was an early pioneer in the graphics processors that many say drastically improved computer gaming. Along with gaming, Nvidia chips now are used in such industries as health care, automobiles and robotics. In March, generative AI took a leap with OpenAI\'s ChatGPT. According to the company, Nvidia\'s AI-capable supercomputer paved the way for the \"iPhone moment of AI.\" That helped Nvidia turn the tide on its results. It reported three quarters of declining year-over-year sales and four quarters of tapering earnings. But then the company achieved record top- and bottom-line growth in the two most recent quarters. Nvidia stock shows exceptional technical strength and boasts a best-possible score of 99 on both its Composite Rating and EPS Rating. Its Relative Strength Rating of 98 also shows that it outperforms the vast majority of stocks in the Investor\'s Business Daily database. Nvidia also is one of the Magnificent Seven stocks that led the 2023 stock rally. The other stocks are Apple (AAPL), Microsoft (MSFT), Alphabet (GOOGL), Meta Platforms (META), Tesla (TSLA) and Amazon (AMZN). Some of these tech titans are customers that rely on Nvidia\'s advanced chips. It is also one of the \"Magnificent Seven of 2024.\" Nvidia stock currently ranks first in the fabless semiconductor group, which holds 16th place among IBD\'s 197 industry groups. The AI stock frequently appears on the IBD 50, IBD Sector Leaders and Tech Leaders lists. Further, the stock is on IBD Leaderboard. In November, Nvidia stock jumped 15% and outperformed the Nasdaq\'s 10.70% gain. But in December, it finished up 6%, just above the Nasdaq\'s 5.5\% advance for the month. Is Nvidia A Stock A Buy? The stock holds an Accumulation/Distribution Rating of B. That shows strong interest among institutional buyers in the last 13 weeks. Overall worldwide AI chip revenue will grow 26% from $53.4 billion in 2023 to $67.1 billion in 2024, according to a recent report from research firm Gartner. That is set to double by 2027 to $119 billion Nvidia\'s graphic processing units help accelerate computing in data centers and AI applications. Nvidia stock is not a buy right now. Shares are extended from a buy zone that originated from a flat base\'s 505.48 entry.',
        'url': 'https://www.investors.com/research/nvda-stock-has-gained-this-year-but-is-nvidia-a-buy/'},

        {'source': 'Investor\'s Business Daily',
        'date': 'February 28, 2024',
        'title': 'Dow Jones Slides 200 Points On Surprise GDP Data; Cathie Wood Sells More Nvidia Stock',
        'text': 'The Dow Jones Industrial Average and the other major indexes dropped after weaker-than-expected GDP data ahead of the opening bell Wednesday. Meanwhile, famed investor Cathie Wood continued to sell shares of Nvidia (NVDA) on the stock market today. The Dow Jones Industrial Average lost 0.4% in morning action, while the S&P 500 was down 0.3%. The tech-heavy Nasdaq composite dropped 0.6% after the opening bell. Among U.S. exchange traded funds, the Nasdaq 100 tracker Invesco QQQ Trust (QQQ) exchange traded fund was down 0.6%, as the SPDR S&P 500 ETF (SPY) fell 0.3%. The 10-year Treasury yield ticked lower to 4.29%. Further, oil prices continue to hover around their recent highs, as West Texas Intermediate futures inched lower, back near $79 a barrel. Cathie Wood\'s Ark Genomic Revolution (ARKG) ETF sold nearly 6,700 shares of Nvidia stock Tuesday, or about $5.2 million worth using the closing price, per daily trade disclosures. On Monday, the fund sold another 2,700 shares of Nvidia.',
        'url': 'https://www.investors.com/market-trend/stock-market-today/dow-jones-nasdaq-sp500-cathie-wood-nvidia-nvda-stock/'
        }
    ]
}

@app.route('/ticker_news', methods = ['GET', 'POST'])
def ticker_news():
    global headline_data
    data = request.get_json()

    headline_data['context'] = data['context']
    headline_data['ticker'] = data['ticker']

    ticker = headline_data['ticker']
    ticker_news = news[headline_data['ticker']]

    headline_data['article-1-source'] = ticker_news[0]['source']
    headline_data['article-1-date'] = ticker_news[0]['date']
    headline_data['article-1-title'] = ticker_news[0]['title']
    headline_data['article-1-url'] = ticker_news[0]['url']

    article = ticker_news[0]['text']
    prompt = f"You are going to be given an article about {ticker} stock. Summarize the article in a few sentences, bolding key metrics or information that may affect the stock price. The article is here: {article}"
    response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=256)["choices"][0]["text"]
    headline_data['article-1-summary'] = response

    headline_data['article-2-source'] = ticker_news[1]['source']
    headline_data['article-2-date'] = ticker_news[1]['date']
    headline_data['article-2-title'] = ticker_news[1]['title']
    headline_data['article-2-url'] = ticker_news[1]['url']

    article = ticker_news[1]['text']
    prompt = f"You are going to be given an article about {ticker} stock. Summarize the article in a few sentences, bolding key metrics or information that may affect the stock price. The article is here: {article}"
    response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=256)["choices"][0]["text"]
    headline_data['article-2-summary'] = response

    headline_data['article-3-source'] = ticker_news[2]['source']
    headline_data['article-3-date'] = ticker_news[2]['date']
    headline_data['article-3-title'] = ticker_news[2]['title']
    headline_data['article-3-url'] = ticker_news[2]['url']

    article = ticker_news[2]['text']
    prompt = f"You are going to be given an article about {ticker} stock. Summarize the article in a few sentences, bolding key metrics or information that may affect the stock price. The article is here: {article}"
    response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=256)["choices"][0]["text"]
    headline_data['article-3-summary'] = response

    headline_data['article-4-source'] = ticker_news[3]['source']
    headline_data['article-4-date'] = ticker_news[3]['date']
    headline_data['article-4-title'] = ticker_news[3]['title']
    headline_data['article-4-url'] = ticker_news[3]['url']

    article = ticker_news[3]['text']
    prompt = f"You are going to be given an article about {ticker} stock. Summarize the article in a few sentences, bolding key metrics or information that may affect the stock price. The article is here: {article}"
    response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=256)["choices"][0]["text"]
    headline_data['article-4-summary'] = response

    # prompt = f"Make a short bull case for {ticker}. Format your output as a list that can be directly placed into a HTML <text> element."
    # response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=256)["choices"][0]["text"]
    # headline_data["bull-case"] = response

    # prompt = f"Make a short bear case for {ticker}. Format your output as a list that can be directly placed into a HTML <text> element."
    # response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=256)["choices"][0]["text"]
    # headline_data["bear-case"] = response

    context = headline_data['context']
    prompt = f"You are going to be given some information about a retail investor and their connection to {ticker} stock. Write one sentence that rephrases the information about them in the second person. The information is here: {context}"
    response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=256)["choices"][0]["text"]
    headline_data["custom"] = response 

    return jsonify(headline_data)

@app.route('/')
def home():
    # you can pass in an existing article or a blank one.
    return render_template('home.html', data=headline_data)   


if __name__ == '__main__':
    # app.run(debug = True, port = 4000)    
    app.run(debug = True)




