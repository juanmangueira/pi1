SELECT
    objetivo,
    id_lancamento,
    id_registro,
    tempo,
    latitude,
    longitude,
    (latitude*60) AS distancia_latitude,
    (longitude*60) AS distancia_longitude,
FROM {{ref('stg_dados')}}
ORDER BY
    objetivo,
    id_lancamento,
    id_registro
