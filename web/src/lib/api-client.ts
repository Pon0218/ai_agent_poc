// Axios client instances and global interceptor configuration
import axios from 'axios';

import { env } from '@/config/env';

// Create axios instance
export const anonymized_api = axios.create({
	baseURL: env.API_URL
	// timeout: 12000,
});

// ─── Interceptors ────────────────────────────────────────────────────────────

[anonymized_api].forEach((client) => {
	// Request interceptor
	client.interceptors.request.use(
		(config) => {
			return config;
		},
		(error) => {
			return Promise.reject(error);
		}
	);

	// Response interceptor — unwrap data and handle errors
	client.interceptors.response.use(
		(response) => {
			return response.data;
		},
		(error) => {
			// Log 500 server errors
			if (error.response?.status === 500) {
				console.error('Server error:', error);
			}

			return Promise.reject(error);
		}
	);
});
