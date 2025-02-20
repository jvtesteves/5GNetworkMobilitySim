# Network Slicing Simulation

Este projeto implementa uma simulação de **Network Slicing** em redes 5G, focando em mobilidade, análise de métricas de QoS (latência, jitter, throughput e perda de pacotes), impacto da sobrecarga, falhas temporárias nas células e interferência entre células vizinhas.

---

## 📚 **Descrição do Projeto**

O projeto utiliza classes específicas para diferentes **slices de rede**:
- **eMBB (Enhanced Mobile Broadband)**: Alta largura de banda e latência moderada.
- **URLLC (Ultra Reliable Low Latency Communication)**: Latência ultrabaixa e alta confiabilidade.
- **mMTC (Massive Machine Type Communication)**: Suporte a um grande número de dispositivos IoT com tráfego esporádico.

### **Funcionalidades**
1. Simulação de cenários fixos (sem mobilidade) e móveis (com mobilidade entre células).
2. Aplicação de penalidades em métricas de QoS em caso de sobrecarga nas células.
3. Introdução de falhas temporárias nas células, forçando a movimentação dos usuários.
4. Simulação da interferência entre células vizinhas, impactando jitter, throughput e perda de pacotes.
5. Geração de relatórios detalhados em formato CSV.
6. Visualização gráfica de métricas, comparação entre cenários e impacto das falhas e interferência.

---

## 📂 **Estrutura do Projeto**

```plaintext
NetworkSlicingSimulation/
├── cells/
│   ├── cell.py       # Gerencia as células, falhas temporárias, interferência e capacidade
├── users/
│   ├── user.py       # Representa os usuários e suas conexões às células
├── slices/
│   ├── embb.py       # Classe para slice eMBB
│   ├── urllc.py      # Classe para slice URLLC
│   ├── mmtc.py       # Classe para slice mMTC
├── metrics/
│   ├── qos.py        # Calcula métricas de QoS considerando interferência
├── mobility.py        # Gerencia a mobilidade dos usuários entre células
├── utils.py           # Funções para exportação, análise, falhas e visualização de dados
├── simulation.py      # Script principal para execução das simulações
└── README.md          # Documentação do projeto
```

---

## 🚀 **Como Executar**

### **Pré-requisitos**
- Python 3.8+
- Bibliotecas necessárias:
  ```bash
  pip install matplotlib pandas
  ```

### **Passo a Passo**
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/network-slicing-simulation.git
   cd network-slicing-simulation
   ```
2. Execute o script principal:
   ```bash
   python simulation.py
   ```

---

## 📊 **Resultados**

### **Relatórios CSV**
Os relatórios são gerados automaticamente após a execução:
- `qos_metrics_fixa.csv`: Métricas do cenário fixo.
- `qos_metrics_mobilidade_interferencia.csv`: Métricas do cenário com mobilidade, falhas temporárias e interferência.
- `qos_overload_analysis.csv`: Impacto da sobrecarga nas métricas.
- `cell_failures.csv`: Relatório dos períodos de falha das células.

### **Gráficos**
Os gráficos incluem:
- Comparação de **latência**, **throughput**, **jitter** e **perda de pacotes** entre os cenários.
- Impacto da sobrecarga nas métricas.
- Visualização do impacto das falhas temporárias e interferência nas métricas de QoS.

---

## 🔧 **Configurações Adicionais**
- **Células**: Modifique a capacidade e o nível de interferência no arquivo `cell.py`.
- **Usuários**: Ajuste o número de usuários no script `simulation.py`.
- **Mapa de Adjacência**: Edite a variável `adjacency_map` no `simulation.py`.
- **Duração das falhas**: Modifique a duração no método `deactivate` em `cell.py`.
- **Parâmetros de Interferência**: Ajuste o cálculo no arquivo `qos.py`.

---

## 🛠️ **Próximas Expansões**
1. Implementar padrões de mobilidade mais complexos.
2. Melhorar o gerenciamento dinâmico de recursos por slice.
3. Adicionar diferentes tipos de tráfego para cada slice.
4. Criar uma interface gráfica para configuração interativa.

---

## 📄 **Licença**
Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---

## 💡 **Contribuições**
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 🤝 **Contato**
- **Autor**: João Victor Tavares Esteves
- **Email**: joaovtesteves2002@gmail.com

