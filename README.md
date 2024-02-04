# GMB-Scraper

# Project Description

This is python script to scrape details of local business in different categories. The script extract address of differnet type of business using OpenStreetMap and Google Places Api. Output is extracted in google sheet.

# Note:

Initially, I attempted to utilize the Google Places API for the fetching business details. However, it became evident that the functionality we require is only available through a paid service, which is beyond the scope of the free tier.

As an alternative, I turned to the OpenStreetMap API. While it provided some functionality, it fell short in providing comprehensive details about businesses. Specifically, we were only able to retrieve basic address information.

Also tried to use Yelp API but this is not accessble in India
