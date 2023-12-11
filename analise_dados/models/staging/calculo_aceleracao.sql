SELECT 
    *
FROM(

    SELECT
        objetivo,
        id_lancamento,
        id_registro,
        variacao_tempo,
        velocidade_instantanea AS velocidade_instantanea_final,
        (LAG(velocidade_instantanea_final) OVER (ORDER BY objetivo, id_lancamento, id_registro)) AS velocidade_instantanea_inicial,
    FROM(
        SELECT
            objetivo,
            id_lancamento,
            id_registro,
            variacao_tempo,
            velocidade_instantanea AS velocidade_instantanea_final
        FROM {{ref('calculo_velocidade')}}
    )
)