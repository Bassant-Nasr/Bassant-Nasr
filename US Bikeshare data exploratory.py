import time
import pandas as pd
import numpy as np

CITY_DATA = { 'C': 'chicago.csv',
              'N': 'new_york_city.csv',
              'W': 'washington.csv' }

months=["January","February","March","April","May","June","All"]
days=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("\n                                         Hello! Let\'s explore some US bikeshare data!\n")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city= input("Welcome there!, please enter the city to illustrate\nC to show (chicago)\nN to show (new york city)\nW to show (washington): ").upper()
    while city not in CITY_DATA.keys():
        print("\nPlease choose a valid city:\nC for (chicago)\nN for (new york city)\nor W for (washington)!")
        city=input("\nHello again!, please enter the city to illustrate: ").upper()
    
    
    month=input("\nGreat! time to pick a full month name, or All for no filter needed: ").title()
    if month != "All":
        while month not in months:
            print("\nOops! out of valid ones, please choose:\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\nor All")
            month=input("\nEnter the month again! : ").title()
    
    day= input("\nWell, Do you need specific day? (Yes, All): ").title()
    if day!="Yes" and day!="All":
        day=input("Are you sure that you chose the right option? please try again: ").title()

    if day=="Yes":
        day=input("Please specify the full day name: ").title()
        while day not in days:
            print("Ugh! this is not valid, please choose:\nSaturday\nSunday\nMonday\nTuesday\nWednesday\nThursday\nFriday")
            day=input("Try again here!: ").title()
    
    
    
    return city,month,day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month']= df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    if month != 'All':
        df = df[df ['Month'] == month]
    
    if day != 'All':
        df=df[df['Day'] == day]

    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # display the most common month
    
    common_month = df['Month'].mode()[0]
    print('The most common month throughout the year is:', common_month)

    
    # display the most common day of week
    
    popular_day = df['Day'].mode()[0]
    print('Here, the most popular day among week days:', popular_day)
    

    # display the most common start hour

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Hour'] = df['Start Time'].dt.hour
    visited_hour = df['Hour'].mode()[0]
    print('This is the most visited start hour:', visited_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    df['Start Station'] = pd.DataFrame(df['Start Station'])
    most_visited_station=df['Start Station'].mode()[0]
    print("Most visited start station is:", most_visited_station)
    
    # display most commonly used end station

    df['End Station'] = pd.DataFrame(df['End Station'])
    most_stop_station=df['End Station'].mode()[0]
    print("Most visited stop station is:", most_stop_station)

    # display most frequent combination of start station and end station trip
    
    df['Trip'] = df['Start Station'] + ", and " + df['End Station']
    most_frequent_point= df['Trip'].mode()[0]
    print("Most frequent stations points are:", most_frequent_point)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    df['Duration In Hours']=df['Trip Duration']/60
    total_time=df['Duration In Hours'].sum()
    print("Total trip hours of this city are: {} hours".format(total_time))
    print("Time in days= ", (total_time/24))


    # display mean travel time

    time_mean=df['Duration In Hours'].mean()
    print("\nThe mean of travel time in choosen city is: {} hours ".format(time_mean))
    print("Time in days= ",(time_mean/24))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # Display counts of user types

    user_types=df['User Type'].value_counts().to_frame()
    print("Counts of all user types in the city are:\n ", user_types)


    # Display counts of gender
    
    try:
        counts_of_gender=df['Gender'].value_counts().to_frame()
        print("\nAnalyzing the category of gender is shown as: \n {} ".format(counts_of_gender))
    except:
        print("\nUnfortunately, gender not available in Washington records")

    # Display earliest, most recent, and most common year of birth

    try:
        earliest_YOB=df['Birth Year'].min()
        print("\nThe earliest year of birth is: ", earliest_YOB)
        print("Current age would be",(2021-earliest_YOB))

        recent_YOB=df['Birth Year'].max()
        print("\nThe most recent year of birth is: {} ".format(recent_YOB))
        print("Current age would be ",(2021-recent_YOB))

        frequent_YOB=df['Birth Year'].mode()[0]
        print("\nThe frequent year of birth in this city is: {} ".format(frequent_YOB))
        print("Current age would be ", (2021-frequent_YOB))

    except:
        print("\nSorry! the year of birth not existing in Washington records")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def overall_illustration(df):

    '''We create a scratch point for the index location to launch the data starting with it'''
    scratch_point=0
    analysis=input('Let\'s have an overall look. shall we?, (Yes, No): ').title()
    
    while analysis=="Yes":
        
        ''' Once user wishes to go through some rows,
        he will have a bonus overall description about those data records'''
    
        print("First, there are some statistics about our records to share!")
        print(df.describe())

        '''Then he will have the absolute freedom to choose the count of rows he would like to look at, not only 5 rows'''
    
        x=int(input('\nWell, how many rows you wish to go through?: '))

        '''Once the first number of data shown to him,
        he will be asked if he desires another tound with different count this time or not'''

        print(df.iloc[scratch_point:(scratch_point+x)])
        scratch_point+=x

        analysis=input("\nAre you willing to look at more rows this time?: (Yes, No): ").title()
    
        if analysis=="No":
            print("\nWe are delighted that you visited us!")
            break

        '''A thank you message will  immediately pop up once he would like no more illustrations.'''

        if analysis!= "No" and "Yes":
            print("\nYou might be mistaken the valid option, please restart the program and try again!")
            continue

    if analysis=="No":
        print("Thank you!")    

    
def main():
    while True:
        city,month,day= get_filters()
        df=load_data(city,month,day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        overall_illustration(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()