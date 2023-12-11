SELECT
    objetivo,
    id_lancamento,
    id_registro,
    variacao_tempo,
    velocidade_instantanea_inicial,
    velocidade_instantanea_final,
    variacao_velocidade/variacao_tempo AS aceleracao_instantanea
FROM (
    SELECT
        objetivo,
        id_lancamento,
        id_registro,
        variacao_tempo,
        velocidade_instantanea_final,
        velocidade_instantanea_inicial,
        velocidade_instantanea_final - velocidade_instantanea_inicial AS variacao_velocidade

    FROM (
        SELECT 
            objetivo,
            id_lancamento,
            id_registro,
            variacao_tempo,
            velocidade_instantanea_final,
            (LAG(velocidade_instantanea_final) OVER (ORDER BY objetivo, id_lancamento, id_registro)) AS velocidade_instantanea_inicial
        FROM(
            SELECT
                objetivo,
                id_lancamento,
                id_registro,
                variacao_tempo,
                velocidade_instantanea_final,
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