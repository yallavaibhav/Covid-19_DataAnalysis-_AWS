# Covid-19_DataAnalysis-_AWS
Using AWS services, we will be analyzing the Big data.

 	
1	Abstract:
Since the first Covid-19 case was reported in November 2019, the world has been experiencing this deadly disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) that attacks the human respiratory system. This deadly disease, Covid-19 (Coronavirus), had killed 4.5M people (about twice the population of New Mexico), and there are still 219M cases present across the world that are infected. Collecting and examining a large amount of Covid-19 data is challenging, and processing and visualizing it statistically needs more processing power. We believe that through an open and collaborative effort that combines data, science, and technology, we can inspire insights and foster breakthroughs necessary to limit COVID-19 cases by finding the trends. In this project, we will use datasets like “COVID-19 Data Lake”, “COVID-19 Foot Traffic Data”, and Kaggle datasets which are used to collate daily COVID-19 cases, deaths, and various other trends. Some supplement datasets are also added to improve the accuracy of our projections. Using this tremendous amount of data and AWS Services, we analyze how this global pandemic has affected human lives worldwide and analyze the vaccination policies of different nations to examine the best feasible way to help mitigate fatality rates. It also discusses how some policies (social distancing, face mask coverings, stay-at-home restrictions) prevent Covid-19 cases. This project will help understand and capture the trends to make people assess the situation quantitatively and take necessary preventive actions. This project can be used by researchers, biomedical engineering, government, and NGOs to make people aware and provide the right support (vaccine, hygiene protocols) and common people to understand the data in a simpler format.

2	Introduction:
2.1	Project goals and objectives
The project goal is to analyze the huge trending covid-19 dataset. Our objective is to understand the patterns of the covid cases, and how other attributes like vaccinations, lockdowns, and handwashing help reduce the number of deaths and cases. Using tools, we have created a pipeline that will help clean the data and analyze it.

2.2	Problem and motivation
Covid-19 pandemic had shaken the entire world. Many lost their loved ones, their jobs, career, businesses, and many more. This had an unbelievably harmful impact on our society. There were more than 270 million people who were affected by covid and more than 5.7 million who died due to covid. There were many vaccines supplied, new policies were added like lockdown, handwashing, and social distancing just to reduce the risk of getting affected by Covid-19. 
The problem is if the above policies and vaccines are even helping reduce the total number of covid cases in the entire world. To understand the pattern, we have analyzed the huge data from the year 2020 February till December 2021. With this data, we can find out some patterns which might help reduce covid.
This information should be present to the entire world, for that we can use some visualization tools which will help users easily understand complex data. So, making this information public will help citizens, researchers, Doctors, students, and Government be cautious about their health and the future.
 
2.3	Project application and impact 
This project analysis can help people understand the rise and fall of covid cases, deaths, vaccines supplies, fully vaccinated people, and many more all over the help. Users all over the world can see the analysis and be cautious about the situation. This will not only help common people, but also the government, doctors, and researchers to advance their techniques

2.4	Project results and deliverables
In our project, we applied knowledge about big data analytic tools on AWS to process and store a huge amount of Covid data worldwide.
We perform analytical queries on AWS and visualization processes on Tableau on to give a whole picture about covid19 in the world in terms of the total cases, deaths, hospitalization country by country, continent by continent, daily, monthly, the numbers of people vaccinated and gain insights how policies and regulations have a significant impact on slowing the spread of this virus.

3	Literature Survey:
Many scientific articles have been conducted based on statistical data on the number of people infected with Covid in different countries to help scientists and epidemiologists build predictive models to help scientists capture the nature of the virus the direction and extent of infection in the community. This helps the government and legislators to make appropriate regulations to reduce the possibility of disease spread in each region as well as to support the right resources. Tosi D (2020) analyzed data collected globally to build models which can predict the waves of infection and when the pandemic is under control in Italia. They also emphasized the effectiveness of big data and data analytics in collecting and analyzing data so that scientists can build models that predict the development of Covid 19. Alsunaidi (2021) presented the importance of big data analytics in processing and studying the huge volume of covid 19 so that scientists can gain insights that contribute to defeating this pandemic. Farhadi (2021) concluded that accurate data sets will be effective tools for scientists and governments to evaluate the effectiveness of methods and policies to reduce the spread of this disease.
It has been two years since the first case was confirmed, the world is still learning and discovering the possibilities of evolutionary of the disease caused by Covid 19. Tools and applications for data collection, storage, and analysis always make a significant contribution in the battle to control the pandemic.

4	Data Description:
4.1	Data Source:
The data is collected and updated by Amazon Open Repository. The team has been collecting data from many sources such as John Hopkins University, European Centre for Disease Prevention and Control (ECDC), and some other countries like the United Kingdom, United States, Canada. The parameters in the data include the number of confirmed cases, deaths, hospitalizations, and testing, as well as other related information such as the degree of policies are imposed on different regions, countries, GDP, or population which are helpful for the analysis process.

4.2	Data Modeling:
Data modeling was a challenging part for us. As we took data from multiple sources, we had to design a model as per our requirements. Our main dataset contained 67 columns and around 200,000 records. So, from this collective dataset, we had to partition it into smaller related entities.
![image](https://user-images.githubusercontent.com/39133612/147705506-2a2b91c2-86a3-48c7-81cf-8166ccc1b433.png)


 We partitioned the dataset into 11 different tables and created primary key foreign keys to connect them. We created tables like Vaccinations, which contained all the information about the vaccination status for all the countries. For the table confirmed cases we put all the columns containing data about the cases in all the countries. Similarly, we created a total of 11 tables which were connected by using foreign keys

5	Design and Implementation:
5.1	Overview:
We have performed ETL operations using AWS. The services include S3 bucket, Glue, Athena, and Redshift. There was also a third-party integration, which is Tableau for visualization.
We have started importing Covid-19 data from the AWS open-data registry to the S3 bucket. S3 buckets are good for storing data, as they are scalable with superior performance and security. After importing, this data is sent to the Data Catalog using AWS crawlers. Crawlers are used to crawl the data and store the metadata in the database as a tabular form in Data Catalog. 

![image](https://user-images.githubusercontent.com/39133612/147706042-7598bdf3-ddad-41da-b14e-dbd8ddefa451.png)


We have created a custom Glue code to fill the NULL values to zero and another job that will help to divide the main table into smaller dimensions. Each dimension has its unique attributes. Once it is divided, we can check the data using SQL queries in ATHENA. All the files are sent to Redshift for analytical queries. 
Integration with redshift was done for visualizing the data. Visualization of the data will help in understanding this complex data more easily.

5.2	S3 Buckets:
We need to store this data in simple storage in AWS, and one of the best options we have is AWS S3. The data we have contains covid-data from all countries all over the world. To access this data in AWS, we first need to store this data in the S3 bucket. We have created two buckets, one for the input and another for the Gl7ue job output files. 
![image](https://user-images.githubusercontent.com/39133612/147706066-85b4e416-987c-40c9-a898-650da038a03e.png)

5.3	AWS Glue Crawler:
Before using crawlers, we need to create a database in the Data Catalog. This will help to store the tables which were created by the crawler in the database.
![image](https://user-images.githubusercontent.com/39133612/147706089-8f9bee63-99cd-4380-b914-1c3c19fc4a83.png)

After creating the database, we have created a crawler with Run on-demand specifications. The source was from the S3 input bucket, and the output will be stored in a table in the database.
Once we run the crawler, the crawler will create a table that will be stored in the Database. We can run it hourly or daily if our data is streaming. The crawler will help recognize your data store, which in turn is used to create a schema for the table.

