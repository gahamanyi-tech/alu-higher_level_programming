# Python - Object-relational mapping

This project covers connecting Python scripts to MySQL databases using `MySQLdb` and `SQLAlchemy`.

## Project Tasks

* **0-select_states.py**: Script that lists all states from `hbtn_0e_0_usa`.
* **1-filter_states.py**: Script that lists all states with a name starting with `N`.
* **2-my_filter_states.py**: Script that displays values matching user input.
* **3-my_safe_filter_states.py**: Script safe from MySQL injection vulnerabilities.
* **4-cities_by_state.py**: Script that lists all cities from `hbtn_0e_4_usa`.
* **5-filter_cities.py**: Script that lists all cities of a given state.
* **model_state.py**: Python file defining the `State` class and SQLAlchemy `Base`.
* **7-model_state_fetch_all.py**: Lists all `State` objects using SQLAlchemy.
* **8-model_state_fetch_first.py**: Prints the first `State` object.
* **9-model_state_filter_a.py**: Lists all `State` objects containing the letter `a`.
* **10-model_state_my_get.py**: Prints `State` object matching argument.
* **11-model_state_insert.py**: Adds the `State` object "Louisiana".
* **12-model_state_update_id_2.py**: Updates `State` where `id = 2` to "New Mexico".
* **13-model_state_delete_a.py**: Deletes all `State` objects with name containing letter `a`.
* **model_city.py**: Python file defining the `City` class.
* **14-model_city_fetch_by_state.py**: Prints all `City` objects linked to their state.
