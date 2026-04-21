import { z } from 'zod';
import { env } from '@/config/env';
import { anonymized_api } from '@/lib/api-client';

// ---------------------------------- API URL ----------------------------------------------------
export const url = (sessionId: string) => `${env.API_URL}/sessions/${sessionId}/swot/generate`;

// --------------------------------- 1. Zod Schema & TypeScript Types ------------------------------

export const OutputSchema = z.object({
	success: z.boolean(),
	data: z.object({
		session_id: z.string(),
		status: z.string(),
		swot_markdown: z.string()
	}),
	error: z.string().nullable(),
	meta: z
		.object({
			message: z.string().nullable().optional()
		})
		.nullable()
});

export type OutputType = z.infer<typeof OutputSchema>;

// ---------------------------------- 2. Fetcher Function ------------------------------------------

export async function generateSwot(sessionId: string): Promise<OutputType> {
	const res = await anonymized_api.post(url(sessionId));
	return OutputSchema.parse(res);
}
