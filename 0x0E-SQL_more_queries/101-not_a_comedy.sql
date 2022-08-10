-- Uses the hbtn_0d_tvshows database to lists all shows without the denre Comedy
SELECT g.title
FROM tv_genres AS g
WHERE g.title NOT IN (
        SELECT g.title
        FROM tv_genres AS g
            JOIN tv_show_genres AS sg ON g.id = sg.genre_id
            JOIN tv_shows AS s ON sg.show_id = s.id
        WHERE s.name = "Comedy"
    )
ORDER BY g.title;
