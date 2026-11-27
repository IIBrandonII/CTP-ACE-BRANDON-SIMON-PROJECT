import Link from "next/link";

import { getApiHealth } from "@/lib/api";

export const dynamic = "force-dynamic";

export default async function StatusPage() {
  const health = await getApiHealth();
  const isHealthy = health !== null;

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-16 text-white">
      <section className="mx-auto max-w-3xl">
        <Link
          href="/"
          className="text-sm font-medium text-teal-400 hover:underline focus-visible:outline-2 focus-visible:outline-offset-4"
        >
          &larr; Back to iFindMySchool
        </Link>

        <h1 className="mt-8 text-4xl font-bold">System Status</h1>

        <p className="mt-3 text-slate-400">
          Development environment connectivity.
        </p>

        <div className="mt-8 space-y-4">
          <article className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-lg font-semibold">Frontend</h2>

            <p className="mt-2 text-emerald-400">Responding</p>

            <p className="mt-2 text-sm text-slate-400">
              Next.js rendered this page successfully.
            </p>
          </article>

          <article className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-lg font-semibold">Backend API</h2>

            <p
              className={`mt-2 font-medium ${
                isHealthy ? "text-emerald-400" : "text-amber-400"
              }`}
            >
              {isHealthy ? "Operational" : "Unavailable"}
            </p>

            <p className="mt-2 text-sm text-slate-400">
              {isHealthy
                ? "The FastAPI health endpoint returned a valid response."
                : "A valid response could not be obtained from the backend."}
            </p>
          </article>

          <article className="rounded-xl border border-slate-800 bg-slate-900 p-6">
            <h2 className="text-lg font-semibold">Database</h2>

            <p className="mt-2 text-slate-400">Not configured</p>

            <p className="mt-2 text-sm text-slate-400">
              PostgreSQL and PostGIS integration is planned for a future
              development phase.
            </p>
          </article>
        </div>

        <p className="mt-8 text-sm text-slate-400">
          Refresh this page to check connectivity again. These checks do not
          represent complete production system monitoring.
        </p>
      </section>
    </main>
  );
}
