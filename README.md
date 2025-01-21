# Network Slicing Simulation

Este projeto implementa uma simção de **Network Slicing** em redes 5G, focando em mobilidade, análise de métricas de QoS (latência, jitter, throughput e perda de pacotes) e impacto da sobrecarga nas células.

---

## 📚 **Descrição do Projeto**

O projeto utiliza classes específicas para diferentes **slices de rede**:
- **eMBB (Enhanced Mobile Broadband)**: Alta largura de banda e latência moderada.
- **URLLC (Ultra Reliable Low Latency Communication)**: Latência ultrabaixa e alta confiabilidade.
- **mMTC (Massive Machine Type Communication)**: Suporte a um grande número de dispositivos IoT com tráfego esporádico.

### **Funcionalidades**
1. Simulação de cenários fixos (sem mobilidade) e móveis (com mobilidade entre células).
2. Aplicação de penalidades em métricas de QoS em caso de sobrecarga nas células.
3. Geração de relatórios detalhados em formato CSV.
4. Visualização gráfica de métricas e comparação entre cenários.

---

## 📂 **Estrutura do Projeto**

```plaintext
NetworkSlicingSimulation/
├── cells/
│   ├── cell.py       # Gerencia as células e sua capacidade
├── users/
│   ├── user.py       # Representa os usuários e suas conexões às células
├── slices/
│   ├── embb.py       # Classe para slice eMBB
│   ├── urllc.py      # Classe para slice URLLC
│   ├── mmtc.py       # Classe para slice mMTC
├── metrics/
│   ├── qos.py        # Calcula métricas de QoS
├── mobility.py        # Gerencia a mobilidade dos usuários entre células
├── utils.py           # Funções para exportação, análise e visualização de dados
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
- `qos_metrics_mobilidade.csv`: Métricas do cenário com mobilidade.
- `qos_overload_analysis.csv`: Impacto da sobrecarga nas métricas.

### **Gráficos**
Os gráficos incluem:
- Comparação de **latência**, **throughput**, **jitter** e **perda de pacotes** entre os cenários.
- Impacto da sobrecarga nas métricas.

---

## 🔧 **Configurações Adicionais**
- **Células**: Modifique a capacidade no arquivo `cell.py`.
- **Usuários**: Ajuste o número de usuários no script `simulation.py`.
- **Mapa de Adjacência**: Edite a variável `adjacency_map` no `simulation.py`.

---

## 🛠️ **Próximas Expansões**
1. Adicionar lógica de interferência entre células.
2. Implementar padrões de mobilidade mais complexos.
3. Melhorar o gerenciamento dinâmico de recursos por slice.
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

