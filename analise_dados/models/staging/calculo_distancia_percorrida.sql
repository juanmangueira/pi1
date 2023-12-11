SELECT
    objetivo,
    id_lancamento,
    id_registro,
    tempo,
    distancia_latitude,
    distancia_longitude,
    SQRT(POWER(distancia_latitude, 2) + POWER(distancia_longitude, 2)) AS distancia_percorrida
FROM {{ref('calculo_distancia_lat_long')}}
ORDER BY
    objetivo,
    id_lancamento,
    id_registro