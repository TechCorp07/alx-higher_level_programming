-- Uses the hbtn_0d_tvshows database to lists all shows without the denre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
        SELECT tv_shows.title
        FROM tv_shows
            JOIN tv_show_genres AS sg ON tv_shows.id = sg.show_id
            JOIN tv_genres AS s ON sg.genre_id = s.id
        WHERE s.name = "Comedy"
    )
ORDER BY tv_shows.title;
