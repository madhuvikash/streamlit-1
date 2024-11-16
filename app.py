import streamlit as st

st.title("USER GUESSING")
("==================================================================================")

st.header("Welcome to the 'GUESSING GAME' by the User ")
st.write("-------------------------------------------")

import random

st.subheader("RULES : ")
st.write("➼    Guess a number in the range of 1 to 100 (both inclusive).")
st.write("""➼    The computer will generate a random answer in the above
          mentioned range.""")
st.write("➼    The user will guess the number one at a time.")
st.write("""➼    If the guess matches the answer generated by the computer,
         then the player has won !""")
st.write("""➼    If the guess doesn't match the answer, a further chance
          will be provided to make another guess. It continues until
         user guesses the correct anwer. """)
st.write("-------------------------------------------")


if "answer" not in st.session_state:
    st.session_state.lowest_number = 1
    st.session_state.highest_number = 100
    st.session_state.answer = random.randint(st.session_state.lowest_number, st.session_state.highest_number)
    st.session_state.guesses = 0
    

st.title("PLAY")
st.write("-------------------------------------------")

user_guess = st.text_input(f"Enter a number between {st.session_state.lowest_number} and {st.session_state.highest_number} : ")
st.write("-------------------------------------------")

if user_guess.isdigit():

    user_guess = int(user_guess)
    st.session_state.guesses += 1

    if user_guess == st.session_state.answer:
        st.write("CORRECT GUESS !!")
        st.write(f"You took {st.session_state.guesses} guesses !")

        if st.session_state.guesses > 0 and st.session_state.guesses <= 7:
            st.write("VICTORY")
            st.success("You've won !")
            st.snow()
        else:
            st.write("Try to guess it within 7 attempts !")
            st.balloons()

    # elif user_guess <= 0 or user_guess > 100:
    #     st.session_state.lowest_number = st.session_state.lowest_number
    #     st.session_state.highest_number = st.session_state.highest_number
    #     st.write("OUT OF RANGE")
    #     st.write(f"Please enter a number between {st.session_state.lowest_number} and {st.session_state.highest_number} both inclusive.")
    #     st.button("NEXT GUESS")
    
    elif user_guess > st.session_state.answer:
        st.write("HIGH ! Go Lower.")
        st.session_state.highest_number = user_guess
        st.write(f"Select a number between {st.session_state.lowest_number} and {st.session_state.highest_number} both inclusive.")
        st.button("NEXT GUESS ⏭️")

    elif user_guess < st.session_state.answer:
        st.write("LOW ! Go Higher.")
        st.session_state.lowest_number = user_guess
        st.write(f"Select a number between {st.session_state.lowest_number} and {st.session_state.highest_number} both inclusive.")
        st.button("NEXT GUESS ⏭️")

    else:
        pass

else:
    if user_guess:
        st.write("INVALID GUESS !")
        st.button("NEXT GUESS")

if st.button("RESTART GAME 🔁"):
    st.session_state.clear()
    st.write("'Click 2 times to Restart the game. 🔁'")
else:
    pass

st.write("==================================================================================")
