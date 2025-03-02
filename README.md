# BatchCrypt

**BatchCrypt** é uma ferramenta simples e eficiente para ofuscar scripts Batch, transformando comandos legíveis em um formato mais difícil de entender, ajudando a proteger o código de visualização direta. Ideal para quem busca ocultar o funcionamento de scripts ou aumentar a segurança ao compartilhar arquivos Batch.

## Funcionalidades

- **Ofuscação de Scripts Batch**: Converte scripts legíveis em uma versão ofuscada, substituindo variáveis por nomes aleatórios.
- **Simulação de Processo**: Acompanha o progresso da ofuscação com uma barra de progresso e logs.
- **Download Automático**: Gera um arquivo `.bat` ofuscado pronto para ser baixado.

## Como Usar

### 1. Faça o upload do seu arquivo Batch

- Clique no botão de **Upload** e selecione o arquivo `.bat` que deseja ofuscar.

### 2. Ofusque o Script

- Após o upload, clique em **Ofuscar Script** para iniciar o processo de ofuscação.
- A barra de progresso será exibida enquanto o script é ofuscado.

### 3. Baixe o Script Ofuscado

- Após a conclusão da ofuscação, insira um nome para o novo arquivo ou use o nome padrão.
- Clique em **Download** para obter o script ofuscado.

## Exemplo de Uso

1. **Script Original**:
    ```batch
    @echo off
    set var=hello
    echo %var%
    ```

2. **Script Ofuscado**:
    ```batch
    @echo off
    set "s=s"
    set "e=e"
    set "t=t"
    
    %s%%e%%t% "GzNlPOdM=hello"
    %GzNlPOdM%
    ```

## Requisitos

- **Navegador**: Funciona em qualquer navegador moderno (Chrome, Firefox, Edge, etc.).
- **Sem Dependências**: Não requer instalação de software adicional.

## Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma branch com sua nova feature ou correção (`git checkout -b feature/BatchCrypt`).
3. Faça as alterações e comite-as (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório (`git push origin feature/BatchCrypt`).
5. Crie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

- **Inspiração**: Ferramentas de ofuscação de código open-source.
- **Tecnologias Usadas**: HTML, JavaScript, CSS.
