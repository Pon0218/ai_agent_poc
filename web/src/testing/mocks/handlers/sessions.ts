import { HttpResponse, http } from 'msw';

import { env } from '@/config/env';
import { networkDelay } from '../utils';

export const sessionsHandlers = [
	http.post(`${env.API_URL}/sessions`, async () => {
		await networkDelay();

		return HttpResponse.json({
			success: true,
			data: {
				session_id: 'sess_000001',
				status: 'created',
				message: '分析任務已建立'
			},
			error: null,
			meta: null
		});
	})
];
