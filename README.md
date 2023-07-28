## Metka Pinezic 
## Data Engineer, Business Intelligence Take Home Assignment  


The objective of this project is to build an ETL to design and deliver a data model that helps make an informed decision on which media streaming platform to subscribe to. The decision will be based on the quality and quantity of films each service provides, with price taken out of consideration.

The scope is to analyze and compare media streaming platforms (Netflix and Amazon Prime) based on the films they offer. The goal is to identify the 
platform with better film offerings, focusing on quality and variety.


### Process outline

#### Data Source Identification and Collection:

  To achieve the objective, three datasets were collected:

    - imdb_raw.csv  // dataset with film ratings
    - netflix_titles.csv  // Netflix dataset with a list of media available on Netflix
    - amazon_prine_titles.csv // Amazon Prime dataset with a list of media available on Amazon Prime

#### Data Exploration and Understanding:

  Upon loading the data into a data mart named 'raw,' initial checks were performed to identify any data quality issues and missing values. This step   helps gain an understanding of the data's structure and potential challenges.

#### Data Cleaning:

  The columns 'release_year' and 'gross' column required cleaning and transformation from string to an integer data type for consistency and better analysis.

#### Transformation:

  A new table in the 'clean' schema was created, combining the three datasets. The new table includes a column indicating whether a film or series is available on either or both platforms.

#### Data Model Design:

    - available in the repository under the name DM_diagram.jpeg

#### Data Loading:

  The initial datasets are loaded into the 'raw' schema. After applying the necessary transformations, the resultant dataset is stored in a new table within the 'clean' schema. This new table will serve as the basis for further analysis and reporting.

#### Data Validation and Quality Assurance:

  To ensure data integrity, a quality check was performed. The number of rows in the new dataset was verified against the number of rows in the raw IMDb file. The transformation process should not introduce any new rows or remove any existing rows from the raw IMDb data.

#### Final deliverable:

- Databricks library as a notebook in an HTML format which you can download and open in a browser.
- A pdf report summarizing the findings, outlining the problem, and providing insights into which media streaming platform is more suitable based on film offerings.
