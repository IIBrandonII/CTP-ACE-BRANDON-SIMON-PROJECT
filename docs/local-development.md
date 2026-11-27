# iFindMySchool (iFMS) — Local Development

> Find Your School. Explore the Facts.

## 1. Project Overview

iFindMySchool is a school discovery and research platform
designed to help NYC families explore public schools using
transparent data and responsible research.

## 2. Technology Stack

### Frontend

- Next.js App Router
- React
- TypeScript
- Tailwind CSS
- ESLint
- Prettier

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- Ruff

### Planned Infrastructure

- PostgreSQL
- PostGIS
- SQLAlchemy
- Alembic
- Docker
- GitHub Actions
- Vercel

## 3. Development Prerequisites

Install the following tools:

- Git
- Node.js and npm
- Python
- Docker
- Visual Studio Code (recommended)

### Observed Local Development Environment

- Operating system: macOS
- Node.js: 26.7.0
- Python: 3.15.2
- Next.js: 16.4.6
- Pytest: 9.2.0

Production runtime versions will be finalized after
dependency and hosting compatibility testing.

## 4. Clone the Repository

```bash
git clone https://github.com/aakashghartichhetri/iFMS.git
cd iFMS
```

## 5. Backend Setup

From the project root:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
```

Start the development server:

```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Backend URL:

http://127.0.0.1:8000

Health endpoint:

http://127.0.0.1:8000/api/v1/health

Interactive API documentation:

http://127.0.0.1:8000/docs

## 6. Frontend Setup

Open a separate terminal from the project root:

```bash
cd frontend
npm ci
```

Create the local environment configuration if it
does not already exist:

```bash
cp -n .env.example .env.local
```

The local environment file should contain:

```env
API_BASE_URL=http://127.0.0.1:8000
```

Start the frontend:

```bash
npm run dev
```

Homepage:

http://localhost:3000

System status:

http://localhost:3000/status

## 7. Backend Verification

From the backend directory with the virtual
environment activated:

```bash
python -m pip check
python -m pytest -v
python -m ruff check app tests
python -m ruff format --check app tests
```

## 8. Frontend Verification

From the frontend directory:

```bash
npm run lint
npm run typecheck
npm run build
```

After a successful production build:

```bash
npm run start
```

Stop the development server before starting
the production server on the same port.

## 9. Architecture

The frontend communicates with the FastAPI backend
through versioned REST endpoints.

Next.js Server Components execute backend requests
on the server.

The homepage is statically rendered.

The system status page is dynamically rendered
to retrieve current backend connectivity information.

## 10. Failure and Recovery Testing

With both applications running:

1. Visit the system status page.
2. Confirm that the backend reports Operational.
3. Stop the backend server.
4. Refresh the status page.
5. Confirm that the backend reports Unavailable.
6. Confirm that the homepage remains accessible.
7. Restart the backend.
8. Refresh the status page.
9. Confirm that the backend reports Operational.

## 11. Security

Never commit:

- Environment files containing secrets
- API keys or passwords
- Python virtual environments
- Node.js dependencies
- Generated build artifacts
- Temporary test and linting caches

The .env.example file contains public example
configuration only.

## 12. Current Limitations

- PostgreSQL and PostGIS are not integrated.
- Real school datasets are not connected.
- School search and comparison are not implemented.
- Research results have not been validated for publication.
- Production deployment is not configured.
- The health endpoint verifies API responsiveness only.
- Team repository integration remains to be confirmed.

## 13. Development Workflow

1. Create or select a development branch.
2. Implement a small, focused change.
3. Run automated verification.
4. Review the Git diff.
5. Create a meaningful commit.
6. Push the development branch.
7. Open a pull request for review.

Avoid developing directly on the main branch.