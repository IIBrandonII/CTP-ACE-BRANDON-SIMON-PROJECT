type HealthResponse = {
  status: "ok";
  service: "ifms-api";
};

function isHealthResponse(data: unknown): data is HealthResponse {
  return (
    typeof data === "object" &&
    data !== null &&
    "status" in data &&
    "service" in data &&
    data.status === "ok" &&
    data.service === "ifms-api"
  );
}

export async function getApiHealth(): Promise<HealthResponse | null> {
  const baseUrl = process.env.API_BASE_URL;

  if (!baseUrl) {
    return null;
  }

  try {
    const response = await fetch(new URL("/api/v1/health", baseUrl), {
      method: "GET",
      cache: "no-store",
      signal: AbortSignal.timeout(5000),
    });

    if (!response.ok) {
      return null;
    }

    const data: unknown = await response.json();

    if (!isHealthResponse(data)) {
      return null;
    }

    return data;
  } catch {
    return null;
  }
}
