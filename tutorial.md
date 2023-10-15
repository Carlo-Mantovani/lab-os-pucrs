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



#  Configuração do Buildroot - Tutorial do professor 2.1 a partir do Tópico 3 até a parte de mandar make clean

Antes de fazer make clean e make:
No menu (menuconfig), navegue para "Toolchain" e habilite o suporte a C++ (barra de espaco)


Obs: 
Quando você editar path (no tutorial o export LINUX....), use o caminho absoluto, você pode obtê-lo usando o comando pwd no terminal.

Continuar o tutorial até parte de emular no topico 4

Navegue até "System Configuration" e encontre a opção "(board/qemu/x86/post-build.sh) Custom scripts to run before creating file system images".

Pressione "Enter" e altere para: custom-scripts/pre-build.sh

Se der algum erro no make, rodar no diretorio buildroot:
```bash
rm output/build/linux-custom/.stamp_*
```

Copie os três arquivos no root do repositório para o diretório lab.../output/images. (bzimage, rootfs.ext2, start-qemu.sh). CASO ELES NAO EXISTIREM



No diretório do Buildroot, execute o seguinte comando para criar um arquivo sdb.bin (disco lógico):

```bash

dd if=/dev/zero of=sdb.bin bs=512 count=2097152
```
Execute make menuconfig novamente no diretório do Buildroot.



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



