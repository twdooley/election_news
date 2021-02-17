# NLP Analysis of Breitbart.com
## Timothy W. Dooley (LASSO)
### METIS Project 4

----------------------------------
## Objective:

To understand the language used by self-described "alt-right" media site Breitbart.com.

## Contents
* BreitBot, a Breitbart headline generator trained on nearly 16,000 election articles can be found at this [link](https://huggingface.co/twdooley/breitbot?text=). You can also follow the bot on twitter [@realBreitBot](https://twitter.com/realBreitBot)
* `scrapebart.py` and `merger.py` were built to sequentially scrape the site for articles before the Election and continually until 11 November. 
* `nlp_clean.ipynb` presents the bulk of analysis and model making. The images generated can be found in the `images` directory in this repo. 
* `breit_transformers.ipynb` used the transformers library to examine the data. In particular, I used this notebook to sentiment score the main csv.
* `breit.ipynb` trains "BreitBot". Huge credit to Richard Bownes, PhD and his article ["Fine Tuning GPT-2 for Magic the Gathering Flavour Text Generation"](https://medium.com/swlh/fine-tuning-gpt-2-for-magic-the-gathering-flavour-text-generation-3bafd0f9bb93) 


## Methods:
I scraped almost 16,000 articles under Breitbart's "Election" section from March 2019 - 11 November 2020. Multiple methods were employed.
<br>
*Topic Modeling* Non-Negative Matrix Factorization
*Sentiment Scoring* Hugging Face Transformers
*Headline Generator* GPT-2, Transformers, Pytorch

## Findings 
After cleaning and preprocessing the text, the words were vectorized and dimensions were reduced with a number of algorithms. I eventually settled on Non-Negative Matrix Factorization for dimensionality reduction. 
NMF yielded the following topics:

1. BLM/Race/Identity Politics/Police
2. DNC Bogetmen of Sanders, Warren, Buttigieg (and Bloomberg)
3. Joe Biden (note the negative association with the Reade scandal)
4. Mail Voting and "Fraud"
5. Trump. (note the positive association with rallies, supporters. Note also that Covid is a sub-topic of Trump)
6. Impeachment
7. Immigration
8. Kamala Harris
9. Hunter Biden, Burisma, Ukraine (Breitbart's October Surprise)
10. SCOTUS and Amy Coney Barrett 

<br>
There is much insight in these top ten topics. I will list a few in no particular order below. 

* Coronavirus/Covid-19 did not appear as its own topic. Rather, it formed a subtopic almost always associated with Trump. 
* Hunter Biden was a significant topic for Breitbart. In the month of October his topic accounted for more articles than his father, the Democratic nominee and President-Elect.
* Racial Politics and support for the police did not see a significant spike in the wake of the murders of George Floyd, Ahmaud Arbery, and Breonna Taylor. 
Instead, this topic occupies a rather consistent tranche of articles throughout the scope of this investigation. 
* Perhaps most interestingly, the focus on postal voting and supposed 'fraud' began as early as April 2020 during the Primary elections and the height of the first Covid wave. 

<br>

![https://github.com/twdooley/election_news/blob/master/images/fraudts.png](https://github.com/twdooley/election_news/blob/master/images/fraudts.png)
<br>
I intend to blog about these findings, especially the mail fraud issue. It is critical to the discourse of the current process and the security of democracy to understand the motives of thsoe who cry fraud. 
It is clear to me that negatively sentimented articles dating before the current discourse indicate the proximate advisors to the President encouraging such a narrative. 

## BreitBot

As mentioned and linked above, BreitBot is a finetuned GPT-2 model trained on almost 16,000 headlines from Breitbart.com. I invite the user to experiment with the link above. 
Many generated headlines are within the realm of realistic, especially for Breitbart. Many are comical. Many also indicate a deeper editorial perspective in the 'clickbaity' nature of the right/far-right. 




