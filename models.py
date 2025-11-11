from dataclasses import dataclass, field
from typing import Set

@dataclass(frozen=True)
class Competencia:
    nome: str
    tipo: str 

@dataclass
class Carreira:
    nome: str
    descricao: str
    competencias_necessarias: Set[Competencia]

@dataclass
class Perfil:
    nome_usuario: str
    competencias_usuario: Set[Competencia] = field(default_factory=set)

    def adicionar_competencia(self, competencia: Competencia):
        self.competencias_usuario.add(competencia)