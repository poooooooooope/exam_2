def country(**kwargs):
    for key, value in kwargs.items():
            print(f"{key} - {value}")

country(county="USA", population="330 million", is_democratic=True)
