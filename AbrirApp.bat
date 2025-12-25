@echo off
setlocal
title Meu App Python Seguro

:: 1. Verifica se o Python está no PATH
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado! 
    echo Por favor, instale o Python 3.11 ou superior para rodar este app.
    pause
    exit /b
)

:: 2. Tenta rodar o app usando o seu carregador __main__.py
:: O Python carregará os arquivos .pyd (binários) automaticamente da pasta /app
python __main__.py

if %errorlevel% neq 0 (
    echo.
    echo [AVISO] O aplicativo fechou com erro (Codigo: %errorlevel%).
    pause
)