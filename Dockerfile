# ===========================
# Базовый образ Python
# ===========================
FROM python:3.10-slim

# ===========================
# Устанавливаем системные зависимости
# ===========================
RUN apt-get update -y && apt-get install -y \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    xdg-utils \
    wget \
    unzip \
    xvfb \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# ===========================
# Добавляем ключ и репозиторий Chrome
# ===========================
RUN mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /etc/apt/keyrings/google-linux-signing-key.gpg && \
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Проверка версии Chrome
RUN google-chrome --version

# ===========================
# Создаем пользователя для безопасной работы
# ===========================
RUN groupadd -r tester && useradd -r -g tester -m tester \
    && mkdir -p /workspace && chown tester:tester /workspace /home/tester

# ===========================
# Устанавливаем Python-зависимости
# ===========================
ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_ROOT_USER_ACTION=ignore \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/usr/local/bin:/home/tester/.local/bin:$PATH"

RUN pip install poetry selenium pytest allure-pytest

# ===========================
# Переключаемся на безопасного пользователя
# ===========================
USER tester
WORKDIR /workspace

# ===========================
# По умолчанию просто bash
# ===========================
CMD ["bash"]
