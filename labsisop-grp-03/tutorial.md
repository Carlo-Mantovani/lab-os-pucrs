# Configuração do Ambiente de Desenvolvimento

## Diretórios de Trabalho
- Diretório Buildroot: `labsisop-grp-03`
- Diretório do Kernel Linux: `linux-4.13.9`

## Instalação do QEMU
Certifique-se de ter o QEMU instalado. Você pode instalá-lo usando o seguinte comando:

```bash
sudo apt-get install qemu-system
```
# Configuração do Buildroot

Acesse o diretório do Buildroot:


```bash
cd labsisop-grp-03
```

Execute o seguinte comando para abrir o menu de configuração:

```bash
make menuconfig
```
No menu, navegue para "Toolchain" e altere a opção "C library" para "uclib".

Ainda em "Toolchain", habilite o suporte a C++.

#  Configuração do Buildroot - Tutorial do professor 2.1 a partir do Tópico 3

Obs: 
Quando você editar caminhos, use o caminho absoluto, você pode obtê-lo usando o comando pwd no terminal.

Após o tutorial: 
Copie os três arquivos no root do repositório para o diretório lab.../output/images.

No diretório do Buildroot, execute o seguinte comando para criar um arquivo sdb.bin (disco lógico):

```bash

dd if=/dev/zero of=sdb.bin bs=512 count=2097152
```
Execute make menuconfig novamente no diretório do Buildroot.

Navegue até "System Configuration" e encontre a opção "(board/qemu/x86/post-build.sh) Custom scripts to run before creating file system images".

Pressione "Enter" e altere para: custom-scripts/pre-build.sh

Salve as configurações.

Execute o seguinte comando para iniciar a compilação:

```bash

make

```

# Executando a Emulação

No diretório do Buildroot, inicie a emulação com o seguinte comando:

```bash

./qemu-start.sh
```
Buildroot login: root



