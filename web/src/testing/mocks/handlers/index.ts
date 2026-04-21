import { HttpResponse, http } from 'msw';

import { env } from '@/config/env';
import { sessionsHandlers } from './sessions';
import { swotHandlers } from './swot';

export const handlers = [
	...sessionsHandlers,
	...swotHandlers,
	http.get(`${env.API_URL}/healthcheck`, async () => {
		return HttpResponse.json({ ok: true });
	})
];
