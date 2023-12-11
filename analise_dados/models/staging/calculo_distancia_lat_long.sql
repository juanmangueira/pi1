SELECT
    objetivo,
    id_lancamento,
    latitude,
    longitude,
    (latitude*60) AS distancia_latitude,
    (longitude*60) AS distancia_longitude,
FROM {{ref('stg_dados')}}
ORDER BY
    objetivo,
    id_lancamento