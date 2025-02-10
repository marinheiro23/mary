#!/bin/bash

# Mensagem padrão para o commit
mensagem="Atualização automática"

# Se o usuário fornecer uma mensagem, usa essa em vez da padrão
if [ ! -z "$1" ]; then
    mensagem="$1"
fi

echo "📂 Adicionando arquivos ao Git..."
git add .

echo "📝 Criando commit..."
git commit -m "$mensagem"

echo "🚀 Enviando para o GitHub..."
git push origin main  # Mude para 'master' se necessário

echo "✅ Arquivos enviados com sucesso!"

