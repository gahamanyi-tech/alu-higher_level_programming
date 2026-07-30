# SQL - More Queries

This project covers advanced SQL concepts including user privileges, subqueries, relational database constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE), and database JOIN operations (INNER JOIN, LEFT JOIN, GROUP BY).

## Files & Descriptions

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists all privileges of users `user_0d_1` and `user_0d_2`. |
| `1-create_user.sql` | Creates root-like user `user_0d_1` with full privileges. |
| `2-create_read_user.sql` | Creates database `hbtn_0d_2` and user `user_0d_2` with SELECT rights. |
| `3-force_name.sql` | Creates table `force_name` with non-null `name` column. |
| `4-never_empty.sql` | Creates table `id_not_null` with default `id = 1`. |
| `5-unique_id.sql` | Creates table `unique_id` with unique `id` default 1. |
| `6-states.sql` | Creates database `hbtn_0d_usa` and table `states` with PRIMARY KEY. |
| `7-cities.sql` | Creates table `cities` with FOREIGN KEY referencing `states`. |
| `8-cities_of_california_subquery.sql` | Subquery listing California cities. |
| `9-cities_by_state_join.sql` | JOIN listing all cities with state names. |
| `10-genre_id_by_show.sql` | Lists shows with linked genre IDs. |
| `11-genre_id_all_shows.sql` | Lists all shows including those without genres (LEFT JOIN). |
| `12-no_genre.sql` | Filters shows that do not have any linked genre. |
| `13-count_shows_by_genre.sql` | Counts shows per genre using GROUP BY. |
| `14-my_genres.sql` | Lists all genres assigned to the show 'Dexter'. |
| `15-comedy_only.sql` | Lists all shows categorized under the 'Comedy' genre. |
| `16-shows_by_genre.sql` | Displays full mapping of shows to genre names. |
