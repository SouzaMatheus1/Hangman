BIBLIOTECA_PANDAS=$(pip freeze | grep pandas)
BIBLIOTECA_RANDOM=$(pip freeze | grep random)
APT_PIP=$(sudo apt list | grep python3-pip)

clear
if [ "" = "$APT_PIP" ]; then
    sudo apt install python3-pip

  echo '\n-------------------------------------------------------'
  echo 'pip instalado com sucesso.'
fi

if [ "" = "$BIBLIOTECA_PANDAS" ]; then
  pip install pandas

  echo '\n-------------------------------------------------------'
  echo 'Biblioteca Pandas instalado com sucesso.'
else
  echo "Biblioteca Pandas já instalado."
fi

if [ "" = "$BIBLIOTECA_RANDOM" ]; then
  pip install pandas

  echo '\n-------------------------------------------------------'
  echo 'Biblioteca Random instalado com sucesso.'
else
  echo "Biblioteca Random já instalado."
fi

if [ "" = "$BIBLIOTECA_OS" ]; then
  pip install os

  echo '\n-------------------------------------------------------'
  echo "Biblioteca OS instalada com suscesso."
else
  echo "Biblioteca OS já instalada."
fi

echo '\n-------------------------------------------------------'
echo 'Iniciando jogo...'

python3 Hangman.py