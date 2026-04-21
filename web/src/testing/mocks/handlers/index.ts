import { HttpResponse, http } from 'msw';

import { env } from '@/config/env';
import { anonymizedHandlers } from './anonymized';

export const handlers = [
	...anonymizedHandlers,
	http.get(`${env.API_URL}/healthcheck`, async () => {
		return HttpResponse.json({ ok: true });
	})
];
