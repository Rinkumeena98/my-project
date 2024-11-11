import streamlit as st

# Initialize session state for tracking game state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9  # 3x3 board
    st.session_state.current_player = "X"  # Player X starts
    st.session_state.winner = None  # No winner at the start

# Function to check if someone has won
def check_winner():
    # Winning combinations: 3 horizontal, 3 vertical, 2 diagonal
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]  # diagonal
    ]
    
    for combo in win_combos:
        if st.session_state.board[combo[0]] == st.session_state.board[combo[1]] == st.session_state.board[combo[2]] != "":
            return st.session_state.board[combo[0]]
    return None

# Function to handle button click
def button_click(index):
    if st.session_state.board[index] == "" and not st.session_state.winner:
        st.session_state.board[index] = st.session_state.current_player
        winner = check_winner()
        if winner:
            st.session_state.winner = winner
            st.success(f"Player {winner} wins!")
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Layout for the game
st.title("Tic-Tac-Toe")

# Show the current board
for i in range(9):
    col = i % 3
    row = i // 3
    button_text = st.session_state.board[i] if st.session_state.board[i] != "" else " "
    button = st.button(button_text, key=f"button_{i}", on_click=button_click, args=(i,))

# Display the current player
st.write(f"Player {st.session_state.current_player}'s turn")

# Reset the game button
if st.button("Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None