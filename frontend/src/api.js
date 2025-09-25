const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';
export const API = API_BASE;

export const fetchCountsSummary = async () => {
  const response = await fetch(`${API_BASE}/summary/counts-summary/`);
  return response.json();
};

export const fetchTimeTrend = async (period = 'month') => {
  const response = await fetch(`${API_BASE}/summary/time-trends/?period=${period}`);
  return response.json();
};

// Export as both 'fetchOptions' and 'options' for compatibility
export const fetchOptions = async () => {
  const response = await fetch(`${API_BASE}/options/`);
  return response.json();
};

// Keep the old export name for compatibility
export const options = fetchOptions;

export const fetchFacilities = async () => {
  const response = await fetch(`${API_BASE}/facilities/`);
  return response.json();
};

export const fetchSexAge = async () => {
  const response = await fetch(`${API_BASE}/sex-age/`);
  return response.json();
};

export const fetchGeo = async () => {
  const response = await fetch(`${API_BASE}/geo/`);
  return response.json();
};

export const fetchAntibiogram = async () => {
  const response = await fetch(`${API_BASE}/antibiogram/`);
  return response.json();
};

export const fetchDataQuality = async () => {
  const response = await fetch(`${API_BASE}/data-quality/`);
  return response.json();
};

export const fetchAlerts = async () => {
  const response = await fetch(`${API_BASE}/alerts/`);
  return response.json();
};

export const uploadFile = async (formData) => {
  const response = await fetch(`${API_BASE}/upload/`, {
    method: 'POST',
    body: formData,
  });
  return response.json();
};
