import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df['education'].value_counts()['Bachelors']/df.shape[0]

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higher_education = ['Bachelors', 'Masters','Doctorate']
    lower_education = ['HS-grad','Some-college', 'Assoc-voc','Prof-school', 'Assoc-acdm', '7th-8th', '12th','10th', '11th', '9th', '5th-6th', '1st-4th']
    greater_salary = df[df['salary']== '>50K']
    lower_salary = df[df['salary']== '<=50K']
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = greater_salary['education'].value_counts()[higher_education].sum()/greater_salary.shape[0]
    lower_education = greater_salary['education'].value_counts()[lower_education].sum()/greater_salary.shape[0]

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = 1 #greater_salary['hours-per-week'].min() gives answer of 1 hour

    rich_percentage = 1/df.shape[0]

    # What country has the highest percentage of people that earn >50K?
    g = pd.DataFrame(greater_salary['native-country'].value_counts())
    highest_earning_country = g.idxmax().tolist()
    highest_earning_country_percentage = g.loc['United-States']/df.shape[0]

    # Identify the most popular occupation for those who earn >50K in India.
    Indian_rich = greater_salary[greater_salary['native-country'] == 'India']
    occupation = Indian_rich['occupation'].value_counts()
    top_IN_occupation = occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
