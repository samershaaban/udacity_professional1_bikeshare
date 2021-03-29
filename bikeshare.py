import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*60, '\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True :
        cities = ['chicago', 'new york city', 'washington']
        city = str(input('choose the city please type Chicago or Washington or New york city.\n')).lower()
        if city in cities :
            break
        else:
            print("invalid input please choose from Chicago or New york city or Washington \n ")
    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = str(input('choose a month or all\n')).lower()
        if month in months:
            break
        else:
            print('invalid input please choose from january or fabruary or march or april or may or june or all\n')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        day = str(input('choose day or all\n')).lower()
        if day in days:
            break
        else:
            print('invalid input please choose from saturday or sunday or monday or tuesday or wednesday or thursday or friday or all\n')

    print('-'*40)

    return city, month, day


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
    #loading the data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    #converting the start time column into datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #adding columns for month, day, hour
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    #adding a filter for the month in the dataframe
    if month != 'all':
        df = df[df['Month'] == month.title()]
    #adding a filter for the month in the dataframe
    if day != 'all':
        df = df[df['Day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month is ', df['Month'].mode()[0], '\n')

    # display the most common day of week
    print('the most common day is ', df['Day'].mode()[0], '\n')

    # display the most common start hour
    print('the most common hour is ', df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most common start station is: ', df['Start Station'].mode()[0], '\n')

    # display most commonly used end station
    print('the most common end station is: ', df['End Station'].mode()[0], '\n')


    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    print('the most common trip is: ', df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('the total travel time is: ', df['Trip Duration'].sum(), '\n')

    # display mean travel time
    print('the mean travel time is: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print('the number of Subscribers is: ', df['User Type'].value_counts()[0], '\n')
    print('the number of Customers is: ', df['User Type'].value_counts()[1], '\n')
    print('-'*40)
    if 'Dependent' in df['User Type'].unique():
        print('the number of Dependent is: ', df['User Type'].value_counts()[2], '\n')
    # Display counts of gender
    if 'Gender' in df:
        print('the number of male is: ', df['Gender'].value_counts()[0], '\n')
        print('the number of female is: ', df['Gender'].value_counts()[1], '\n')
        print('-'*40)
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('the most recent year of birth is: ', int(df['Birth Year'].max()))
        print('the earliest year of birth is: ', int(df['Birth Year'].min()))
        print('the most common year of birth is: ', int(df['Birth Year'].mode()[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)



def rawdata(df):
    i = 1
    while True:
        add_data = str(input('\nfor vewing 5 rows of raw data enter yes.\n if you want to stop adding rawdata enter any other thing. \n'))
        if add_data.lower() == 'yes':
            print(df[i:i+5])
            i = i+5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        rawdata(df)

        restart = input('\nWould you like to restart? Enter yes \nor enter any other thing for ending the program.\n')
        if restart.lower() != 'yes':
            print('\nthank you and good bye....\n')
            break


if __name__ == "__main__":
	main()
