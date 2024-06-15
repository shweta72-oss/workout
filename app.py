import streamlit as st

# Title of the app
st.title('Home Workout Planner')

# Input fields for the user
name = st.text_input('Enter your name')
days_per_week = st.number_input('Days per week', min_value=1, max_value=7, step=1)
workout_duration = st.number_input('Workout duration (minutes)', min_value=10, max_value=180, step=10)

# Dropdown for selecting workout type
workout_type = st.selectbox('Select workout type', ['Cardio', 'Strength', 'Flexibility', 'Mixed'])

# Button to generate the plan
if st.button('Generate Workout Plan'):
    # Display the user's input
    st.subheader(f"Workout Plan for {name}")
    st.write(f"Days per week: {days_per_week}")
    st.write(f"Workout duration: {workout_duration} minutes")
    st.write(f"Workout type: {workout_type}")
    
    # Sample workout plan
    workout_plan = {
        'Cardio': ['Running', 'Cycling', 'Jump Rope'],
        'Strength': ['Push-ups', 'Pull-ups', 'Squats'],
        'Flexibility': ['Yoga', 'Stretching', 'Pilates'],
        'Mixed': ['Burpees', 'Mountain Climbers', 'Plank']
    }
    
    selected_workouts = workout_plan[workout_type]
    
    st.subheader('Your Workouts:')
    for day in range(1, days_per_week + 1):
        st.write(f"Day {day}: {selected_workouts[day % len(selected_workouts)]}")

# Run the app with:
# streamlit run home_workout_planner.py