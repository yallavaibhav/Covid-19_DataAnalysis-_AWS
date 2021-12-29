--copy test(id,total_deaths,new_deaths,new_deaths_smoothed,total_deaths_per_million,new_deaths_per_million,new_deaths_smoothed_per_million)
--from 's3://covid-19-outputt/run-S3bucket_node3-3-part-r-00000'
--iam_role 'arn:aws:iam::999940996360:role/service-role/AmazonRedshift-CommandsAccessRole-20211205T165109'
--csv
--IGNOREHEADER 1;
--
--select * from test;
--
--CREATE TABLE test
--(
--  id     INTEGER ,
--  total_deaths        INTEGER ,
--  new_deaths        INTEGER ,
--  new_deaths_smoothed    real,
--  total_deaths_per_million   real ,
--  new_deaths_per_million       real ,
--  new_deaths_smoothed_per_million        real
--);

--
--
--CREATE TABLE coviddata (
--id BIGINT,
--iso_code CHAR,
--continent CHAR,
--location CHAR,
--date DATE,
--total_cases BIGINT,
--new_cases BIGINT,
--new_cases_smoothed REAL,
--total_deaths BIGINT,
--new_deaths BIGINT,
--new_deaths_smoothed REAL,
--total_cases_per_million REAL,
--new_cases_per_million REAL,
--new_cases_smoothed_per_million REAL,
--total_deaths_per_million REAL,
--new_deaths_per_million REAL,
--new_deaths_smoothed_per_million REAL,
--reproduction_rate REAL,
--icu_patients BIGINT,
--icu_patients_per_million REAL,
--hosp_patients BIGINT,
--hosp_patients_per_million REAL,
--weekly_icu_admissions BIGINT,
--weekly_icu_admissions_per_million REAL,
--weekly_hosp_admissions BIGINT,
--weekly_hosp_admissions_per_million REAL,
--new_tests BIGINT,
--total_tests BIGINT,
--total_tests_per_thousand REAL,
--new_tests_per_thousand REAL,
--new_tests_smoothed BIGINT,
--new_tests_smoothed_per_thousand REAL,
--positive_rate REAL,
--tests_per_case REAL,
--tests_units CHAR,
--total_vaccinations BIGINT,
--people_vaccinated BIGINT,
--people_fully_vaccinated BIGINT,
--total_boosters BIGINT,
--new_vaccinations BIGINT,
--new_vaccinations_smoothed BIGINT,
--total_vaccinations_per_hundred REAL,
--people_vaccinated_per_hundred REAL,
--people_fully_vaccinated_per_hundred REAL,
--total_boosters_per_hundred REAL,
--new_vaccinations_smoothed_per_million REAL,
--new_people_vaccinated_smoothed BIGINT,
--new_people_vaccinated_smoothed_per_hundred REAL,
--stringency_index REAL,
--population BIGINT,
--population_density REAL,
--median_age REAL,
--aged_65_older REAL,
--aged_70_older REAL,
--gdp_per_capita REAL,
--extreme_poverty REAL,
--cardiovasc_death_rate REAL,
--diabetes_prevalence REAL,
--female_smokers REAL,
--male_smokers REAL,
--handwashing_facilities REAL,
--hospital_beds_per_thousand REAL,
--life_expectancy REAL,
--human_development_index REAL,
--excess_mortality_cumulative_absolute REAL,
--excess_mortality_cumulative REAL,
--excess_mortality REAL,
--excess_mortality_cumulative_per_million REAL
--);
--
--
--copy coviddata1(id,iso_code,continent,location,date,total_cases,new_cases,new_cases_smoothed,total_deaths,new_deaths,new_deaths_smoothed,total_cases_per_million,new_cases_per_million,new_cases_smoothed_per_million,total_deaths_per_million,new_deaths_per_million,new_deaths_smoothed_per_million,reproduction_rate,icu_patients,icu_patients_per_million,hosp_patients,hosp_patients_per_million,weekly_icu_admissions,weekly_icu_admissions_per_million,weekly_hosp_admissions,weekly_hosp_admissions_per_million,new_tests,total_tests,total_tests_per_thousand,new_tests_per_thousand,new_tests_smoothed,new_tests_smoothed_per_thousand,positive_rate,tests_per_case,tests_units,total_vaccinations,people_vaccinated,people_fully_vaccinated,total_boosters,new_vaccinations,new_vaccinations_smoothed,total_vaccinations_per_hundred,people_vaccinated_per_hundred,people_fully_vaccinated_per_hundred,total_boosters_per_hundred,new_vaccinations_smoothed_per_million,new_people_vaccinated_smoothed,new_people_vaccinated_smoothed_per_hundred,stringency_index,population,population_density,median_age,aged_65_older,aged_70_older,gdp_per_capita,extreme_poverty,cardiovasc_death_rate,diabetes_prevalence,female_smokers,male_smokers,handwashing_facilities,hospital_beds_per_thousand,life_expectancy,human_development_index,excess_mortality_cumulative_absolute,excess_mortality_cumulative,excess_mortality,excess_mortality_cumulative_per_million
--)
--from 's3://covid-19-outputt/run-S3bucket_node3-3-part-r-00000'
--iam_role 'arn:aws:iam::999940996360:role/service-role/AmazonRedshift-CommandsAccessRole-20211205T165109'
--csv
--IGNOREHEADER 2 DATEFORMAT 'MM/DD/YYYY';

