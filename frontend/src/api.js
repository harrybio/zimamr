const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// API endpoints
export const API = API_BASE;

// Summary endpoints
export const fetchCountsSummary = async () => {
  const response = await fetch(`${API_BASE}/summary/counts-summary/`);
  if (!response.ok) throw new Error('Failed to fetch counts summary');
  return response.json();
};

export const fetchTimeTrend = async (period = 'month') => {
  const response = await fetch(`${API_BASE}/summary/time-trends/?period=${period}`);
  if (!response.ok) throw new Error('Failed to fetch time trends');
  return response.json();
};

export const fetchOptions = async () => {
  const response = await fetch(`${API_BASE}/options/`);
  if (!response.ok) throw new Error('Failed to fetch options');
  return response.json();
};

// Other API functions
export const fetchFacilities = async () => {
  const response = await fetch(`${API_BASE}/facilities/`);
  if (!response.ok) throw new Error('Failed to fetch facilities');
  return response.json();
};

export const fetchSexAge = async () => {
  const response = await fetch(`${API_BASE}/sex-age/`);
  if (!response.ok) throw new Error('Failed to fetch sex/age data');
  return response.json();
};

export const fetchGeo = async () => {
  const response = await fetch(`${API_BASE}/geo/`);
  if (!response.ok) throw new Error('Failed to fetch geo data');
  return response.json();
};

export const fetchAntibiogram = async () => {
  const response = await fetch(`${API_BASE}/antibiogram/`);
  if (!response.ok) throw new Error('Failed to fetch antibiogram');
  return response.json();
};

export const fetchDataQuality = async () => {
  const response = await fetch(`${API_BASE}/data-quality/`);
  if (!response.ok) throw new Error('Failed to fetch data quality');
  return response.json();
};

export const fetchAlerts = async () => {
  const response = await fetch(`${API_BASE}/alerts/`);
  if (!response.ok) throw new Error('Failed to fetch alerts');
  return response.json();
};

// Upload functions
export const uploadFile = async (formData) => {
  const response = await fetch(`${API_BASE}/upload/`, {
    method: 'POST',
    body: formData,
  });
  if (!response.ok) throw new Error('Upload failed');
  return response.json();
};
