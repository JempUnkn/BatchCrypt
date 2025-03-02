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

## Limitações da Versão Atual

A versão atual do obfuscador não é compatível com scripts de Batch mais complexos, como aqueles que utilizam estruturas como `if`, `else` e `for`. Esses comandos podem não funcionar corretamente após a ofuscação, já que a ferramenta foi desenvolvida para lidar apenas com comandos mais simples de Batch.

### O que fazer?

Para contornar essas limitações, recomenda-se o seguinte processo:

1. **Hospedar seu arquivo em um local seguro**: Faça o upload do seu script Batch em um repositório ou servidor seguro. Certifique-se de que o arquivo permaneça acessível via URL RAW. Um exemplo de URL seria:

   ```
   https://raw.githubusercontent.com/SeuUsuario/SeuRepositorio/main/seu_arquivo.bat
   ```

2. **Baixar e executar o arquivo diretamente**: Use o PowerShell para baixar e executar o arquivo de forma temporária. Isso pode ser feito com o seguinte comando:

   ```powershell
   powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/SeuUsuario/SeuRepositorio/main/seu_arquivo.bat' -OutFile \"$env:TEMP\\seu_arquivo.bat\"; cmd /c \"$env:TEMP\\seu_arquivo.bat\"; Remove-Item \"$env:TEMP\\seu_arquivo.bat\""
   ```

   Substitua `'https://raw.githubusercontent.com/SeuUsuario/SeuRepositorio/main/seu_arquivo.bat'` pela URL do seu arquivo RAW.

3. **Versão Melhorada**: Após fazer upload do arquivo em um repositório, basta criar um arquivo seguindo o exemplo abaixo.

   Um exemplo de como o código melhorado pode se parecer:

   ```batch
   @echo off
   powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/SeuUsuario/SeuRepositorio/main/seu_arquivo.bat' -OutFile \"$env:TEMP\\seu_arquivo.bat\"; cmd /c \"$env:TEMP\\seu_arquivo.bat\"; Remove-Item \"$env:TEMP\\seu_arquivo.bat\""
   ```

4. **Upload no Obfuscador**: Para dar o próximo passo, você pode usar o nosso **Obfuscador** [aqui](#link). Basta fazer o upload do arquivo e seguir as instruções para gerar a versão ofuscada e segura do seu script.

## Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma branch com sua nova feature ou correção (`git checkout -b feature/BatchCrypt`).
3. Faça as alterações e comite-as (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório (`git push origin feature/BatchCrypt`).
5. Crie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

- **Minhas necessidades**: Eu precisava de obfuscador para um projeto que usa Bacthfile e sem sucesso ao procurar na Net.
- **Tecnologias Usadas**: HTML, JavaScript, CSS.

## LINK
- [BatchCrypt.io](https://jempunkn.github.io/BatchCrypt)
