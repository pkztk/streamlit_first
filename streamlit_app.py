# Tytuł aplikacji
st.title('Demo formularza Streamlit')

# Tworzenie formularza
with st.form(key='form1'):
    st.text_input(label='Wpisz jakiś tekst')
    st.number_input(label='Wpisz liczbę', step=1)
    st.text_area(label='Wpisz dłuższy tekst')
    st.date_input(label='Wybierz datę')
    st.time_input(label='Wybierz czas')

    radio_option = st.radio(label='Wybierz opcję', options=['Opcja A', 'Opcja B', 'Opcja C'])
    selectbox_option = st.selectbox(label='Wybierz z listy', options=['Item 1', 'Item 2', 'Item 3'])
    multiselect_option = st.multiselect(label='Wybierz wiele opcji', options=['Option 1', 'Option 2', 'Option 3'])

    slider_value = st.slider(label='Przesuń slider', min_value=0, max_value=100)
    select_slider_value = st.select_slider(label='Przesuń i wybierz', options=['jeden', 'dwa', 'trzy'])

    st.file_uploader(label='Prześlij plik')
    st.camera_input(label='Zrób zdjęcie')

    color_picker_value = st.color_picker(label='Wybierz kolor')

    # Przycisk do wysyłania formularza
    submit_button = st.form_submit_button(label='Wyślij')

# Logika po naciśnięciu przycisku
if submit_button:
    st.write('Wybrana opcja (radio):', radio_option)
    st.write('Wybrana opcja (selectbox):', selectbox_option)
    st.write('Wybrane opcje (multiselect):', multiselect_option)
    st.write('Wartość slidera:', slider_value)
    st.write('Wartość select slidera:', select_slider_value)
    st.write('Wybrany kolor:', color_picker_value)
