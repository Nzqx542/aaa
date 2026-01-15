import streamlit as st

st.title("Theme selection - color basics")


# Временно решение
if "colors" not in st.session_state:
    st.session_state.colors = {
        "Number": 0,
        "Red": 0,
        "Green": 0,
        "Blue": 0,
    }


if "first" not in st.session_state:
    st.session_state.first = {
        "Number": 0,
        "Initial": 0,
        "Final": 0,
        "Size": 0,
    }


st.subheader("Select common seed")

option = st.selectbox("Select seed", list(st.session_state.colors.keys()))
option = st.selectbox("Select seed", list(st.session_state.first.keys()))


if st.button("Accept seeds"):
    st.session_state.colors["Blue"] += 1
    st.session_state.first["Size"] += 1
    st.success("Selected and saved")

st.subheader("")


st.markdown("---") # Делител


# Графика по доминанта
st.subheader("Linear")
df = pd.DataFrame.from_dict(
    st.session_state.colors, orient="index", columns=["Rand"]
)
st.bar_chart(df)


# Графика по първоначални
st.subheader("Linear")
df = pd.DataFrame.from_dict(
    st.session_state.first, orient="index", columns=["Rand"]
)
st.bar_chart(df)
