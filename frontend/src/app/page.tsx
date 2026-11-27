import Link from "next/link";

export default function Home() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 px-6 text-white">
      <section className="max-w-3xl text-center">
        <p className="mb-4 text-sm font-semibold tracking-widest text-teal-400">
          iFindMySchool
        </p>

        <h1 className="text-4xl font-bold tracking-tight sm:text-6xl">
          Find Your School.
          <span className="block text-teal-400">Explore the Facts.</span>
        </h1>

        <p className="mt-6 text-lg leading-8 text-slate-300">
          Discover NYC public schools through transparent data, accessible
          information, and responsible research.
        </p>

        <Link
          href="/status"
          className="mt-8 inline-flex rounded-lg border border-teal-400 px-6 py-3 font-medium text-teal-400 transition-colors hover:bg-teal-400 hover:text-slate-950 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-teal-400 motion-reduce:transition-none"
        >
          View System Status
        </Link>

        <p className="mt-8 text-sm text-slate-400">
          Development version - school data integration is not yet available.
        </p>
      </section>
    </main>
  );
}
