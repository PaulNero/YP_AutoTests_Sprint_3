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
# Настраиваем пользователя с UID/GID Jenkins
# ===========================
ARG JENKINS_UID=115
ARG JENKINS_GID=121

# Создаём группу и пользователя с нужными ID
RUN groupadd -g ${JENKINS_GID} tester && \
    useradd -m -u ${JENKINS_UID} -g ${JENKINS_GID} tester && \
    mkdir -p /workspace && chown -R tester:tester /workspace /home/tester

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

RUN pip install --upgrade pip && pip install poetry selenium pytest allure-pytest && \
    rm -rf ~/.cache/pip

# ===========================
# Переключаемся на пользователя Jenkins
# ===========================
USER tester
WORKDIR /workspace

# ===========================
# Точка входа
# ===========================
CMD ["bash"]
