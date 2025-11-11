from models import Perfil, Carreira
from typing import List, Dict, Any

def gerar_recomendacoes(perfil: Perfil, lista_carreiras: List[Carreira]) -> List[Dict[str, Any]]:
    recomendacoes = []

    for carreira in lista_carreiras:
        competencias_necessarias = carreira.competencias_necessarias
        competencias_usuario = perfil.competencias_usuario

        match = competencias_usuario.intersection(competencias_necessarias)

        faltantes = competencias_necessarias.difference(competencias_usuario)

        if not competencias_necessarias:
            percentual_match = 0.0
        else:
            percentual_match = (len(match) / len(competencias_necessarias)) * 100


        if percentual_match >= 40.0:
            recomendacoes.append({
                "carreira": carreira,
                "percentual_match": percentual_match,
                "competencias_match": match,
                "competencias_faltantes": faltantes
            })

    return sorted(recomendacoes, key=lambda r: r['percentual_match'], reverse=True)