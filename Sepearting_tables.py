import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrameCollection
from awsglue.dynamicframe import DynamicFrame

# Script generated for node Custom transform
def MyTransform(glueContext, dfc) -> DynamicFrameCollection:
    from pyspark.sql.functions import expr
    from pyspark.sql.functions import when
    from pyspark.sql.functions import lit
    from pyspark.sql.functions import col

    dk = dfc.select(list(dfc.keys())[0]).toDF()
    dk = dk.na.fill(0.0)
    newcust_df = DynamicFrame.fromDF(dk, glueContext, "newcust_df")
    return DynamicFrameCollection({"CustomTransform0": newcust_df}, glueContext)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data Catalog table
DataCatalogtable_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="covid-19-database",
    table_name="owid_covid_data_csv",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("id", "long", "id", "long"),
        ("iso_code", "string", "iso_code", "string"),
        ("continent", "string", "continent", "string"),
        ("location", "string", "location", "string"),
        ("date", "string", "date", "string"),
        ("total_cases", "long", "total_cases", "long"),
        ("new_cases", "long", "new_cases", "long"),
        ("new_cases_smoothed", "double", "new_cases_smoothed", "double"),
        ("total_deaths", "long", "total_deaths", "long"),
        ("new_deaths", "long", "new_deaths", "long"),
        ("new_deaths_smoothed", "double", "new_deaths_smoothed", "double"),
        ("total_cases_per_million", "double", "total_cases_per_million", "double"),
        ("new_cases_per_million", "double", "new_cases_per_million", "double"),
        (
            "new_cases_smoothed_per_million",
            "double",
            "new_cases_smoothed_per_million",
            "double",
        ),
        ("total_deaths_per_million", "double", "total_deaths_per_million", "double"),
        ("new_deaths_per_million", "double", "new_deaths_per_million", "double"),
        (
            "new_deaths_smoothed_per_million",
            "double",
            "new_deaths_smoothed_per_million",
            "double",
        ),
        ("reproduction_rate", "double", "reproduction_rate", "double"),
        ("icu_patients", "string", "icu_patients", "long"),
        ("icu_patients_per_million", "string", "icu_patients_per_million", "double"),
        ("hosp_patients", "string", "hosp_patients", "long"),
        ("hosp_patients_per_million", "string", "hosp_patients_per_million", "double"),
        ("weekly_icu_admissions", "string", "weekly_icu_admissions", "long"),
        (
            "weekly_icu_admissions_per_million",
            "string",
            "weekly_icu_admissions_per_million",
            "double",
        ),
        ("weekly_hosp_admissions", "string", "weekly_hosp_admissions", "long"),
        (
            "weekly_hosp_admissions_per_million",
            "string",
            "weekly_hosp_admissions_per_million",
            "double",
        ),
        ("new_tests", "string", "new_tests", "long"),
        ("total_tests", "string", "total_tests", "long"),
        ("total_tests_per_thousand", "string", "total_tests_per_thousand", "double"),
        ("new_tests_per_thousand", "string", "new_tests_per_thousand", "double"),
        ("new_tests_smoothed", "string", "new_tests_smoothed", "long"),
        (
            "new_tests_smoothed_per_thousand",
            "string",
            "new_tests_smoothed_per_thousand",
            "double",
        ),
        ("positive_rate", "string", "positive_rate", "double"),
        ("tests_per_case", "string", "tests_per_case", "double"),
        ("tests_units", "string", "tests_units", "string"),
        ("total_vaccinations", "long", "total_vaccinations", "long"),
        ("people_vaccinated", "long", "people_vaccinated", "long"),
        ("people_fully_vaccinated", "long", "people_fully_vaccinated", "long"),
        ("total_boosters", "string", "total_boosters", "long"),
        ("new_vaccinations", "long", "new_vaccinations", "long"),
        ("new_vaccinations_smoothed", "long", "new_vaccinations_smoothed", "long"),
        (
            "total_vaccinations_per_hundred",
            "double",
            "total_vaccinations_per_hundred",
            "double",
        ),
        (
            "people_vaccinated_per_hundred",
            "double",
            "people_vaccinated_per_hundred",
            "double",
        ),
        (
            "people_fully_vaccinated_per_hundred",
            "double",
            "people_fully_vaccinated_per_hundred",
            "double",
        ),
        (
            "total_boosters_per_hundred",
            "string",
            "total_boosters_per_hundred",
            "double",
        ),
        (
            "new_vaccinations_smoothed_per_million",
            "long",
            "new_vaccinations_smoothed_per_million",
            "double",
        ),
        (
            "new_people_vaccinated_smoothed",
            "long",
            "new_people_vaccinated_smoothed",
            "long",
        ),
        (
            "new_people_vaccinated_smoothed_per_hundred",
            "double",
            "new_people_vaccinated_smoothed_per_hundred",
            "double",
        ),
        ("stringency_index", "double", "stringency_index", "double"),
        ("population", "long", "population", "long"),
        ("population_density", "double", "population_density", "double"),
        ("median_age", "double", "median_age", "double"),
        ("aged_65_older", "double", "aged_65_older", "double"),
        ("aged_70_older", "double", "aged_70_older", "double"),
        ("gdp_per_capita", "double", "gdp_per_capita", "double"),
        ("extreme_poverty", "string", "extreme_poverty", "double"),
        ("cardiovasc_death_rate", "double", "cardiovasc_death_rate", "double"),
        ("diabetes_prevalence", "double", "diabetes_prevalence", "double"),
        ("female_smokers", "string", "female_smokers", "double"),
        ("male_smokers", "string", "male_smokers", "double"),
        ("handwashing_facilities", "double", "handwashing_facilities", "double"),
        (
            "hospital_beds_per_thousand",
            "double",
            "hospital_beds_per_thousand",
            "double",
        ),
        ("life_expectancy", "double", "life_expectancy", "double"),
        ("human_development_index", "double", "human_development_index", "double"),
        (
            "excess_mortality_cumulative_absolute",
            "string",
            "excess_mortality_cumulative_absolute",
            "double",
        ),
        (
            "excess_mortality_cumulative",
            "string",
            "excess_mortality_cumulative",
            "double",
        ),
        ("excess_mortality", "string", "excess_mortality", "double"),
        (
            "excess_mortality_cumulative_per_million",
            "string",
            "excess_mortality_cumulative_per_million",
            "double",
        ),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node Custom transform
Customtransform_node1638578721076 = MyTransform(
    glueContext,
    DynamicFrameCollection({"ApplyMapping_node2": ApplyMapping_node2}, glueContext),
)

# Script generated for node Select From Collection
SelectFromCollection_node1638578812316 = SelectFromCollection.apply(
    dfc=Customtransform_node1638578721076,
    key=list(Customtransform_node1638578721076.keys())[0],
    transformation_ctx="SelectFromCollection_node1638578812316",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=SelectFromCollection_node1638578812316,
    connection_type="s3",
    format="csv",
    connection_options={"path": "s3://covid-19-outputt/", "partitionKeys": []},
    transformation_ctx="S3bucket_node3",
)

job.commit()
