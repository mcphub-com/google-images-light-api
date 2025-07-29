# Aigeon AI Google Images Light API

## Project Description

The Aigeon AI Google Images Light API is a Python-based server application designed to facilitate advanced image searches using Google's Image Search capabilities. This API leverages the SerpAPI to perform detailed and customizable image searches, providing users with a wide array of search parameters to refine their queries and obtain precise results.

## Features Overview

- **Advanced Image Search**: Perform detailed image searches with a variety of customizable parameters.
- **Location-Based Searches**: Simulate searches from specific geographic locations.
- **Time-Sensitive Queries**: Filter image results based on specific time frames.
- **Image Attributes**: Search for images based on size, color, type, and aspect ratio.
- **Licensing and Safety Filters**: Customize searches to include specific licenses and safe search settings.
- **Pagination and Device Simulation**: Control result pagination and simulate searches from different device types.

## Main Features and Functionality

The Aigeon AI Google Images Light API provides a comprehensive set of features for conducting advanced image searches:

1. **Query Customization**: Users can specify search queries using various parameters similar to those available in a standard Google Images search, including domain and language settings.
2. **Location and Language Settings**: Customize the search origin by specifying location and language codes, simulating searches from different regions and in different languages.
3. **Time-Based Filtering**: Limit searches to specific time periods using start and end dates or relative time units (e.g., days, weeks, months).
4. **Image Attribute Filters**: Refine search results based on image size, color, type, and aspect ratio.
5. **Licensing Options**: Filter images based on licensing requirements, ensuring compliance with usage rights.
6. **Safe Search and Result Filtering**: Enable or disable safe search filters and control the inclusion of similar or omitted results.
7. **Pagination and Device Emulation**: Manage result pagination and simulate searches from desktop, tablet, or mobile devices.

## Main Functions Description

### `search_images_light`

The primary function of the API, `search_images_light`, allows users to perform advanced image searches with a wide range of parameters:

- **q**: (str) The query string for the image search.
- **location**: (str, optional) The geographic location from which to simulate the search.
- **uule**: (str, optional) Google encoded location for the search.
- **google_domain**: (str, optional) The Google domain to use for the search.
- **gl**: (str, optional) Country code for the search.
- **hl**: (str, optional) Language code for the search.
- **cr**: (str, optional) Limit search to specific countries.
- **period_unit**: (str, optional) Time period unit for recent images.
- **period_value**: (int, optional) Time period value to use with `period_unit`.
- **start_date**: (str, optional) Start date for time-limited searches.
- **end_date**: (str, optional) End date for time-limited searches.
- **tbs**: (str, optional) Advanced search parameters.
- **imgar**: (str, optional) Aspect ratio of images.
- **imgsz**: (str, optional) Size of images.
- **image_color**: (str, optional) Color of images.
- **image_type**: (str, optional) Type of images.
- **licenses**: (str, optional) Licensing scope of images.
- **safe**: (str, optional) Level of filtering for adult content.
- **nfpr**: (int, optional) Exclusion of results from auto-corrected queries.
- **filter**: (int, optional) Enable or disable filters for similar and omitted results.
- **start**: (int, optional) Result offset for pagination.
- **device**: (str, optional) Device type to simulate for the search.
- **no_cache**: (bool, optional) Force fetching of results without using cache.

This function is designed to provide users with a flexible and powerful tool for conducting image searches tailored to their specific needs.