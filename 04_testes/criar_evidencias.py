import os

def create_md_file(hu_name, ct_number, description, procedure, expected_result, evidence_links):
    hu_path = os.path.join("04_testes", "Externo - new", f"Mesario - {hu_name}")
    ct_path = os.path.join(hu_path, f"CT{ct_number} - {description}")

    if not os.path.exists(hu_path):
        print(f"A HU '{hu_name}' não existe. Por favor, crie a HU antes de adicionar um CT.")
        return
    if os.path.exists(ct_path):
        print(f"O CT '{ct_number}' já existe na HU '{hu_name}'.")
        return

    evidences_path = os.path.join(ct_path, "evidencias")
    os.makedirs(evidences_path, exist_ok=True)
    md_file_path = os.path.join(ct_path, f"CT{ct_number}.md")
    md_content = f"""# CT{ct_number} - {description}

<details>
<summary><strong>Descrição</strong></summary>
<p>{description}</p>
</details>

<details>
<summary><strong>Procedimento</strong></summary>
<p>{procedure}</p>
</details>

<details>
<summary><strong>Resultado Esperado</strong></summary>
<p>{expected_result}</p>
</details>

<details>
<summary><strong>Links para Evidências</strong></summary>
<p>{evidence_links}</p>
</details>

Criando uma POC para o novo modelo de evidências
"""

    with open(md_file_path, 'w') as md_file:
        md_file.write(md_content)
    print(f"Arquivo CT{ct_number}.md criado com sucesso em {ct_path}")

# Exemplo de uso do script
create_md_file(
    hu_name="HU025 Realizar Treinamento Novo",
    ct_number="0024",
    description="Exibição do Índice do Treinamento",
    procedure="1. Navegar até a tela de treinamento no aplicativo.<br>2. Observar a parte inferior da tela para verificar a presença do índice.",
    expected_result="O índice deve ser exibido como um menu suspenso na parte inferior da tela. Este índice deve conter os nomes dos módulos, das aulas, das atividades e das avaliações disponíveis no treinamento.",
    evidence_links="- <a href='evidencias/exemplo_01.png'>Imagem do Índice na Tela de Treinamento</a><br>- <a href='link-para-imagem2'>Detalhe do Índice com Módulos e Aulas</a>"
)
