# Single City - Heroku

-A self-made emergency backup for citrics.io

A flask app run on heroku that was meant to be used as a temporary backend for citrics.io.

Routes:

/{ACCESS_KEY}/singlecityWiki/(id)
  
  returns wikipedia information on a city
  
/{ACCESS_KEY}/wikisum/(id)
  
  returns the wikipedia summary on a city
  
/{ACCESS_KEY}/singlecityYelp/(id)
  
  returns the Yelp data for a city
  
/{ACCESS_KEY}/statecrime/(sa) (state abbreviation)
  
  returns state and national crime data
