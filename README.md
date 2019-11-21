# Client Project: Identifying Major Electrical Disturbances in the U.S. Using Social Media Posts

***Author: [Creighton Ashton](https://www.linkedin.com/in/creightonashton/), [Meroe Yadollahi](https://www.linkedin.com/in/meroe-yadollahi/), [Jack Wang](https://www.linkedin.com/in/jackweijiawang/)***

---

## Problem Statement

The traditional method to spot a power outage/electrical disturbance is to check the live feeds provided by major utility companies or the satellite data that capture the extent of light emitted at night. We will build a tool that identifies the major electrical disturbances using social media posts. Unlike the traditional methods, our tool will identify major electrical disturbances more timely.

---

## Executive Summary

The goal of this project is to develop a tool that will scan Twitter for certain posts containing power outage keywords and build a classification model in order to predict which areas are most likely to be suffering from a power outage. The power outage data will be collected on [the U.S. Department of Energy website](https://www.oe.netl.doe.gov/OE417_annual_summary.aspx), the weather data will be collected on [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov/data-access/severe-weather), and we will scrape historical Twitter posts on [Twitter](https://twitter.com) for our Twitter data. We will build different types of classification models and select the best model based on the recall score, F1 score, and accuracy score of the models.

---

## Software Requirements

Codes are written in Jupyter Notebook with Python. Users are recommended to know Python library `Numpy`, `Pandas`, classification models with `Scikit-learn`, visualization with `matplotlib`, and the knowledge of supervised machine learning.

---

## Content with Jupyter Notebooks

Users should follow the below order to read through our works, all notebooks have descriptions and comments for the codes:

### 1. Data Collection

As mentioned in executive summary, we collected our data on [the U.S. Department of Energy website](https://www.oe.netl.doe.gov/OE417_annual_summary.aspx), [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov/data-access/severe-weather), and we scraped posts on [Twitter](https://twitter.com) by using Twitter scraper. We mainly focus on power outage data and the Twitter data because our model is built on these two data. The weather data we collected is for EDA purpose. The intuition is from our findings in power outage data. 

**Below are the Jupyter Notebooks for Data Collection:**
- [Twitter Scraper](./Code/Twitter_Scraper.ipynb)
- [Power Outage Data](./Code/power-outage-data.ipynb)
- [Weather Data](./Code/Weather_Data.ipynb)

### 2. Data Cleaning & Merging

We did the data cleaning by dropping missing values, checking data types, and dropping the columns/features we don't need. For Twitter data, we removed hyperlinks and words not making sense. For the data merging, we did an inner merge by the common date and location of power outage data and Twitter data. The final data we used to build our models is exported from `Combining_Data` notebook.

**Below are the Jupyter Notebooks for Data Cleaning & Merging:**
- [Cleaned Twitter Data](./Code/twitter_cleaning.ipynb)
- [Combining Data (power outage and twitter)](./Code/Combining_Data.ipynb)

### 3. EDA

We did the exploratory data analysis (EDA) on power outage data, weather data, and also the Twitter data. The intuition of collecting weather data is that we found out the power outage events are mostly caused by severe weathers. So we collected weather data and did an EDA on it, details can be found in the weather EDA notebook. For Twitter data, we tried to understand the relationship of the keywords related to power outage events by applying Word2Vec transformer, and created a word cloud for visualization.

**Below are the Jupyter Notebook for EDA:**
- [Twitter EDA](./Code/Twitter_EDA.ipynb)
- [Weather & Power Outage EDA](./Code/Weather_PowerOutage_EDA.ipynb)
- [Word2Vec](./Code/Word2Vec.ipynb)


### 4. Modeling & Pickle

Our models are built on `twitter_target.csv`, our goal is to find the model that optimizes the F1 score and recall score. We have built Random Forest Classifier, Logistic Regression Model, and Bagging Classifier. The obstacle we had was the unbalanced classes of our data, which we chose to balance two classes by decreasing the majority class. The final model is a bagging classifier built on decreased dataset. We have imported our final model to a pickle file, as shown in the`Pickle` notebook.

**Below are the Jupyter Notebook for Modeling & Pickle:**
- [Modeling](./Code/Modeling.ipynb)
- [Pickle](./Code/Pickle.ipynb)

### 5. Final Product

The final product is an interactive App that asks users to select a state, and shows users the probabilities of the state suffering from a major electrical disturbance as of the current time. Please click [here](https://youtu.be/gP7jnR8r_M0) for the demonstration. 

**Below is the Python code file of Final Product:**
- [Final Product](./Files/final-product.py)
- [Demonstration Video](https://youtu.be/gP7jnR8r_M0)

---

## Conclusion

We selected our final model with the highest F1 score and recall score because optimizing these two matrices can minimize false negative events. Our final classification model is not performing pretty well since it only has 64.36% F1 score and 63.13% recall score. However, it is understandable because we are limited by the number of data we have so we could not train our model effectively. The power outage data we have does not line up well with our Twitter data because most of the posts on Twitter are about local power outages, where our power outage data are major electrical power outages. We could not find useful local power outage historical data because most utility companies tend to not give out historical power outage data, they only provide live feeds of power outage events. As a consequence, our model is more conservative when it is predicting the electrical disturbances, which means it usually classifies small/local power outage events as 0 (false; not a power outage).

To improve our model, we definitely need more power outage data and also more detail of it. Most of our power outage data only have location that is state-level, which gave us a hard time matching the Twitter posts to the power outage events because users on Twitter usually use cities as their location. Another thing we can work on is the keyword selection. We included "blackout" as one of the keywords we scrape from Twitter, which ends up giving us a lot of noises. For example, we have people who are drunk and "blackout".

In summary, the main obstacle is the data collecting. If we had the ideal power outage data and budget (which we found can be purchased from [some websites](https://poweroutage.us/products), we could have built a model with higher recall and F1 score. 

---

## Sources

- [the U.S. Department of Energy](https://www.oe.netl.doe.gov/OE417_annual_summary.aspx)
- [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov/data-access/severe-weather)
- [Using word2vec to Analyze News Headlines and Predict Article Success](https://towardsdatascience.com/using-word2vec-to-analyze-news-headlines-and-predict-article-success-cdeda5f14751)
- [7 Techniques to Handle Imbalanced Data](https://www.kdnuggets.com/2017/06/7-techniques-handle-imbalanced-data.html)
- [twitterscraper](https://github.com/taspinar/twitterscraper)