
1) Definição do Sistema**
A Clinica Total Saúde é um sistema de gestão para uma clínica médica, desenvolvido em Python com interface gráfica utilizando a biblioteca Tkinter e banco de dados SQLite. A aplicação tem como objetivo automatizar e facilitar os processos administrativos da clínica, permitindo que a recepção faça o login e registro de usuários, cadastre médicos (com informações como nome, especialidade e CRM) e pacientes (com nome, idade e médico responsável). Além disso, oferece um controle eficaz dos atendimentos, permitindo marcar cada paciente como pendente ou atendido, proporcionando uma visão clara do fluxo de atendimentos.



2) Requisitos Básicos do Sistema

Login e Registro de Usuários (Recepção): O sistema possibilita a criação e autenticação de usuários por meio de e-mail e senha.


Cadastro de Médicos: Permite o cadastro de médicos com informações essenciais, como nome, especialidade e CRM (com verificação de duplicidade do CRM).

Cadastro de Pacientes: Permite o cadastro de pacientes, incluindo nome, idade, médico responsável e status do atendimento (pendente ou atendido).

Gerenciamento de Atendimentos: O sistema permite alterar o status de cada paciente para 'pendente' ou 'atendido', facilitando o controle do fluxo de atendimentos.

Listagens**: O sistema oferece consultas de todos os médicos e pacientes cadastrados, com o vínculo entre paciente e médico.

Banco de Dados Integrado**: O sistema utiliza um banco de dados relacional (SQLite) para garantir a persistência dos dados de usuários, médicos e pacientes.



3) Uso do Banco de Dados no Sistema Proposto**

O sistema faz uso do SQLite como banco de dados relacional. Essa escolha foi feita devido à leveza do SQLite, que não exige instalação extra e é ideal para sistemas de pequeno a médio porte. O banco de dados do sistema é composto pelas seguintes tabelas:

Tabela 'usuarios': Armazena os dados dos usuários da recepção (nome, e-mail e senha).

Tabela 'medicos': Registra os médicos, incluindo nome, especialidade e CRM. O CRM é único para garantir que não haja duplicidade.

Tabela 'pacientes': Mantém os dados dos pacientes, vinculados a um médico por meio de chave estrangeira (medico_id), além do status do atendimento.


