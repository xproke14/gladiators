SELECT war_name, count(fights.id) AS 'Number of wins' FROM warriors LEFT JOIN fights ON warriors.id = fights.winner_id
	GROUP BY warriors.id ORDER BY count(fights.id) DESC;


SELECT concat(war_name, ' won ', count(fights.id), ' times') AS 'Top 3' FROM warriors LEFT JOIN fights ON warriors.id = fights.winner_id
	GROUP BY warriors.id ORDER BY count(fights.id) DESC LIMIT 3;


SELECT concat(arena_name, ' hosted ', count(fights.id), ' fights.') AS 'Fights by arena' FROM arenas LEFT JOIN fights ON arenas.id = fights.arena_id
	GROUP BY arenas.id ORDER BY count(fights.id) DESC;


SELECT fights.id, winner.war_name as 'Winner', loser.war_name as 'Loser', arena_name FROM fights
	JOIN warriors winner ON winner.id = fights.winner_id
    JOIN warriors loser on loser.id = fights.loser_id
    JOIN arenas ON fights.arena_id = arenas.id
    ORDER BY fights.id;


