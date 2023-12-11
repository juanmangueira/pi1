SELECT
    objetivo,
    id_lancamento,
    id_registro,
    variacao_tempo,
    variacao_distancia,
    (variacao_distancia / variacao_tempo) AS velocidade_instantanea
FROM (

    SELECT 
        objetivo,
        id_lancamento,
        id_registro,
        (tempo_final - tempo_inicial) AS variacao_tempo,
        (distancia_final - distancia_inicial) AS variacao_distancia,
    FROM(
        SELECT 
            objetivo,
            id_lancamento,
            id_registro,
            tempo_inicial,
            distancia_inicial,
            (LEAD(tempo_inicial) OVER (ORDER BY objetivo, id_lancamento, id_registro)) AS tempo_final,
            (LEAD(distancia_inicial) OVER (ORDER BY objetivo, id_lancamento, id_registro)) AS distancia_final,
            
        FROM(
            SELECT
                objetivo,
                CAST(id_lancamento AS INT) AS id_lancamento,
                CAST(id_registro AS INT) AS id_registro,
                distancia_percorrida AS distancia_inicial,
                tempo AS tempo_inicial
            FROM {{ref('calculo_distancia_percorrida')}}
            ORDER BY
                objetivo,
                id_lancamento,
                id_registro
        )
        ORDER BY
            objetivo,
            id_lancamento,
            id_registro
    )
    ORDER BY
        objetivo,
        id_lancamento,
        id_registro
)
ORDER BY
    objetivo,
    id_lancamento,
    id_registro