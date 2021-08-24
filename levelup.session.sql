SELECT * FROM levelupapi_gametype;

SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;

SELECT * FROM levelupapi_game;

SELECT * FROM levelupapi_event;

SELECT
    e.id,
    e.title,
    e.game_id,
    e.date,
    e.time,
    e.description,
    e.host_id,
    g.title as g_title,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM 
    levelupapi_event e
JOIN 
    levelupapi_game g ON e.game_id = g.id
JOIN
    auth_user u ON e.host_id = u.id