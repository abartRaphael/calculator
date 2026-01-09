FROM python:3.11-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS test-target
COPY . .
CMD ["sh", "-c", "python -m coverage run -m unittest discover -s tests && coverage report -m"]

FROM base AS production
COPY src .