--
--
--

--CREATE TABLE coviddata1 (
--id BIGINT,
--iso_code CHAR(250),
--continent CHAR(250),
--location CHAR(250),
--date DATE,
--total_cases BIGINT,
--new_cases BIGINT,
--new_cases_smoothed REAL,
--total_deaths BIGINT,
--new_deaths BIGINT,
--new_deaths_smoothed REAL,
--total_cases_per_million REAL,
--new_cases_per_million REAL,
--new_cases_smoothed_per_million REAL,
--total_deaths_per_million REAL,
--new_deaths_per_million REAL,
--new_deaths_smoothed_per_million REAL,
--reproduction_rate REAL,
--icu_patients BIGINT,
--icu_patients_per_million REAL,
--hosp_patients BIGINT,
--hosp_patients_per_million REAL,
--weekly_icu_admissions BIGINT,
--weekly_icu_admissions_per_million REAL,
--weekly_hosp_admissions BIGINT,
--weekly_hosp_admissions_per_million REAL,
--new_tests BIGINT,
--total_tests BIGINT,
--total_tests_per_thousand REAL,
--new_tests_per_thousand REAL,
--new_tests_smoothed BIGINT,
--new_tests_smoothed_per_thousand REAL,
--positive_rate REAL,
--tests_per_case REAL,
--tests_units CHAR(250),
--total_vaccinations BIGINT,
--people_vaccinated BIGINT,
--people_fully_vaccinated BIGINT,
--total_boosters BIGINT,
--new_vaccinations BIGINT,
--new_vaccinations_smoothed BIGINT,
--total_vaccinations_per_hundred REAL,
--people_vaccinated_per_hundred REAL,
--people_fully_vaccinated_per_hundred REAL,
--total_boosters_per_hundred REAL,
--new_vaccinations_smoothed_per_million REAL,
--new_people_vaccinated_smoothed BIGINT,
--new_people_vaccinated_smoothed_per_hundred REAL,
--stringency_index REAL,
--population BIGINT,
--population_density REAL,
--median_age REAL,
--aged_65_older REAL,
--aged_70_older REAL,
--gdp_per_capita REAL,
--extreme_poverty REAL,
--cardiovasc_death_rate REAL,
--diabetes_prevalence REAL,
--female_smokers REAL,
--male_smokers REAL,
--handwashing_facilities REAL,
--hospital_beds_per_thousand REAL,
--life_expectancy REAL,
--human_development_index REAL,
--excess_mortality_cumulative_absolute REAL,
--excess_mortality_cumulative REAL,
--excess_mortality REAL,
--excess_mortality_cumulative_per_million REAL
--);


select * from coviddata1 limit 10;