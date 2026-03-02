# SRE Journey: AWS E2E & Observability

Projeto focado em automação de infraestrutura e observabilidade.

## 🚀 Tecnologias Utilizadas
- **Ansible**: Automação de setup e deploy.
- **Docker & Docker Compose**: Conteinerização da aplicação e stack de monitoramento.
- **Prometheus**: Coleta de métricas (Time Series Database).
- **Grafana**: Visualização de dashboards (ID: 1860 - Node Exporter).
- **Python**: Aplicação alvo do deploy.

## 🛠️ Como rodar o deploy
1. Configure o IP no arquivo `ansible/hosts.ini`.
2. Rode o setup do Docker:
   `ansible-playbook -i ansible/hosts.ini ansible/setup-docker.yml -K`
3. Rode o deploy da aplicação e monitoramento:
   `ansible-playbook -i ansible/hosts.ini ansible/deploy-app.yml -K`

## 📊 Endereços Úteis
- App: `http://IP_SERVIDOR:8080`
- Prometheus: `http://IP_SERVIDOR:9090`
- Grafana: `http://IP_SERVIDOR:3000`
